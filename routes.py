from flask import Flask, render_template, request, url_for, redirect, jsonify

# Init Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = HomeworkUser.query.all()
    return render_template('index.html', title='Home', users=users)

if __name__ == "__main__":
    app.run()
