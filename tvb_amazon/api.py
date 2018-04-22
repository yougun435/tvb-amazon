from flask import request, Response, render_template, send_from_directory
from tvb_amazon.models.product import ProductModel
from tvb_amazon import app
from tvb_amazon.models.user import UserModel

product_model = ProductModel()
user_model = UserModel()


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/api/product', methods=['POST', 'GET'])
def product():
    if request.method == 'GET':
        query = request.args['name']
        matches = product_model.search_by_name(query)

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

            product_model.save(p)

            return Response(str({'status': 'success'}), mimetype='application/json', status=200)
        elif request.form['op_type'] == 'delete':
            _id = request.form['_id']
            product_model.delete_by_id(_id)

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

            product_model.update_by_id(_id, updated_product)

            return Response(str({'status': 'success'}), mimetype='application/json', status=200)


@app.route('/api/user/<action>', methods=['POST'])
def user(action):
    if action == 'login':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        is_valid = user_model.authenticate(username, password)
        if is_valid:
            return render_template('profile.html')
        else:
            return send_from_directory('./tvb_amazon/static', 'index.html')
    elif action == 'signup':
        name = request.form.get('name', None)
        email = request.form.get('email', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        # TODO : validation

        user_model.add_new_user(name, email, username, password)

        return render_template('profile.html', name=name)

    else:
        status = {
            'status': 'Invalid action'
        }
        return Response(str(status), status=400, mimetype='application/json')
