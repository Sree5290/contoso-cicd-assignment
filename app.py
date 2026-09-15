from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Contoso Learning Solutions - CI/CD Deployment Successful!"

@app.route("/about")
def about():
    return "DevOps CI/CD Practical Assignment"

if __name__ == "__main__":
    app.run()
