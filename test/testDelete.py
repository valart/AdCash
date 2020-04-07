import requests

def testDeletingProduct():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    product=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    before=len(requests.get("http://127.0.0.1:5000/categories/"+str(category.json()['id'])).json())
    requests.delete(url="http://127.0.0.1:5000/products/"+str(product.json()['id']))
    after=len(requests.get("http://127.0.0.1:5000/categories/"+str(category.json()['id'])).json())
    assert before-1==after
    #Deleting Category
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))


def testDeletingCategory():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    product=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    before=len(requests.get("http://127.0.0.1:5000/categories").json())
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    after=len(requests.get("http://127.0.0.1:5000/categories").json())
    assert before-1==after
    
def testDeleteNotExistingProduct():
    delete=requests.delete(url="http://127.0.0.1:5000/products/400")
    assert delete.status_code == 400

def testDeleteNotExistingCategory():
    delete=requests.delete(url="http://127.0.0.1:5000/categories/400")
    assert delete.status_code == 400
