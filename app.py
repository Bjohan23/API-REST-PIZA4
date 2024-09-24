from flask import Flask, request, jsonify#se importa la clase Flask de flask para crear la aplicacion, request para obtener los datos de la peticion y jsonify para devolver los datos en formato json
from products import products

app = Flask(__name__)#iniciamos la aplicacion de flask con el nombre de la aplicacion (__name__)

@app.route('/', methods=['GET'])
def get_welcome():
    return ({'message': 'Welcome to the store'})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<string:product_name>', methods=['GET'])
def get_product(product_name):
    product = [product for product in products if product['name'] == product_name]
    if len(product) > 0:##si la longitud de la lista es mayor a 0, es decir si hay un producto con ese nombre
        return jsonify(product[0])
    return jsonify({'message': 'Product no encontrado'})

@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message': 'Product added', 'products': products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def update_product(product_name):
    product = [product for product in products if product['name'] == product_name]
    if len(product) > 0:
        product[0]['name'] = request.json['name']
        product[0]['price'] = request.json['price']
        product[0]['quantity'] = request.json['quantity']
        return jsonify({'message': 'Product updated', 'product': product[0]})
    return jsonify({'message': 'Product no encontrado'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    product = [product for product in products if product['name'] == product_name]
    if len(product) > 0:
        products.remove(product[0])
        return jsonify({'message': 'Product deleted', 'products': products})
    return jsonify({'message': 'Product no encontrado'})





if __name__ == "__main__":#inicializamos el servidor de flask en el puerto 5000 y en modo debug para que se reinicie automaticamente
    # app.run(debug=True,port=4000)
    app.run(debug=True)