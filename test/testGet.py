import requests

def testGettingAllData():
    #Adding some test data
    categoryData={"name": "Category Test 1"}
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    product=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert len(response.json()) != 0
    #Deleting the same data
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    
def testGetAllCategories():
    before = len(requests.get("http://127.0.0.1:5000/categories").json())
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    after = requests.get("http://127.0.0.1:5000/categories")
    assert after.headers['Content-Type'] == "application/json"
    assert after.status_code == 200
    assert len(after.json())-1 == before
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))


def testGetAllProductsByCategory():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    beforeProducts = requests.get("http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    #Adding new products
    productData1={"name": "Product Test 1", "category": "Category Test 1"}
    productData2={"name": "Product Test 2", "category": "Category Test 1"}
    requests.post(url="http://127.0.0.1:5000/products", json=productData1)
    requests.post(url="http://127.0.0.1:5000/products", json=productData2)
    afterProducts = requests.get("http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    assert afterProducts.headers['Content-Type'] == "application/json"
    assert afterProducts.status_code == 200
    assert len(afterProducts.json())-2==len(beforeProducts.json())
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))

def testGetProductThatNotExists():
    response = requests.get("http://127.0.0.1:5000/categories/100")
    assert response.status_code == 404

def testGetRequestThatNotExists():
    response = requests.get("http://127.0.0.1:5000/category")
    assert response.status_code == 404
