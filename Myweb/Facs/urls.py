from django.urls import path
from . import views
urlpatterns = [
    path('inf',views.Dep_inf),
    path('sm',views.Dep_sm),
    path('st',views.Dep_st),
    path('bio',views.Dep_bio),
    path('sport',views.Dep_sport),
    path('math',views.Dep_math),
] 