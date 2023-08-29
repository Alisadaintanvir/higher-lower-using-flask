from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
print(random_number)


@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src = 'https://media0.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?"
            "cid=ecf05e47q58c5st3qs02raetqe9jyclyne52y8relf9ofc61&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>")


@app.route("/<int:number>")
def guess_number(number: int):
    if number == random_number:
        return "<h1>You Found Me.</h1>"
    elif number > random_number:
        return "<h1>Too High,Try again.</h1>"
    else:
        return "<h1>Too Low, Try again.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
