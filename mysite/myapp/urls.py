from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', view=views.index),
    path('<int:my_id>/', view=views.indexItem, name='detail')
]
