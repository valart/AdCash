import json
from database.dataManipulation import readDatabase,updateItem,getCategoryID

def updateProduct(body,id):
    data=readDatabase()
    for item in data['product']:
        if item['id']==id: #If this product exists
            categoryID=getCategoryID(data['category'],body['category'])
            if categoryID == -1: #There is now such category
                return {}
            #Change all properties
            item['name']=body['name']
            item['categoryId']=categoryID
            updateItem(data)
            return item
    return {}
    
def updateCategory(body,id):
    data=readDatabase()
    for item in data['category']:
        if item['id']==id: #If this category exists
            item['name']=body['name'] #then I can change properties
            updateItem(data)
            return item
    return {}