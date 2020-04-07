import requests

def testUpdatingCategory():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    data={"name": category.json()['name']+"1"}
    putReq=requests.put(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']), json=data)
    assert category.json()['name']+"1"==putReq.json()['name']
    #Deleting test data
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))
    
def testUpdatingProduct():
    categoryData={"name": "Category Test 1"}
    category1=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    categoryData={"name": "Category Test 2"}
    category2=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    #Adding product
    productData1={"name": "Product Test 1", "category": "Category Test 1"}
    product=requests.post(url="http://127.0.0.1:5000/products", json=productData1)
    #Will change first element
    nameBefore = product.json()['name']
    categoryIdBefore = product.json()['categoryId']
    #Change now only name
    data={"name": nameBefore+"1", "category": category1.json()['name']}
    putReq=requests.put(url="http://127.0.0.1:5000/products/"+str(product.json()['id']), json=data)
    nameAfter = putReq.json()['name']
    assert nameBefore+"1"==nameAfter
    #Change now only category
    beforeCount = len(requests.get("http://127.0.0.1:5000/categories/"+str(category2.json()['id'])).json())
    data={"name": nameAfter, "category": category2.json()['name']}
    putReq=requests.put(url="http://127.0.0.1:5000/products/"+str(product.json()['id']), json=data)
    afterCount = len(requests.get("http://127.0.0.1:5000/categories/"+str(category2.json()['id'])).json())
    assert category2.json()['id'] == putReq.json()['categoryId']
    assert beforeCount+1==afterCount
    #Delete everything
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category1.json()['id']))
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category2.json()['id']))

def testUpdatingProductWithNoExsitingCategory():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    product=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    falseData={"name": "Product Test 1", "category": "Category Test 2"}
    putReq=requests.put(url="http://127.0.0.1:5000/products/"+str(product.json()['id']), json=falseData)
    assert putReq.status_code == 400
    #Delete everything
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))

def testUpdatingNotExistingProduct():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    productData={"name": "Product Test 1", "category": "Category Test 1"}
    product=requests.post(url="http://127.0.0.1:5000/products", json=productData)
    newData={"name": "Product Test 1", "category": "Category Test 2"}
    putReq=requests.put(url="http://127.0.0.1:5000/products/"+str(product.json()['id']+1), json=newData)
    assert putReq.status_code == 400
    #Delete everything
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))

def testUpdatingNotExistingCategory():
    categoryData={"name": "Category Test 1"}
    category=requests.post(url="http://127.0.0.1:5000/categories", json=categoryData)
    newData={"name": "Category Test 2"}
    putReq=requests.put(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']+1), json=newData)
    assert putReq.status_code == 400
    #Delete everything
    requests.delete(url="http://127.0.0.1:5000/categories/"+str(category.json()['id']))





    
