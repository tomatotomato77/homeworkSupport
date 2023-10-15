from django.urls import path
from . import views
urlpatterns = [
    path("send/",views.indexView,name="send"),
    path("showhistry/",views.showView.as_view(),name="showhistory"),
    path("showresult/",views.resultView.as_view(),name="showresult"),
    path("home/",views.homeView.as_view(),name="home"),
]