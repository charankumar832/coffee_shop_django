from django.db import models

class Product(models.Model):
    product_id=models.CharField(max_length=200, unique=True)
    product_name=models.CharField(max_length=200)
    product_description=models.CharField(max_length=200)
    product_category=models.CharField(max_length=200)
    product_image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product_id+self.product_name
    

class Contact_Query(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    msg=models.CharField(max_length=200)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+" | "+self.email


    