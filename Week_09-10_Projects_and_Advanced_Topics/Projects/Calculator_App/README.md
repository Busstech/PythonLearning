
# Flask Calculator Application

This is a simple calculator application built using Flask. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division via a web interface.

---

## Prerequisites

Ensure you have the following installed on your Mac before proceeding:

1. **Python**: Version 3.13 or higher.
   - Confirm installation by running: `python3 --version`
2. **Homebrew**: For installing dependencies.
   - Install Homebrew if not already installed:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
3. **pip**: Python package manager (comes with Python, but ensure it’s upgraded).
   - Upgrade pip:
     ```bash
     python3 -m pip install --upgrade pip
     ```

---

## Setup Instructions

### 1. Clone the Repository
First, clone the repository containing the Flask calculator code:

```bash
git clone https://github.com/your-repo/flask-calculator.git
cd flask-calculator
```

### 2. Create a Virtual Environment
A virtual environment isolates dependencies and ensures no conflicts with global packages:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
# macOS/Linux
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

### 3. Install Flask
Install Flask within the virtual environment:

```bash
pip install flask
```

Verify Flask is installed:

```bash
pip show flask
```

You should see information about the Flask package, including its version and location.

### 4. Run the Application
Start the Flask server to run the calculator app:

```bash
python app.py
```

The app will start, and you should see output similar to:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Visit `http://127.0.0.1:5000` in your browser to use the calculator.

---

## Additional Notes

### How to Deactivate the Virtual Environment
When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

### Install Additional Python Dependencies
If you add new features to the application that require additional Python libraries, install them using `pip` and save the dependencies to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

To reinstall all dependencies from `requirements.txt` (e.g., on a new machine), use:

```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Common Issues

1. **`ModuleNotFoundError: No module named 'flask'`**
   - Ensure the virtual environment is activated (`source venv/bin/activate`).
   - Install Flask: `pip install flask`.

2. **`command not found: python3`**
   - Ensure Python 3 is installed. Install via Homebrew:
     ```bash
     brew install python
     ```

3. **Virtual Environment Activation Fails**
   - If you see an error like `no such file or directory: venv/bin/activate`, ensure the `venv` directory was created:
     ```bash
     python3 -m venv venv
     ```

---

## Next Steps

### Deployment
For production deployment:
1. Use a WSGI server like `Gunicorn`.
2. Set up a reverse proxy with `Nginx` or `Apache`.

Detailed production deployment instructions can be added later.

---

## Author
Your Name  
Email: [your-email@example.com]  
GitHub: [https://github.com/your-profile](https://github.com/your-profile)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
