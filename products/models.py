from django.db import models

class Category(models.Model): #table Category
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Product(models.Model): # table Product
    name = models.CharField(max_length=100) # (null = true) to accepted null
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="photos/%y/%m/%d")
    

    def __str__(self):
        return self.name


#After defining your models, you need to create migrations and apply them to update the database schema: