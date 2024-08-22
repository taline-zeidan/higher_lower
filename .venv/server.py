# Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and 9" and
# display a gif of your choice from giphy.com.

from flask import Flask
import random

app = Flask(__name__)

correct_guess = random.randint(0, 9)


@app.route("/")
def guessing_game():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>')


# Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against
# the generated random number. If the number is too low, tell the user it's too low, same with too high or if they
# found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random number
# was 5:

@app.route("/<int:number>")
def validate_guess(number):
    if number > correct_guess:
        return "<h1 style='color: purple'>too high!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif number < correct_guess:
        return "<h1 style='color: red'>too low!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    else:
        return "<h1 style='color: green'>You found me!</h1>"\
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)
