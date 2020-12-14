from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    value = request.form['list']
    print('hello')
    print(value)


if __name__ == '__main__':
    app.run()
