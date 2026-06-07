from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "crowd_density_secret"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

if __name__ == '__main__':
    app.run(debug=True)