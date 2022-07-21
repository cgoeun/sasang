from django.urls import path
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    path('upload/', views.upload),
    path('download/', views.download),
    path('form/basic/', views.basic_form),
    path('form/model/', views.form_model),

    path('template/', views.template),
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show, name='show'),
    # path parameter
    path('<str:year>/<int:month>',views.date),
    # query parameter
    path('search/', views.search),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post),
    # path('show/', views.show, name ='show'),
]
