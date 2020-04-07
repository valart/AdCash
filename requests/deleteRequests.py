from database.dataManipulation import readDatabase, deleteItem
import json

def deleteProduct(itemID):
    products=readDatabase()['product'] #Getting list of all products
    data=[]
    delete=[]
    for value in products:
        if value['id'] != itemID: #Adding all product that does not belong to given id
            data.append(value)
        else:
            delete.append(value)
    if len(delete)!=0:
        deleteItem('product',data)
        return delete #returning deleted product
    return []
    
def deleteCategory(categoryID):
    #First of all I try to find all products that belong to this category
    #If they exist then I delete them
    products=readDatabase()['product']
    data = [value for value in products if value['categoryId'] != categoryID]
    deleteItem('product',data)
   
    #Finally I delete category in the same principle as product deleting
    categories=readDatabase()['category']
    data=[]
    delete=[]
    for value in categories:
        if value['id'] != categoryID:
            data.append(value)
        else:
            delete.append(value)
    if len(delete)!=0:
        deleteItem('category',data)
        return delete
    return []