from django.urls import path
from.import views
urlpatterns = [
   path('insertempapi',views.saveemp,name = "saveemp"),
   path('',views.insertemp),
]
