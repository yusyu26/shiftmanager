from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='shortage_shift_list'),
    path('create/', views.Create.as_view(), name='shortage_shift_create'),
    path('confirm/<int:pk>/',views.Confirmsubstitute.as_view(), name='update'),
    path('signup/',views.signupfunc, name='signup'),
    path('login/',views.loginfunc, name='login'),
    path('logout/',views.logoutfunc, name='logout'),
]
