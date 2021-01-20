from flask import Flask, render_template


app = Flask(__name__, template_folder="template", static_url_path='/static')


@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/signup')
def signup_page():
    return render_template("signup.html")


@app.route('/signin')
def signin_page():
    return render_template("signin.html")


if __name__ == "__main__":
    app.run(debug=True)
