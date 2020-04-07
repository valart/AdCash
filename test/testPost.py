import requests
import json

def testAddingNewCategory():
    #Getting all categories before adding
    categories = requests.get("http://127.0.0.1:5000/categories")
    data={"name": "Category Test 1"}
    post=requests.post(url="http://127.0.0.1:5000/categories", json=data)
    categoriesAfter = requests.get("http://127.0.0.1:5000/categories")
    assert len(categories.json()) == len(categoriesAfter.json())-1
    assert post.status_code == 200
    #Deleting added category                                 
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(post.json()['id']))

def testAddingExistingCategory():
    #Getting all categories before adding
    data={"name": "Category 1"}
    post1=requests.post(url="http://127.0.0.1:5000/categories", json=data)
    post2=requests.post(url="http://127.0.0.1:5000/categories", json=data)
    assert post2.status_code == 400
    #Delete category
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(post1.json()['id']))

def testAddingProduct():
    #Quite the same test as in testGet.py file
    #Getting all products before adding
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    before = requests.get("http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    post=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    after = requests.get("http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    assert len(before.json()) == len(after.json())-1
    assert post.status_code == 200
    #Deleting added product and category                              
    requests.delete("http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    
def testAddingExistingProduct():
    #Getting all categories before adding
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    requests.post(url="http://127.0.0.1:5000/products", json=productData)
    post=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    assert post.status_code == 400
    #deleting test data
    requests.delete("http://127.0.0.1:5000/categories/"+str(category.json()['id']))

def testAddingProductToNotExistingCategory():
    #Getting all categories before adding
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    post=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    assert post.status_code == 400

def testSendingDataWithWrongKeys():
    #Getting all categories before adding
    categoryData={"nam": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    assert category.status_code == 400
    data={"nam": "Product 4", "category": "Category 10"}
    post=requests.post(url="http://127.0.0.1:5000/products", json=data)
    assert post.status_code == 400
    data={"name": "Product 4", "categori": "Category 10"}
    post=requests.post(url="http://127.0.0.1:5000/products", json=data)
    assert post.status_code == 400
    
