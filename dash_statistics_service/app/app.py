
from datetime import date, timedelta
from generator import generate_records

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/v1/dash/statistics', methods=['GET'])
def welcome():
    n_websites = 50
    days = 10
    generator = generate_records(n_websites=n_websites, start_date=date.today() - timedelta(days=days), end_date=date.today())
    results = []
    for data in generator:
        results.append(data.to_dict())
    return jsonify({"statistics": results})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



