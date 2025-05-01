from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (HomeTemplateView)
                      


app_name = "shinapages"
 
urlpatterns = [
    path("", view=HomeTemplateView.as_view(), name="home")
]
