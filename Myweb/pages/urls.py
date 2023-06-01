from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home),
    path('cours',views.Cours),
    path('question',views.Question),
    path('addQ',views.AddQuest),
    path('addC',views.AddCours),
    path('comments/<str:id>',views.Comments,name='comments'),
    path('comtact',views.Contact),
    path('dep',views.Dep),
    path('profDep',views.Profdep),
    path('profile',views.profile),
    path('srch',views.scrh),
    path('srchQ',views.Question_scrh),
    path('ann',views.Admin_An),
    path('upd',views.update_profile,name= "upd"),
    path('contact',views.send_message,name='send_message') ,
    
]
  