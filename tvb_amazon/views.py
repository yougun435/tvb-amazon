from flask import send_from_directory
from tvb_amazon import app


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./tvb_amazon/static', 'index.html')
