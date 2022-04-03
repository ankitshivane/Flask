from flask import Flask

myapp=Flask(__name__)

@myapp.route("/")
def functionHello():
    return "Hello, World"

myapp.run(port=5000)
