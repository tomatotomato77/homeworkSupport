from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("send/",views.indexView,name="send"),
    path("showhistry/",views.showView.as_view(),name="showhistory"),
    path("showresult/",views.resultView.as_view(),name="showresult"),
    path("",views.homeView.as_view(),name="home"),
]