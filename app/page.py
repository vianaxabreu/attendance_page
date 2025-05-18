from flask import Flask, render_template, redirect, request, send_from_directory
from dotenv import load_dotenv
import os

app = Flask(__name__, static_folder="app/static")

@app.route('/')
def qrcode():
    return render_template('qrcode.html')

@app.route('/empty')
def empty():
    return render_template('empty.html')

@app.route('/readme')
def readme():
    return render_template('readme.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def gh_login():
    load_dotenv()
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

    REDIRECT_URI = os.getenv("REDIRECT_URI") # callback
    github_auth_url = "https://github.com/login/oauth/authorize"
    redirect_uri = "http://localhost:5000/callback"
    scope = "read:user user:email"
    return redirect(f"{github_auth_url}?client_id={GITHUB_CLIENT_ID}&redirect_uri={redirect_uri}&scope={scope}")

@app.route('/thankyou')
def thankyou():
    user = request.args.get("user")
    email = request.args.get("email")
    avatar = request.args.get("avatar")
    return render_template('thankyou.html', user=user, email=email, avatar=avatar)

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("app/static", filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)