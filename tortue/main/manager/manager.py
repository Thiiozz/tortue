import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('layout.html')


@app.route('/metrics')
def metrics():
    return '{' \
           '"total_subjects": 10,' \
           '"pending_subjects": 7,' \
           '"ready_subjects": 2,' \
           '"learned_subjects": 1' \
           '}'


@app.route('/subjects/pending/<number_of_elements_to_fetch>')
def pending_subjects(number_of_elements_to_fetch):
    data = []

    el = '{"title": "Tiger Nixon", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi nec ' \
         'mauris at tellus semper maximus. Morbi nec mauris at tellus semper maximus max ... "}'

    for _ in range(0, int(number_of_elements_to_fetch)):
        data.append(el)

    return json.dumps(data)


@app.route('/workers')
def workers():
    data = []

    el = '{"id": "ear19a1fvea1981", "last_seen": "01/02/03 10:22:56"}'

    for _ in range(0, 2):
        data.append(el)

    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=True)
