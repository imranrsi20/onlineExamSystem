
from django.urls import path
from results import views


urlpatterns = [

    path('result/',views.ResultView,name='result'),
    path('search/',views.Search,name='search'),
    path('search_auto/',views.search_auto,name='search_auto'),
    path('test4/',views.test4,name='test4'),
    path('test2/',views.test,name='test'),


]
