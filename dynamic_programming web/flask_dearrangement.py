from flask import Flask, render_template, request
from dearrangement_calculator import dearrangement

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        user_input = int(request.form['user_input'])
        result = dearrangement(user_input)
        return render_template('result.html', result=result, input=user_input)
    except ValueError:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
