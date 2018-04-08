from flask import Flask, send_from_directory, request, Response

app = Flask('mini-amazon', static_url_path='')


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/products', methods=['POST'])
def products():
    product = dict()
    product['name'] = request.form['name']
    product['description'] = request.form['description']
    product['price'] = request.form['price']

    print(product)

    return Response('OK', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
