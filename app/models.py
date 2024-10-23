from django.db import models
class Submit(models.Model):
    stock=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)
class feedback(models.Model):
    userid=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
class complaint(models.Model):
    userid=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    reply=models.CharField(max_length=255,null=True,blank=True)
class helprequest(models.Model):
    userid=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    reply=models.CharField(max_length=255,null=True,blank=True)
class Supplycosubmit(models.Model):
    stock=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.CharField(max_length=20,null=True,blank=True)
class Supplyconotification(models.Model):
    userid=models.CharField(max_length=20,null=True,blank=True)
    notification=models.CharField(max_length=20,null=True,blank=True)
    date=models.CharField(max_length=20,null=True,blank=True)
    
