from database.dataManipulation import readDatabase, addNewItem, getCategoryID

def newID(data, name):
    #Function finds the gighest id and adds to it +1
    id = 0
    for i in data:
        if i['name'] == name: #Already exists
            return -1
        if i['id']>id:
            id=i['id']
    return id+1
    

def addNewCategory(name):
    categoryDatabase = readDatabase()['category']
    id=newID(categoryDatabase, name) #Getting new id for new category
    if id!=-1: #Only if category with this name does not exist
        category=dict()
        category['id']=id
        category['name']=name
        addNewItem('category',category) #Adding new category to database
        return category
    return {}
        
def addNewProduct(name,category):
    categoryDatabase = readDatabase()['category']
    productDatabase = readDatabase()['product']
    id=newID(productDatabase, name)
    categoryID = getCategoryID(categoryDatabase,category)
    if id!=-1 and categoryID!=-1: #Check that given product name and category do not exist
        product=dict()
        product['id']=id
        product['name']=name
        product['categoryId']=categoryID
        addNewItem('product',product) #Adding new product to database
        return product
    return {}
    

