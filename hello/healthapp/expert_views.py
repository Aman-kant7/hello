from django.shortcuts import render,HttpResponse,redirect
from.models import HealthExperts,Tips,Expert_detail,Booking_Request
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import JsonResponse



# def demo(request):
#      print("hello")
#      return HttpResponse(request,"<h1>hello</h1>")
def Registration_expert(request):
     if request.method=="GET":          
          return render(request,'healthapp/expert/Registration_expert.html') 

     if request.method=="POST":     
          cusername=request.POST["txtusername"]
          cpassword=request.POST["txtpassword"]
          cname=request.POST["txtname"]
          cemail=request.POST["txtemail"]
          cphone=request.POST["txtphone"]
          caddress=request.POST["txtaddress"]
          ccity=request.POST["txtcity"]
          cgender=request.POST["txtgender"]
          cexpertypes=request.POST["txtselect"]

          healthexperts=HealthExperts(user_name=cusername,password=cpassword,name=cname,email=cemail,phone=cphone,address=caddress,city=ccity,gender=cgender,expertype=cexpertypes)

          healthexperts.save()
          messages.success(request,"Thank you for Registration_expert Please to login")

     return render(request,'healthapp/expert/Registration_expert.html',)

def login_expert(request):
     if request.method == 'GET':
          return render(request,'healthapp/expert/login_expert.html')  

     if request.method=="POST":     
          username = request.POST["txtusername"]
          password = request.POST["txtpassword"]    
          e=HealthExperts.objects.filter(user_name=username,password=password)
          if len(e)>0:
               request.session["user_key"]=username
               request.session["user_type"]="HealthExpert"
               user_objects=HealthExperts.objects.get(user_name=username) #fetch individual objects
               context={
                    "userdata":user_objects  
               }
               return render(request,'healthapp/expert/expert_home.html',context)
          else:
               messages.error(request,"Invaild Credentials")     
               return redirect("login_expert")

####code for logout########################
def expert_logout(request):    
    del request.session['user_key']
    return redirect("login_expert")               

### Expert Edit profile 0##### 
def expert_edit(request):
     if "user_key" in request.session.keys():

          loggedinuser_name=request.session['user_key']   
          if request.method =="GET":
               user_objects=HealthExperts.objects.get(user_name=loggedinuser_name)
               context={
                    "userdata":user_objects
                    }
               return render(request, 'healthapp/expert/expert_edit.html',context)
               
          if request.method == 'POST':
               Emailid=request.POST["txtemail"]
               Phone=request.POST["txtphone"]
               address=request.POST["txtaddress"]
               city=request.POST["txtcity"]
               expertype=request.POST["txtselect"]
               print(Emailid,Phone,address,city,expertype)

               user_objects=HealthExperts.objects.get(user_name=loggedinuser_name)
               user_objects.email=Emailid
               user_objects.phone=Phone
               user_objects.address=address
               user_objects.city=city
               user_objects.expertype=expertype
               user_objects.save()
               context={
                    "userdata":user_objects
                    }
               messages.success(request,"Profile update successfully")
               return render(request,'healthapp/expert/expert_edit.html',context)     
     else:
               messages.error(request,"please do login first")
               return redirect('home')     

def expert_home(request):
     return render(request,'healthapp/expert/expert_home.html')

# def compose_message(request):
#      if request.method=='GET':
#           return render(request,'healthapp/expert/compose_message.html')  
# 
class Expert_upload_pic(View):
     def post(self, request):
          loggedinuser_name=request.session["user_key"]
          expert_pic=request.FILES['file_upload']
          print("fileupload",expert_pic)
          fs=FileSystemStorage()
          file_obj=fs.save(expert_pic.name,expert_pic)
          print("name",expert_pic.name)
          print("fileobj",file_obj)
          print("base",fs.base_url)
          uploaded_file_url=fs.url(file_obj)
          print("file urls is",uploaded_file_url)
          expert_object=HealthExperts.objects.get(user_name=loggedinuser_name)
          expert_object.pic_name=expert_pic.name
          expert_object.save()
          context={
               "userdata":expert_object,
               "file_url":uploaded_file_url
               }
          return render(request,'healthapp/expert/expert_home.html',context)




             


class Tips_Management(View):
     def get(self, request):
          if "user_key" in request.session.keys():

               user_role=request.session["user_type"]
               
               if user_role=='HealthExpert':
                    return render(request,'healthapp/expert/Tips.html')    
          else:
               messages.error(request,"please do login first")
               return redirect('home')

     def post(self,request):
          user_name=request.session["user_key"]
          tips_content=request.POST['txtcontent']
          h=HealthExperts.objects.get(user_name=user_name) #import healthexpert attribute 
          print(h.user_name)
          Tip=Tips(username=h,tips_content=tips_content)
          Tip.save()
          
         # user_name=='HealthExpert'
          messages.success(request,"Thanks you for message!")
          return redirect('Tips')

class Add_details(View):
     def get(self, request):
          if "user_key" in request.session.keys():
               user_name=request.session["user_key"]
               #print(user_role)
               user_object=HealthExperts.objects.get(user_name=user_name)
               context={
                    "userdata": user_object
               }
               
               
               return render(request,'healthapp/expert/add_details.html',context)    
          else:
               messages.error(request,"please do login first")
               return redirect('home')         
     def post(self,request):
          user_name=request.session["user_key"]
          experience=request.POST["txtexperience"]
          skills=request.POST["txtskill"]
          about=request.POST["txtabout"]
          qualification=request.POST["txtqualification"]
          E=HealthExperts.objects.get(user_name=user_name) #import healthexpert attribute 
          a=Expert_detail(user_name=E,experience=experience,skills=skills,about=about,qualification=qualification)
          a.save()


          messages.success(request,"Thanks you for message!")
          return redirect('add_details')

class expert_viewbooking(View):
     def get(self, request):
          if "user_key" in request.session.keys():

               user_name=request.session["user_key"]
               booking=Booking_Request.objects.filter(expert_user_name=user_name)
               # print(booking)
               context={
                    "expert_user":booking  
               }
               
               return render(request,'healthapp/expert/expert_viewbooking.html',context)    
         
class Confirm_Booking(View):
     def get (self,request,id):
          if "user_key" in request.session.keys():

               user_name=request.session["user_key"]
               booking=Booking_Request.objects.filter(expert_user_name=user_name)
               # print(booking)
               context={
                    "expert_user":booking  
               }
               booking_request_obj=Booking_Request.objects.get(id=id)
               booking_request_obj.status="confirm"
               booking_request_obj.response_text="Booking has been confirmed"
               booking_request_obj.save()
               messages.success(request,"Booking has been confirmed")

               return render(request,'healthapp/expert/expert_viewbooking.html',context)     

class Cancel_Booking(View):
     def get (self,request,id):
          if "user_key" in request.session.keys():

               user_name=request.session["user_key"]
               booking=Booking_Request.objects.filter(expert_user_name=user_name)
               # print(booking)
               context={
                    "expert_user":booking  
               }
               booking_request_obj=Booking_Request.objects.get(id=id)
               booking_request_obj.status="cancel"
               booking_request_obj.response_text="Booking has been cancelled"
               booking_request_obj.save()
               messages.success(request,"Booking has been cancelled")

               return render(request,'healthapp/expert/expert_viewbooking.html',context)                

def validate_username1(request):
    username=request.GET['username']
    data={
     #    'exists':Patient.objects.filter(user_name__iexact=username).exists()
        'exists':HealthExperts.objects.filter(user_name__iexact=username).exists()

    }         
    return JsonResponse(data)               