from django.urls import path
from . import views
urlpatterns = [
    path('conecter',views.Login),
    path('register',views.Signin),  
    path('adminee',views. MDADMIN,name='adminee') ,
    path('add',views.ADD,name='add'),
    path('edit',views.Edit,name='edit'),
    path('update/<str:id>',views.Update,name='update'),
    path('deleteA/<str:id>',views.Delete_A,name='deleteA'),
    path('conadmine',views.Login_Admin,name = 'login'),
    path('logout', views.logout_V, name='logout'),
    path('out', views.logout_E, name='out'),
    
    #cours 
    path('Mcours',views.Manage_Cours,name ="course"),
    path('add_c',views.ADD_C,name='add_c'),
    path('deleteC/<str:id>', views.Delete_C, name='deleteC'),
    path('edit_c',views.Edit_C,name='edit_c'),
    path('updat/<str:id>',views.Update_C,name='updat'),
    #Questions 
    path('MQuestion',views.Manage_Question),
    path('add_q',views.ADD_Q,name='add_q'),
    path('updatee/<str:id>',views.Update_Q,name='updatee'),
    #Ann
    path('Annonce',views.Admin_An,name="ann"),
    path('delete/<str:id>',views.Delete,name='delete'),
    path('add_A',views.ADD_Ann,name='add_A'),
    path('update_A/<str:id>',views.Update_Ann,name='update_A'),
    
    
    
]