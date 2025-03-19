from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize score
score = {"user": 0, "computer": 0}

@app.route('/')
def index():
    return render_template('index.html', score=score)

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "win"
        score["user"] += 1
    else:
        result = "lose"
        score["computer"] += 1

    return jsonify({
        "result": result,
        "computerChoice": computer_choice,
        "score": score
    })

@app.route('/reset', methods=['POST'])
def reset():
    global score
    score = {"user": 0, "computer": 0}
    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(debug=True)