from django.urls import path
from . import views

urlpatterns=[
    path('books/add',views.add_book,name='add'),
    path('books/',views.display,name='list'),
    path('',views.home,name='home'),
    path('books/<int:id>/update',views.update,name='update'),
    path('books/<int:id>/delete',views.delete_book,name='delete'),

]