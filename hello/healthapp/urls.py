from django.urls import path
from .import views,expert_views,message_views

urlpatterns = [
    path("",views.home,name="home"),
    path("Aboutus/",views.Aboutus,name="Aboutus"),
    path("contactus/",views.contactus,name="contactus"),
    path("login_patient/",views.login_patient,name="login_patient"),
    path("login_expert/",expert_views.login_expert,name="login_expert"),


    path("Registration_patient/",views.Registration_patient,name="Registration_patient"),
    path("Registration_expert/",expert_views.Registration_expert,name="Registration_expert"),
    # path("",views.expert_views,name="Expert_views"),


    path("patient_logout/",views.patient_logout,name="Patient Logout"),
    path("expert_logout/",expert_views.expert_logout,name="Expert Logout"),


    path("patient_Editprofile/",views.patient_Editprofile,name="Patient Editprofile"),
    path("expert_edit/",expert_views.expert_edit,name="Expert Edit"),


    path("patient_home/",views.patient_home,name="patient_home"),
    path("expert_home/",expert_views.expert_home,name="expert_home"),


    path("trial",views.trial,name="Trial"),

    path("compose_message/",message_views.Compose_Message.as_view(),name="compose_message"),
    
    # path("compose_message",message_views.Compose_Message.as_view(),name="compose_message")


    path("inbox/",message_views.User_Inbox.as_view(),name="inbox"),
    path("delete_message/",message_views.Delete_Message.as_view(),name="delete_message"),

    path("Show_Message/<int:msg_id>/",message_views.Show_Message.as_view(),name="Show_Message"),

    path("Tips/",expert_views.Tips_Management.as_view(),name="Tips"),
    path("add_details/",expert_views.Add_details.as_view(),name="add_details"),

    path("View_Expert/",views.View_Expert.as_view(),name="view_expert"),

    path("booking_request/<str:expert_id>/",views.booking_request.as_view(),name="booking_request"),
    path("final_booking_request/",views.final_booking_request.as_view(),name="final_booking_request"),


    
    path("expert_viewbooking/",expert_views.expert_viewbooking.as_view(),name="expert_viewbooking"),
    path("confirm_booking/<int:id>/",expert_views.Confirm_Booking.as_view(),name="confirm_booking"),
    path("cancel_booking/<int:id>/",expert_views.Cancel_Booking.as_view(),name="cancel_booking"),
    path("booking_details/",views.Booking_Details.as_view(),name="booking_details"),


    path("Feedback/<str:exp_name>/",views.feedbacks.as_view(),name="Feedback"),
    path("Final_Feedback/",views.Final_Feedback.as_view(),name="Final_Feedback"),
    path("back/<str:exp_name>/",views.back.as_view(),name="back"),

    path("validate_username/",views.validate_username,name="validate_username"),
    path("validate_username1/",expert_views.validate_username1,name="validate_username1"),

    path("expert_upload_pic/",expert_views.Expert_upload_pic.as_view(),name="expert_upload_pic"),

    path("search/<str:exptype>/",views.SearchResult.as_view(),name="search"),

    path("mess/",views.mess,name="mess"),
    path("health/",views.Health.as_view(),name="health"),

    
    
    


    
]
