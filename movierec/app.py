from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

from openai import OpenAI
client = OpenAI()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # Simulating getting data from an API
    movies = {}
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        movies = recom(movie_title)
        # movies = redirect(url_for('recom', movie_title=movie_title))
        print(movies)
    return render_template('movies.html', movies=movies)

# @app.route('/recom', methods=['GET', 'POST'])
def recom(movie_title):
    # movie_title = request.args.get('movie_title')
    example = {
    "1": {
        "title": "Blade Runner",
        "description": "In a future world where androids are almost indistinguishable from humans, a cop is tasked with hunting down rogue androids in this visually stunning cyberpunk film."
    },
    "2": {
        "title": "Arrival",
        "description": "When mysterious spacecraft touch down across the globe, an elite team is brought together to decipher their intent in this thought-provoking sci-fi film."
    },
    "3": {
        "title": "Interstellar",
        "description": "In a future where Earth is becoming uninhabitable, a team of explorers must travel through a wormhole in space in search of a new home for humanity."
    },
    "4": {
        "title": "Annihilation",
        "description": "A biologist joins a mission into a mysterious environmental disaster zone where the laws of nature don't apply in this mind-bending sci-fi thriller."
    },
    "5": {
        "title": "Elysium",
        "description": "In a dystopian future, the wealthy live on a space station while the rest of the population suffers on a ruined Earth, leading to a struggle for equality."
    }
    }
    messages = [
        {"role": "system", "content": "You are my movie recommendation system called Tony. User will give you a title of a movie and you give them just a title and a short description of 5 movies in the same genre and style in the json format like this example: {example}"},
        {"role": "user", "content": movie_title}
    ]
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object" },
    messages= messages
    )
    recom = completion.choices[0].message.content
    json_object = json.loads(recom)
    return json_object

if __name__ == '__main__':
    app.run(debug=True)
