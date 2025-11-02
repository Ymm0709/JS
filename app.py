from flask import Flask, jsonify, render_template

app = Flask(__name__)

players = {
    'B费': 'B费摊手',
    '库尼亚': '库尼亚帅锅',
    '阿莫林': '阿莫林惨',
    '梅西': '梅西🈚️'
}

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/players')
def get_players():
    return jsonify(players)

if __name__ == '__main__':
    app.run(debug=True)

