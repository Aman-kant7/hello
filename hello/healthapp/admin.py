from django.contrib import admin

from healthapp.expert_views import expert_viewbooking
from.models import Booking_Request, Contact,HealthCampaign,Feed_back, HealthExperts, Patient, User_Message,Tips,Expert_detail


class HealthExpertsAdmin(admin.ModelAdmin):

     list_display=('name','email','phone','address','city','expertype')    
     list_filter=['name','city']
     search_fields=('city','phone','expertype')

class PatientAdmin(admin.ModelAdmin):

     list_display=('name','email','phone','address')
     list_filter=['name','address']
     search_fields=('phone','address')



class User_MessageAdmin(admin.ModelAdmin):

     list_display=('receiver_id','sender_id','subject','date')
     list_filter=['date']
     search_fields=('sender_id','receiver_id','date')



class HealthcampaignAdmin(admin.ModelAdmin):
     list_display=('description','organizer_name')
     list_filter=['organizer_name']
     search_fields=('organizer_name',)




class ContactAdmin(admin.ModelAdmin):
     list_display=('name','email','phone','date')
     list_filter=['date']
     search_fields=('date',)
     


class FeedbackAdmin(admin.ModelAdmin):
     list_display=('user_name','expert_name','rating','date')
     list_filter=['rating','expert_name']
     search_fields=('date','rating')



class TipsAdmin(admin.ModelAdmin):
     list_display=('username','date')
     list_filter=['date']
     search_fields=('date','username')


class Expert_detailAdmin(admin.ModelAdmin):
     list_display=('user_name','experience','qualification')
     list_filter=['experience','qualification']
     search_fields=('experience','qualification')


class Booking_RequestAdmin(admin.ModelAdmin):
     list_display=('from_Date','to_Date','expert_user_name')
     list_filter=['expert_user_name']
     search_fields=('expert_user_name',)
     






# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(HealthCampaign,HealthcampaignAdmin)
admin.site.register(Feed_back,FeedbackAdmin)
admin.site.register(HealthExperts,HealthExpertsAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(User_Message,User_MessageAdmin)
admin.site.register(Expert_detail,Expert_detailAdmin)
admin.site.register(Tips, TipsAdmin)
admin.site.register(Booking_Request,Booking_RequestAdmin)
# admin.site.register(expert_viewbooking)
# admin.site.register()

admin.site.site_header="Health and Fitness Administration"
admin.site.site_title="Health and Fitness Admin Dashborad"
admin.site.index_title="welcome to Health and Fitness"





