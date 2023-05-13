from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title 

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="subcategory")
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/subcategory/',null=True)
    slug = models.SlugField(unique=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
class Component(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="name of component")
    image = models.ImageField(upload_to = 'uploads/components/')
    stock = models.IntegerField()
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    subcategory_id = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

    def __str__(self):
        return self.name



class Borrower(models.Model):
    barcode = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return str(self.barcode)

    

class BorrowList(models.Model):
    id = models.AutoField(primary_key=True) 
    borrower_id = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)
    pieces = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField()

    def __str__(self):
        return self.component_id.name +" -  "+ str(self.borrower_id)

class Transaction(models.Model):
    fine = models.IntegerField()  
    return_date = models.DateField()



