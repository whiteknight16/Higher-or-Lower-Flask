from flask import Flask
from random import randint


radom_number = randint(0, 9)
print(radom_number)
app = Flask("__name__")


@app.route("/")
def home():
    return '<h1>Guess the number between 0 to 9</h1>'\
        '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjlkMGNiZmI5MDBmNmQ1YWEwZjM1ZWI0ODU4ZWQwZjZiMzNlNTA3OCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/Kehzyp9EFa2IYDte8P/giphy.gif">'


@app.route("/<number>")
def guess(number):
    if int(number) > radom_number:
        return '<h1 style="color:red">Too High</h1>'\
               '<img src="https://media.giphy.com/media/UFRtykmfyBA8F7qPh9/giphy.gif">'
    elif int(number) < radom_number:
        return '<h1 style="color:orange">Too Low</h1>'\
               '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif">'

    elif int(number) == radom_number:
        return '<h1 style="color:green">Found Me</h1>'\
            '<img src="https://media.giphy.com/media/3oKHWeG1Z8lk1ap1nO/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
