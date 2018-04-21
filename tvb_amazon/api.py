from flask import request, Response, render_template
from tvb_amazon.models.product import Product
from tvb_amazon import app

product = Product()


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/api/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        query = request.args['name']
        matches = product.search_by_name(query)

        output_type = request.args.get('output_type', None)
        if output_type == 'html':
            return render_template('results.html', query=query, results=matches)
        else:
            return Response(str(matches), mimetype='application/json', status=200)
    elif request.method == 'POST':
        if request.form['op_type'] == 'insert':
            p = dict()
            p['name'] = request.form['name']
            p['description'] = request.form['description']
            p['price'] = request.form['price']

            product.save(p)

            return Response(str({'status': 'success'}), mimetype='application/json', status=200)
        elif request.form['op_type'] == 'delete':
            _id = request.form['_id']
            product.delete_by_id(_id)

            return Response(str({'status': 'success'}), mimetype='application/json', status=200)
        elif request.form['op_type'] == 'update':
            _id = request.form['_id']

            updated_product = dict()
            if request.form['name'] != '':
                updated_product['name'] = request.form['name']
            if request.form['description'] != '':
                updated_product['description'] = request.form['description']
            if request.form['price'] != '':
                updated_product['price'] = request.form['price']

            product.update_by_id(_id, updated_product)

            return Response(str({'status': 'success'}), mimetype='application/json', status=200)
