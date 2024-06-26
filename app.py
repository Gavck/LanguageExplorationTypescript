from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/people')
def people():
    data = {
        'firstname': 'Gavin',
        'lastname': 'Kidwell',
        'age': 25,
        'companies': [
            'CCU',
            'GCSD'
        ]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)