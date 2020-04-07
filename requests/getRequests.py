from database.dataManipulation import readDatabase
import json
from flask import abort

def getAllData(): #Getting all possible data from database
    return readDatabase()

def getAllCategories():
    #Getting list of all categories
    categories = readDatabase()['category']
    return categories

def getProductsByCategoryId(id):
    #check that category exists
    exist=False
    for value in readDatabase()['category']:
        if value['id']==id:
            exist=True
            break
    if exist == False:
        abort(404)
    #Getting list of all products that belong to given category id
    products = readDatabase()['product']
    correctProduct=[product for product in products if product['categoryId']==id]
    return correctProduct
