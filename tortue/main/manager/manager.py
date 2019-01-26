import json
from flask import Flask, render_template

from tortue.main.common.utils.configuration import Configuration
from tortue.main.common.dao.mongo.scrapper_dao import ScrapperDAO
from tortue.main.common.dao.mongo.raw_data_DAO import RawDataDAO

app = Flask(__name__)

Configuration.instance().load_from_file("./tortue.json")


@app.route("/")
def home():
    return render_template('layout.html')


@app.route('/metrics')
def metrics():
    dao = RawDataDAO()

    return '{' \
           '"total_subjects": %i,' \
           '"pending_subjects": %i,' \
           '"ready_subjects": %i,' \
           '"learned_subjects": %i' \
           '}' % (
               dao.count(), dao.count_by_status('PENDING'), dao.count_by_status('READY'), dao.count_by_status('LEARN')
           )


@app.route('/subjects/pending/<number_of_elements_to_fetch>')
def pending_subjects(number_of_elements_to_fetch):
    data = []

    for s in RawDataDAO().find_n_by_status(number_of_elements_to_fetch, 'PENDING'):
        data.append(s.to_json())

    return json.dumps(data)


@app.route('/workers')
def workers():
    data = []

    for s in ScrapperDAO().find_n_elements(3):
        data.append(s.to_json())

    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=True)
