# AdCash Internship
**Software Engineering Internship - Backend Services &amp; APIs - Adcash**


The application was written in Python3. This means that You will need Python3 and you will need to install *pytest* to run tests, *requests* to get and send responses and *flask* with the help of what we create a server.
To intsall *pytest*, *requests* and *flask* You can use *pip*

> pip install -U pytest

> pip install -U requests

> pip install -U Flask

Now, to run the server You just have to run app.py file.

Database (json file) is empty, so that it would be nice to add something using Post. But without this, everything works too.

If You would like to run tests, You must go to "test" folder and using command line type 
> pytest `<filename>`.py

## GET requests

### Getting everything in database

http://127.0.0.1:5000/

### Getting the list of all categories

http://127.0.0.1:5000/categories

### Getting the list of products of the concrete category

http://127.0.0.1:5000/categories/<int:category_id>

## POST requests

### Adding a new category

http://127.0.0.1:5000/categories

and sending response should be next : 
```
{
  "name": "Category name"
}
```

### Adding a new product

http://127.0.0.1:5000/products

and sending response should be next : 
```
{
  "name": "Category name",
  "category": "Name on concrete category"
}
```

## PUT requests

### Updating a category

http://127.0.0.1:5000/categories/<int:category_id>

and sending response should be next : 

```
{
  "name": "Category name"
}
```

### Updating a product

http://127.0.0.1:5000/products/<int:product_id>

and sending response should be next : 

```
{
  "name": "Category name",
  "category": "Name on concrete category"
}
```

## DELETE requests

### Deleting a product

http://127.0.0.1:5000/products/<int:product_id>

### Deleting a category

If some products belong to this category, then those products will be also deleted

http://127.0.0.1:5000/categories/<int:category_id>
