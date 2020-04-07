import json

def readDatabase():
    #Reading file and getting data from it
    with open('database.json') as json_file:
        return json.load(json_file)

def writeDatabase(data):
    #Getting data and writing it to file
    outfile = open('database.json', "w")
    json.dump(data, outfile,indent=2)
    outfile.close()
    

def addNewItem(classifiaction,item):
    data=readDatabase()
    data[classifiaction].append(item) #adding new item
    writeDatabase(data)
    
def deleteItem(classifiaction,item):
    data=readDatabase()
    data[classifiaction]=item #Adding new items without deleted item
    writeDatabase(data)
    
def updateItem(data):
    writeDatabase(data)
    
def getCategoryID(data,name):
    #Function that returns given category or product id
    for i in data:
        if i['name']==name:
            return i['id']
    return -1