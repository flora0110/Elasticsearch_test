from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "test_data"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    results = perform_elasticsearch_search(search_term)
    return render_template('index.html', results=results, search_term=search_term)


def perform_elasticsearch_search(search_term):
    search_url = f"{ELASTICSEARCH_URL}/{INDEX_NAME}/_search"
    query = {
        "query": {
            "match": {
                "content": search_term
            }
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(search_url, headers=headers, data=json.dumps(query))
    results = response.json().get('hits', {}).get('hits', [])
    return results


if __name__ == '__main__':
    app.run(debug=True)
