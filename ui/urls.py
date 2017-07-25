from django.conf.urls import url, include
from .views import Index, Insults

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^insults$', Insults.as_view(), name="Insults"),

]