from django.db import models

class Logintable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    type=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=20,null=True,blank=True,default='REJECT')

class Userprofile(models.Model):
    login_id=models.ForeignKey(Logintable,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    phoneno=models.CharField(max_length=100,null=True,blank=True)
    
class Stock(models.Model):
    product=models.CharField(max_length=20,null=True,blank=True)
    price=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)


class Supplycostock(models.Model):
    product=models.CharField(max_length=20,null=True,blank=True)
    price=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)

class User(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    userid=models.CharField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)


class feedback(models.Model):
    userid=models.ForeignKey(Logintable,null=True,blank=True,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=255,null=True,blank=True)

class complaint(models.Model):
    userid=models.ForeignKey(Logintable,null=True,blank=True,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=255,null=True,blank=True)
    date=models.CharField(max_length=255,null=True,blank=True)
    reply=models.CharField(max_length=255,null=True,blank=True)

class Shopstockbooking(models.Model):
    product=models.CharField(max_length=255,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)
    date=models.CharField(max_length=255,null=True,blank=True)
    time=models.CharField(max_length=255,null=True,blank=True)
    bookingstatus=models.CharField(max_length=255,null=True,blank=True)


class helprequest(models.Model):
    userid=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    reply=models.CharField(max_length=255,null=True,blank=True)

class Supplycosubmit(models.Model):
    stock=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)

class Supplyconotification(models.Model):
    userid=models.CharField(max_length=200,null=True,blank=True)
    notification=models.CharField(max_length=200,null=True,blank=True)
    date=models.CharField(max_length=200,null=True,blank=True)
    time=models.CharField(max_length=200,null=True,blank=True)

class Shop(models.Model):
    login_id=models.ForeignKey(Logintable,null=True,blank=True,on_delete=models.CASCADE)
    shopname=models.CharField(max_length=20,null=True,blank=True)
    owner=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)
    phoneno=models.CharField(max_length=20,null=True,blank=True)
    openingtime=models.CharField(max_length=20,null=True,blank=True)
    closingtime=models.CharField(max_length=20,null=True,blank=True)

class Supplyco(models.Model):
    login_id=models.ForeignKey(Logintable,null=True,blank=True,on_delete=models.CASCADE)
    shopname=models.CharField(max_length=20,null=True,blank=True)
    owner=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)
    phoneno=models.CharField(max_length=20,null=True,blank=True)
    openingtime=models.CharField(max_length=20,null=True,blank=True)
    closingtime=models.CharField(max_length=20,null=True,blank=True)




    
