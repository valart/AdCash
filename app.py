#Author: Artjom Valdas

from flask import Flask, abort, request,jsonify
from requests.getRequests import getAllData,getAllCategories, getProductsByCategoryId
from requests.postRequests import addNewCategory, addNewProduct
from requests.deleteRequests import deleteProduct, deleteCategory
from requests.putRequests import updateProduct, updateCategory

app = Flask(__name__)


#GETTING DATA
@app.route('/') #get all data
def index():
    return getAllData()

@app.route('/categories') #get all categories
def GETCategories():
    categories = getAllCategories()
    return jsonify(categories)

@app.route('/categories/<int:category_id>', methods=['GET']) #Get all products by category id
def GETproducts(category_id):
    products=getProductsByCategoryId(category_id)
    return jsonify(products)

#ADDING NEW ITEMS
@app.route('/categories', methods=['POST']) #Adding new category
def createNewCategory():
    if not request.json or 'name' not in request.json:
        abort(400)
    category = addNewCategory(request.json['name'])
    if len(category)==0:
        abort(400)
    return jsonify(category)

@app.route('/products', methods=['POST']) #Adding new product
def createNewProduct():
    if not request.json or 'name' not in request.json or 'category' not in request.json:
        abort(400)
    product=addNewProduct(request.json['name'],request.json['category'])
    if len(product)==0:
        abort(400)
    return jsonify(product)

#DELEING ITEMS
@app.route('/products/<int:product_id>', methods=['DELETE']) #deleting product by id
def DELETEproduct(product_id):
    delete=deleteProduct(product_id)
    if len(delete)==0:
        abort(400)
    return jsonify(delete)

@app.route('/categories/<int:category_id>', methods=['DELETE']) #Deleting category and all product that belong to this category
def DELETEcategory(category_id):
    delete=deleteCategory(category_id)
    if len(delete)==0:
        abort(400)
    return jsonify(delete)

#UPDATING ITEMS
@app.route('/products/<int:product_id>', methods=['PUT']) #Updating product by id
def UPDATEproduct(product_id):
    update = updateProduct(request.json,product_id)
    if len(update)==0 or request.json['name']=="" or request.json['category']=="":
        abort(400)
    return jsonify(update)

@app.route('/categories/<int:category_id>', methods=['PUT']) #Updating category by id. You can noty update Id
def UPDATEcategory(category_id):
    update=updateCategory(request.json,category_id)
    if len(update)==0 or request.json['name']=="":
        abort(400)
    return jsonify(update)


if __name__ == '__main__':
    app.run(debug=True)
