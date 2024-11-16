from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv
import logging
import os
import pymysql

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Database Configuration
DB_USER = os.getenv('DB_USER', 'todo_app_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'YourStrongPassword123!')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'todo_app_db')

# Debug logging for database configuration
logger.info(f"Database Configuration:")
logger.info(f"User: {DB_USER}")
logger.info(f"Host: {DB_HOST}")
logger.info(f"Database: {DB_NAME}")

# Verify database configuration
if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
    raise ValueError("Missing database configuration. Check your .env file.")

# Database connection string
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Database connection settings
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True  # Enable SQL query logging

# Initialize SQLAlchemy
db = SQLAlchemy(app)

class Todo(db.Model):
    """Todo model for database"""
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    category = db.Column(db.String(50))
    due_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Todo object to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

def test_db_connection():
    """Test database connection"""
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        connection.close()
        logger.info("Database connection test successful!")
        return True
    except Exception as e:
        logger.error(f"Database connection test failed: {e}")
        return False

@app.route('/')
def index():
    """Main page route handler"""
    try:
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return render_template('index.html', todos=todos)
    except Exception as e:
        logger.error(f"Error in index route: {str(e)}")
        return render_template('error.html', message="Unable to fetch todos."), 500

@app.route('/add_todo', methods=['POST'])
def add_todo():
    """Add new todo route handler"""
    try:
        data = request.form
        due_date = None
        if data.get('due_date'):
            try:
                due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Invalid date format'}), 400

        new_todo = Todo(
            title=data['title'],
            description=data.get('description', ''),
            category=data.get('category', 'general'),
            due_date=due_date,
            status='pending'
        )

        db.session.add(new_todo)
        db.session.commit()
        logger.info(f"Added new todo: {new_todo.title}")
        return redirect(url_for('index'))

    except Exception as e:
        logger.error(f"Error adding todo: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Failed to add todo'}), 500

@app.route('/update_status/<int:todo_id>', methods=['POST'])
def update_status(todo_id):
    """Update todo status route handler"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        new_status = request.json.get('status')

        if new_status not in ['pending', 'completed']:
            return jsonify({'error': 'Invalid status'}), 400

        todo.status = new_status
        db.session.commit()
        logger.info(f"Updated todo status: ID {todo_id} to {new_status}")
        return jsonify({'success': True, 'status': new_status})

    except Exception as e:
        logger.error(f"Error updating todo status: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Failed to update status'}), 500

@app.route('/delete_todo/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete todo route handler"""
    try:
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        logger.info(f"Deleted todo: ID {todo_id}")
        return jsonify({'success': True})

    except Exception as e:
        logger.error(f"Error deleting todo: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Failed to delete todo'}), 500

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """API endpoint to get all todos"""
    try:
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return jsonify({'todos': [todo.to_dict() for todo in todos]})
    except Exception as e:
        logger.error(f"Error in get_todos API: {str(e)}")
        return jsonify({'error': 'Failed to fetch todos'}), 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('error.html', message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('error.html', message="Internal server error"), 500

def init_db():
    """Initialize the database"""
    try:
        # Test database connection first
        if not test_db_connection():
            raise Exception("Failed to connect to database")

        with app.app_context():
            db.create_all()
            logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise

if __name__ == '__main__':
    # Initialize the database
    init_db()
    
    # Run the application
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=port, debug=debug)