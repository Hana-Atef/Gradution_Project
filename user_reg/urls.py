from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_form, name='user_insert'), #get & request for insert operation
    path('<int:id>/',views.user_form, name='user_update'), # get & post req for update
    path('delete/<int:id>/',views.user_delete, name='user_delete'),
    path('list/',views.user_list, name='user_list') # get & req to retrieve and display all records
]