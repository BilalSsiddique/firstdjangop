from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.welcome, name='home'),
    path('load_form', views.load_form, name='load_form'),
    path('add', views.add, name='add'),
    path('show', views.show, name='showall'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('showproject', views.showproject, name='showproject'),
    path('addproject', views.addproject, name='addproject'),
    path('addpr', views.addprd, name='addprs'),
]
