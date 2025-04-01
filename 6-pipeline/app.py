from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Set up an in-memory SQLite database (for demonstration only)
conn = sqlite3.connect(':memory:', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
# Insert a sample user
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
conn.commit()

@app.route('/')
def index():
    return 'Welcome to the Vulnerable Flask App!'

# Vulnerable endpoint: Unsanitized output creates an XSS vulnerability.
@app.route('/search')
def search():
    # Retrieve the 'q' parameter without sanitization
    query = request.args.get('q', '')
    # Directly inject the user input into the HTML response (vulnerable to XSS)
    html = f"<h1>Search Results for: {query}</h1>"
    return html

# Vulnerable endpoint: Constructs SQL queries via string concatenation (SQL injection risk).
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input from form
        username = request.form.get('username')
        password = request.form.get('password')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
