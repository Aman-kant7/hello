from django.shortcuts import render,HttpResponse,redirect
from.models import Booking_Request, Contact,HealthCampaign, HealthExperts,Patient,Tips,Expert_detail,Booking_Request,Feed_back,Prediction
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from sklearn.tree import DecisionTreeClassifier
import joblib
import pandas as pd



###  code_home.##
def home(request):
    # data_dict={
    #     "info": 
    #     "Data from view"
    # },data_dict

    campaign = HealthCampaign.objects.all()
    a=Tips.objects.all()
    context={
        "info": campaign,
        "tips":a 

    }
    return render(request,'healthapp/html/home.html',context)



### code of Aboutus###
def Aboutus(request):
    return render(request,'healthapp/html/Aboutus.html')   


def trial(request):
    return render(request,'healthapp/patient/trial.html')



 #### code of Contactus Page ###   
def contactus(request):


    if request.method=="GET":
        return render(request,'healthapp/html/contactus.html')    

    if request.method=="POST":
        # print(request.POST)#built in dictionary
        cname=request.POST["txtname"]  #it is used to get the values from textboxes
        cemail=request.POST["txtemail"]
        cphone=request.POST["txtphone"]
        cquery=request.POST["txtquery"]
        # print(cname,cemail,cphone,cquery)

        contact=Contact(name=cname,email=cemail,phone=cphone,your_query=cquery) #creating object of contactus
        contact.save()
        print("contact Added")
        messages.success(request,"Thankyou for Contacting Us")

    return render(request,'healthapp/html/contactus.html')
         
### code of patient_Registration ### 
def Registration_patient(request):

    if request.method == "GET":

        return render(request,'healthapp/patient/Registration_patient.html')   

    if request.method == "POST":
        cusername=request.POST["txtusername"]      
        cpassword=request.POST["txtpassword"]   
        cname=request.POST["txtname"]
        cemail=request.POST["txtemail"]
        cphone=request.POST["txtphone"]
        caddress=request.POST["txtaddress"]

        patient=Patient(user_name=cusername,password=cpassword,name=cname,email=cemail,phone=cphone,address=caddress)

        patient.save()
        messages.success(request,"Thankyou For Regitration please to login")

    return render(request,'healthapp/patient/Registration_patient.html')    

  

### code of Login_patient###
def login_patient(request):
    if request.method=="GET":
        return render(request,'healthapp/patient/login_patient.html')

    if request.method=="POST":
        username=request.POST["txtusername"]
        password=request.POST["txtpassword"]
        p=Patient.objects.filter(user_name=username,password=password)
        if len (p)>0:
            request.session["user_key"]=username
            request.session["user_type"]="Patient"
            user_objects=Patient.objects.get(user_name=username) #fetch individual object      

            context={
                "userdata":user_objects
            }
            return render(request,'healthapp/patient/patient_home.html',context)
        else:
            messages.error(request,"Invaild Credentials")
            return redirect("login_patient")


#####code for patient_logout ########
def patient_logout(request):
    del request.session['user_key']
    return redirect("login_patient")


###patient_home################################
def patient_home(request):
    if "user_key" in request.session.keys():
        return  render(request,'healthapp/patient/patient_home.html')
    else:
        return redirect('home')
###  patient_Editprofile   #####
def patient_Editprofile(request):
    if "user_key" in request.session.keys():

        loggedinuser_name=request.session["user_key"]
        if request.method =="GET":
            user_objects=Patient.objects.get(user_name=loggedinuser_name)
            context={
                "userdata":user_objects
                }
            return render(request,'healthapp/patient/patient_Editprofile.html',context)

        if request.method == 'POST':
            Emailid=request.POST["txtemail"]
            Phone=request.POST["txtphone"]
            address=request.POST["txtaddress"]
            
            print(Emailid, Phone, address)
            user_objects=Patient.objects.get(user_name=loggedinuser_name)
            user_objects.email=Emailid
            user_objects.phone=Phone
            user_objects.address=address
            user_objects.save()
            context={
                "userdata":user_objects
                }
            messages.success(request,"Profile update successfully")    
            return render(request,'healthapp/patient/patient_Editprofile.html',context)
    else:
               messages.error(request,"please do login first")
               return redirect('home')



