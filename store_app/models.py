from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name 
   
class Brand(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name 
   
class Color(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=50)
    def __str__(self):
        return self.name 
   
class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 TO 10000', '1000 TO 10000'),
        ('10000 TO 20000','10000 TO 20000'),
        ('20000 TO 30000', '20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000')
    )

    price=models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price 
   


class Product(models.Model):
    CONDITION = (
        ('New', 'New'),
        ('Old', 'Old')
    )
    STOCK=(('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
    STATUS=(('Publish','Publish'),('Draft','Draft'))


    unique_id=models.CharField(unique=True,max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='Product_images/img')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    condition=models.CharField(choices=CONDITION,max_length=100)
    information=models.TextField()
    description=models.TextField()
    stock=models.CharField(choices=STOCK,max_length=200)
    status=models.CharField(choices=STATUS,max_length=200)
    created_date=models.DateField(default=timezone.now,max_length=200)
    
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs) 
    def __str__(self):
        return self.name
    


class Images(models.Model):
    image=models.ImageField(upload_to='Product_images/img')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)



class Tag(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class Contact_Us(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    address=models.TextField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    postcode=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField() 

    amount=models.IntegerField()
    payment_id=models.CharField(max_length=200, null=True, blank=True)
    paid=models.BooleanField(default=False, null=True)
    date=models.DateField(default='datetime.date.today')   
    
    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=123)
    image=models.ImageField(upload_to='Product_images/Order_Img')
    quantity=models.CharField(max_length=123)
    price=models.CharField(max_length=123)
    total=models.CharField(max_length=1203)

    def __str__(self):
        return self.order.user.username