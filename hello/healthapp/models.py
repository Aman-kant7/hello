from tabnanny import verbose
from unicodedata import name
from urllib import request, response
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
class Contact(models.Model):
     name=models.CharField(max_length=45,null=False)
     email=models.EmailField(max_length=45,null=False)
     phone=models.CharField(max_length=10,null=False)
     your_query=models.TextField()
     date=models.DateField(default=timezone.now)
     def __str__(self): ##It is used to represent an object into string format
          return self.name  


class HealthCampaign(models.Model):
     campaig_id=models.AutoField(primary_key=True)
     description=models.CharField(max_length=100)
     organizer_name=models.CharField(max_length=45,null=False)
     date=models.DateField()
     pic_name=models.ImageField(max_length=255,upload_to="healthapp/campaign_pic",default="")
     def __str__(self): ##It is used to represent an object into string format
          return self.organizer_name       


class HealthExperts(models.Model):
     user_name=models.CharField(max_length=45,primary_key=True)
     password=models.CharField(max_length=45,null=False)
     name=models.CharField(max_length=45,null=False)
     email=models.EmailField(max_length=45,null=False)
     phone=models.CharField(max_length=10,null=False)
     address=models.CharField(max_length=45,null=False)
     city=models.CharField(max_length=45,null=False)
     gender=models.CharField(max_length=6,null=False)
     expertype=models.CharField(max_length=45,null=False)
     date=models.DateField(default=timezone.now)
     pic_name=models.FileField(max_length=255,upload_to="healthapp/campaign_pic",default="")

class Patient(models.Model):
     user_name = models.CharField(max_length=45,primary_key=True)
     password=models.CharField(max_length=45,null=False)
     name=models.CharField(max_length=45,null=False)
     email=models.EmailField(max_length=45,null=False)
     phone=models.CharField(max_length=10,null=False)
     address=models.CharField(max_length=45,null=False)
     date=models.DateField(default=timezone.now)

class Feed_back(models.Model):
     user_name = models.ForeignKey(Patient,null=False,on_delete=models.DO_NOTHING)
     expert_name = models.CharField(max_length=45,null=False)
     feedback_text = models.TextField()
     rating=models.IntegerField()
     date=models.DateField(default=timezone.now)

class User_Message(models.Model):
     receiver_id=models.CharField(max_length=45, default=None)
     sender_id=models.CharField(max_length=45,default=None)
     subject=models.CharField(max_length=100,null=False)
     content=models.TextField(null=False)
     date=models.DateField(default=timezone.now)
     receiver_status=models.BooleanField(default=True ,null=True)
     sender_status=models.BooleanField(default=True , null=True)
     def __str__(self):
          return self.subject

     def get_absolute_url(self):
          return reverse('Show_Message',args=[(self.id)]) #return the url on the basis of viewname    



class Tips(models.Model):
     username=models.ForeignKey(HealthExperts,on_delete=models.DO_NOTHING)
     tips_content=models.TextField(null=False)
     date=models.DateField(default=timezone.now)

class Expert_detail(models.Model):
     user_name = models.OneToOneField(HealthExperts,null=False,on_delete=models.DO_NOTHING)
     experience=models.CharField(max_length=45,null=False)
     skills=models.CharField(max_length=45,null=False)
     about=models.TextField( )
     qualification=models.CharField(max_length=45,null=False)
     status=models.CharField(max_length=45, default="not")
     

class Booking_Request(models.Model):
     from_Date=models.DateField(verbose_name="start_date",default=timezone.now)   
     to_Date=models.DateField(verbose_name="end_date",default=timezone.now)
     user_name = models.ForeignKey(Patient,null=False,on_delete=models.DO_NOTHING)
     expert_user_name = models.CharField(max_length=45,null=False,default="abc")
     request_date=models.DateField(default=timezone.now)
     status=models.CharField(max_length=50,default="not_comfirm")
     response_text=models.CharField( max_length=50,null=False,default="No response")
     user_message_text=models.CharField(max_length=45,null=False,default=" ")



     

class Prediction(models.Model):
    name = models.CharField(max_length=45)
    age= models.PositiveIntegerField(null=True, blank=True)
    gender=models.PositiveIntegerField(null=True, blank=True)
    hemoglobin= models.DecimalField(null=True, blank=True,decimal_places=2 , max_digits=5)
    weight= models.PositiveIntegerField(null=True, blank=True)
    diastolic_l=models.PositiveIntegerField(null=True, blank=True)
    systolic_h=models.PositiveIntegerField(null=True, blank=True)
    heartbeat= models.PositiveIntegerField(null=True, blank=True)
    predicted_value=models.CharField(max_length=100,blank=True)
     