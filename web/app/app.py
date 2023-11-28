from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

ELASTICSEARCH_URL = "http://host.docker.internal:9200"
INDEX_NAME = "law_test_data"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    results = perform_elasticsearch_search(search_term)
    
    return render_template('index.html', results=results, search_term=search_term)

@app.route('/health')
def health():
    response = requests.get("http://host.docker.internal:9200/_cluster/health")
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON content
        json_content = response.json()

        # Return the JSON content as a response
        return jsonify(json_content)
    else:
        # If the request was not successful, return an error response
        return jsonify({"error": f"Request failed with status code {response.status_code}"})

def perform_elasticsearch_search(search_term):
    print("search_term")
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
    app.run(host='0.0.0.0',port=5000,debug=True)
