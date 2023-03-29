"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS,3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route("/game")
def show_madlib_form():
    """Get user response for playing a game"""

    player_choice = request.args.get("game_response")

    #if playerchoice = no; return goodbye.html
    #otherwise, cont. to game.html

    if player_choice == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route("/madlib")
def show_madlib():
    """Returns player's madlib"""
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adjective")
    loc = request.args.get("place")
    celebrities = request.args.getlist("celebrities")

    random_file = choice(["madlib.html", "madlib2.html", "madlib3.html"])

# getlist - turns all options into a list... in html file (madlib)
    # for celeb in celebrity; celeb1 = this; increment to get celeb2 (do in jinji2 however)

    return render_template(random_file, color=color, noun=noun, adj=adj, place=loc, celebrities=celebrities)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
