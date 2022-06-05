from django.shortcuts import render,HttpResponse,redirect
from.models import Contact,HealthCampaign,Patient,User_Message
from django.contrib import messages
from django.views import View





class Compose_Message(View):
     def get(self, request):
          if "user_key" in request.session.keys():

               user_role=request.session["user_type"]
               if user_role=="Patient":
                     return render(request,'healthapp/patient/compose_message.html')
               if user_role=='HealthExpert':
                    return render(request,'healthapp/expert/compose_message.html')    
          else:
               messages.error(request,"please do login first")
               return redirect('home')

     def post(self,request):
          user_role=request.session["user_type"]
          receiver_id=request.POST['txtreceiverid']
          sender_id=request.session["user_key"]
          subject=request.POST['txtmessage']
          content=request.POST['txtcontent']
          user_msg=User_Message(receiver_id=receiver_id,sender_id=sender_id,subject=subject,content=content)
          user_msg.save()


          if user_role=='Patient':
               messages.success(request,"Thanks you for message!")
               return render(request,'healthapp/patient/compose_message.html') 

          if user_role=='HealthExpert':
               messages.success(request,"Thanks you for message!")
               return render(request,'healthapp/expert/compose_message.html')


# def compose_message(request):    
#     if request.method=='GET':
#         return render(request,'healthapp/patient/compose_message.html')


class User_Inbox(View):
     def get(self, request):
          if "user_key" in request.session.keys():

               user_id = request.session["user_key"]
               user_role=request.session["user_type"]
               message_objects=User_Message.objects.filter(receiver_id=user_id) #return multiple objects
          # print(message_objects)

               context={
                    "msg":message_objects
               }
               if user_role=="Patient":
                    return render (request,'healthapp/patient/patient_index.html',context)
               if user_role=='HealthExpert':
                    return render(request,'healthapp/expert/expert_index.html',context)        
          else:
               messages.error(request,"please do login first")
               return redirect('home')


class Delete_Message(View):
     def post(self,request):
          user_id=request.session["user_key"]
          user_role=request.session["user_type"]
          message_objects_list=request.POST.getlist("chk")
          # print(message_objects_list) #[1,2]
          for msg_id in message_objects_list:
               # print(msg_id) 
               msg_object=User_Message.objects.get(id=msg_id)
               msg_object.delete()
          message_objects=User_Message.objects.filter(receiver_id=user_id)#return multiple message_objects
          context={
                    "msg":message_objects
               }
          if user_role=="Patient":
                return render (request,'healthapp/patient/patient_index.html',context)
          if user_role=='HealthExpert':
                return render(request,'healthapp/expert/expert_index.html',context)  


class Show_Message(View):
     def get(self, request,msg_id):
          user_id=request.session["user_key"]
          user_role=request.session["user_type"]
          message_object=User_Message.objects.get(id=msg_id)
          print(message_object)
          context={
               "msg":message_object
               }
          if user_role=="Patient":
               return render(request,'healthapp/patient/patient_Show_Message.html',context)     

          if user_role=='HealthExpert':
                return render(request,'healthapp/expert/expert_show_message.html',context)       