class View_Expert(View):
     def get(self, request):

        user_Objects=Expert_detail.objects.all()
        context={
            "userdata":user_Objects
        }
        # return render(request,'healthapp/html/view_expert.html',context)
        if "user_key" in request.session.keys():
            return render(request,'healthapp/patient/p_view_expert.html',context)               
            


        else:
            return render(request,'healthapp/html/view_expert.html',context)


class booking_request(View):
    def get(self, request,expert_id):
        context={
             "e_id":expert_id
            }

        
        return render(request,'healthapp/patient/booking_request.html',context)

class final_booking_request(View):
            def post(self,request):
                u_name=request.session["user_key"]
                expert_id = request.POST["txtexpert_id"]
                fromdate=request.POST["fromdate"]
                todate=request.POST["todate"]
                message=request.POST["txtmessage"]
                p=Patient.objects.get(user_name=u_name)
                b=Booking_Request(from_Date=fromdate,to_Date=todate,user_name=p,expert_user_name=expert_id,user_message_text=message)
                b.save()
                messages.success(request,"thanks you for Booking")    

                return render(request,'healthapp/patient/booking_request.html')

class Booking_Details(View):
    def get(self, request):    
          if "user_key" in request.session.keys():
                u_name=request.session["user_key"]

                booking_obj=Booking_Request.objects.filter(user_name=u_name)
                context={
                    "booking":booking_obj
                    }
                return render(request,'healthapp/patient/booking_details.html',context)


        

class feedbacks(View):
    def get(self, request,exp_name):
        if "user_key" in request.session.keys():
            
            context={
                "exp_name":exp_name
            }
            return render(request,'healthapp/patient/Feedback.html',context)

class Final_Feedback(View):
    def post(self,request):
        u_name=request.session["user_key"]
        expert_id = request.POST["txtexpert_id"]
        feedback=request.POST["txtfeedback"]
        rating=request.POST["txtrating"]
        p=Patient.objects.get(user_name=u_name)
        f=Feed_back(user_name=p,expert_name=expert_id,feedback_text=feedback,rating=rating)
        f.save()
        messages.success(request,"thanks you for feedback") 

        return render(request,'healthapp/patient/Feedback.html')
        
class back(View):
     def get(self, request,exp_name):
        # if "user_key" in request.session.keys():
             user_objects=Feed_back.objects.filter(expert_name=exp_name)

             context={
                     "exp_name":user_objects
                 }

             return render(request,'healthapp/html/feedback.html',context)       


def validate_username(request):
    username=request.GET['username']
    data={
        'exists':Patient.objects.filter(user_name__iexact=username).exists()
        # 'exists':Health.objects.filter(user_name__iexact=username).exists()

    }         
    return JsonResponse(data)


class SearchResult(View):
    def get(self, request,exptype):
        expert_objects=HealthExperts.objects.filter(expertype=exptype)
        if (len(expert_objects)>0):
            context={
                "expdata":expert_objects
            }
            return render (request,'healthapp/html/search.html',context)
        else:
            messages.success(request,"This type of Expert not avilable")  
            
            return redirect('home')

def mess(request):       
     messages.success(request,"Please Login First")    
     return redirect('home') 



class Health(View):

    def get(self,request):

        return render(request, 'healthapp/html/health.html') 

    def post(self,request):
        name=request.POST["txtname"]
        age=request.POST["txtage"]
        gender=request.POST["txtgender"]
        hemoglobin=request.POST["txthemoglobin"]
        weight=request.POST["txtweight"]
        upper_bp=request.POST["txtsystolic"]
        lower_bp=request.POST["txtdiastolic"]
        heartbeat=request.POST["txtheartbeat"]
        print(name,age,gender,hemoglobin,weight,lower_bp,upper_bp,heartbeat)
        ml_model=joblib.load("ml_model/heathandfitness_modal.joblib")
        print(ml_model)
        predicted_value=ml_model.predict([[int(gender),float(hemoglobin),int(heartbeat),int(upper_bp),int(lower_bp)]])
        print(predicted_value)
        p=Prediction(predicted_value=predicted_value,name=name,age=age,gender=gender,hemoglobin=hemoglobin,weight=weight,systolic_h=upper_bp,diastolic_l=lower_bp,heartbeat=heartbeat)
        p.save()

        
        str= predicted_value
        if str.__contains__("1"):
            status="conguration you are healthy"
        else:
            status="please take care your health"
        context={
            "health":status
        }
     

        return render(request, 'healthapp/html/health.html',context) 

        


