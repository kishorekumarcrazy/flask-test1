from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_trusted_url(url):
    # You can implement your logic to check whether the URL is trusted or fake
    # For simplicity, let's just check if the URL starts with "https://" as an example
    return url.startswith("https://")

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'URL not provided'}), 400

    url = data['url']
    is_trusted = is_trusted_url(url)

    return jsonify({'url': url, 'is_trusted': is_trusted})

if __name__ == '__main__':
    app.run(debug=True)
