
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('index/',views.index,name="index"),
    path('Register/',views.register,name="Register"),
    path('Calling/',views.Calling,name="Calling"), 
    path('Counselling/',views.Counselling,name="Counselling"),
    path('joinning/',views.joinning,name="joinning"),
    path('model_html/',views.Register_modelform,name='Register_modelform'),
    path('data_page/',views.data_page,name='data_page'),
    # path('single_data/<pk>',views.single_data,name='single_data')
    path('walkins/',views.Walkins,name='Walkins'),
    path('Calling1/',views.Calling1,name='Calling1'),
    path('Counselling1/',views.Counselling1,name="Counselling1"),
    path('current/',views.current,name="current"),
    path('Dead/<id>',views.Dead,name='Dead'),
    path('Willing/<id>',views.Willing,name='Willing'),
    path('edit/<id>',views.edit,name='edit'),
    path('students/',views.students,name='students'),
    path('complete/<id>',views.complete,name='complete'),
    path('delay/<id>',views.delay,name='delay'),
    path('rejoin/<id>',views.rejoin,name='rejoin'),

]
