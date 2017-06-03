from django.conf.urls import url
from . import views
from TOPA.views import InicioView

urlpatterns = [
    url(r'^', views.ejemplo),
    url(r'^inicio/', InicioView.as_view(), name="inicio"),
]
