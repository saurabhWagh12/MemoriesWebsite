from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from .models import *

urlpatterns = [
    path('',home,name="Home"),
    path('getImages/<str:id>/',getAllImages,name="getImages"),
    path('login/',loginPage,name="loginPage"),
    path('register/',register,name="registerPage"),
    path('addMemory/',addMemory,name="AddMemory"),
    path('addtofavourite/<str:id>/',addToFav,name="addingToFavourite"),
    path('showfavourites/',showFav,name="ShowFavourites"),
    path('removefromfavourite/<str:id>/',removeFav,name="RemoveFromFavourite"),
    path('addMoreImages/<str:id>/',addImages,name="AddingMoreImages"),
    path('logout/',loggingOut,name="logoutUser"),
    path('delete/<str:id>/',delete,name="DeleteMemory"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)