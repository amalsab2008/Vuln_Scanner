from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Vulnerable Test App</h2>

    <form action="/search">
        <input name="q">
        <input type="submit">
    </form>

    <form action="/login">
        <input name="username">
        <input name="password">
        <input type="submit">
    </form>
    """

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return f"Search Result: {q}"

@app.route("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    if "' OR '1'='1" in username:
        return "Database Error: SQL Syntax Error"

    return "Login Failed"

app.run(debug=True)