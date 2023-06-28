from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'esto es secreto'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html', gold=session['gold'], activities=session['activities'])


@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        earned_gold = random.randint(10, 20)
        session['gold'] += earned_gold
        session['activities'].append(
            f"Earned {earned_gold} gold from the farm.")
    elif building == 'cave':
        earned_gold = random.randint(5, 10)
        session['gold'] += earned_gold
        session['activities'].append(
            f"Earned {earned_gold} gold from the cave.")
    elif building == 'house':
        earned_gold = random.randint(2, 5)
        session['gold'] += earned_gold
        session['activities'].append(
            f"Earned {earned_gold} gold from the house.")
    elif building == 'casino':
        earned_gold = random.randint(-50, 50)
        session['gold'] += earned_gold
        if earned_gold > 0:
            session['activities'].append(
                f"Earned {earned_gold} gold from the casino.")
        else:
            session['activities'].append(
                f"Entered a casino and lost {abs(earned_gold)} gold.")

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
