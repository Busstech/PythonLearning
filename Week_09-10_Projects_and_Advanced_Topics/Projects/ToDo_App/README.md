
# Flask Todo Application

A modern, database-driven Todo application built with Flask and MySQL. This application allows users to create, read, update, and delete todo items with categories, due dates, and status tracking.

---

## Features

✨ Create new todo items with titles, descriptions, and categories  
📅 Set due dates for tasks  
✅ Mark todos as completed/pending  
🗑️ Delete todos  
🏷️ Category-based organization  
🔄 Real-time status updates  
📱 Responsive web interface  

---

## Technology Stack

- **Backend**: Python/Flask  
- **Database**: MySQL  
- **ORM**: SQLAlchemy  
- **Frontend**: HTML, CSS (Tailwind CSS)  

---

## Database Schema

```sql
CREATE TABLE todo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500),
    category VARCHAR(50),
    due_date DATETIME,
    status VARCHAR(20) DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

## Setup Guide

### Prerequisites

- **Python**: Version 3.8+  
- **MySQL**: Version 5.7+  
- **pip**: Python package manager  

### 1. Database Setup

Connect to MySQL and run the following commands:

```bash
# Login to MySQL
mysql -u root -p

# Create Database and User
CREATE DATABASE todo_app_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'todo_app_user'@'localhost' IDENTIFIED BY 'YourStrongPassword123!';
GRANT ALL PRIVILEGES ON todo_app_db.* TO 'todo_app_user'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Application Setup

```bash
# Clone the repository
git clone <repository-url>
cd todo-app

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory with the following content:

```env
DB_USER=todo_app_user
DB_PASSWORD=YourStrongPassword123!
DB_HOST=localhost
DB_NAME=todo_app_db
FLASK_ENV=development
PORT=5001
```

### 4. Run the Application

Start the application using:

```bash
python app.py
```

Visit [http://localhost:5001](http://localhost:5001) in your browser.

---

## Project Structure

```
Todo_App/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore             # Git ignore file
├── static/                # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/             # HTML templates
│   ├── index.html
│   └── error.html
└── README.md              # Documentation
```

---

## API Endpoints

| Endpoint               | Method | Description              | Parameters                        |
|------------------------|--------|--------------------------|------------------------------------|
| `/`                    | GET    | Main todo list page      | None                               |
| `/add_todo`            | POST   | Create new todo          | `title`, `description`, `category`, `due_date` |
| `/update_status/<id>`  | POST   | Update todo status       | `status` (pending/completed)      |
| `/delete_todo/<id>`    | POST   | Delete todo              | None                               |
| `/api/todos`           | GET    | Get all todos (JSON)     | None                               |

---

## Error Handling

The application includes comprehensive error handling for:  
- Database connection errors  
- Input validation  
- 404 and 500 error pages  
- Transaction rollbacks  
- Detailed error logging  

---

## Troubleshooting

### Common Issues

1. **Port Already in Use**:  
   - Ensure the specified port (default: `5001`) is not already being used.

2. **Database Connection Failed**:  
   - Verify MySQL is running.
   - Check credentials in `.env`.
   - Ensure the `todo_app_db` database exists.

3. **Package Installation Issues**:  
   - Ensure dependencies are listed in `requirements.txt`.

---

## Development

### Running Tests

```bash
# Run unit tests (if any)
pytest
```

### Code Style

```bash
# Use flake8 or pylint for linting
flake8 app.py
```

---

## Security Notes

⚠️ Never commit the `.env` file.  
🔒 Use strong passwords for database credentials.  
🔐 Keep MySQL credentials secure.  
📝 Apply regular security updates.  
🔍 Monitor error logs frequently.  

---

## Contributing

1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:  
   ```bash
   git commit -m 'Add AmazingFeature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Support

For support, email support@busstech.com

---

### Made with ❤️ by Warren Le Roux
