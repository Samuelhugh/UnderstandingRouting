from flask import Flask  # Importing flask. Important!
web = Flask(__name__)  # Creating a New Flask instance.
@web.route('/')  # "@" decorator associates this route with the function immediately following.
def hello():
    return 'Hello World!'
@web.route('/dojo')  # "@" decorator associates this route with the function immediately following.
def dojo():
    return 'Dojo!'
@web.route('/say/<name>')  # "@" decorator associates this route with the function immediately following.
def say(name):
    return f'Hi {name}!'
@web.route('/repeat/<int:num>/<name>')  # "@" decorator associates this route with the function immediately following.
def repeat(num, name):
    return f'{num * name}'
if __name__ == "__main__":  # Ensures this file is being run directly and not from a different module.
    web.run(debug=True)  #Runs the server "web" in debug mode.