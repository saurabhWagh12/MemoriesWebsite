from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .decorators import *
from django.contrib.auth.models import User
from django.contrib import messages
import time
# import maxminddb
# from django.conf import settings
# import requests


# import folium
# from geopy.geocoders import Nominatim
# Create your views here.
# def home(request):

#     user = MemoryCreator.objects.get(user=request.user)
#     mem = Memory.objects.get(user=request.user)
#     imagesOfMemory = Images.objects.filter(memory=mem)
#     for i in imagesOfMemory:
#         print(i)

#     return render(request,"temp.html",{'user':user,'memory':mem,'images':imagesOfMemory,'user':user})
    # user_ip = request.META.get('REMOTE_ADDR')
    # user_ip="203.192.225.53"
    # YOUR_API_KEY = "639983ba6313c0665456a90ce36a23a1"
    # response = requests.get('http://api.ipstack.com/{}?access_key={}'.format(user_ip, YOUR_API_KEY))
    # if response.status_code == 200:
    #     data = response.json()
    #     latitude = data.get('latitude')
    #     longitude = data.get('longitude')

    # geolocator = Nominatim(user_agent='waghsa1@rknec.edu')
    # location = geolocator.geocode('Shri ramdeobaba college of engineering and management ,nagpur')
    # latitude = location.latitude
    # longitude = location.longitude

    # latitude = 21.176521100000002
    # longitude = 79.06172412550505

    # m=folium.Map(location=[int(latitude),int(longitude)])
    # test = folium.Html('<h3>Maps</h3>', script=True)
    # popup = folium.Popup(test, max_width=500)
    # folium.RegularPolygonMarker(location=[latitude,longitude], popup=popup).add_to(m)
    # m=m._repr_html_()
  # with maxminddb.open_database(settings.GEOIP_PATH) as reader:
    #     response = reader.city(user_ip)
    #     latitude = response.location.latitude
    #     longitude = response.location.longitude


@login_required(login_url='/login/')
def home(request):
    user = MemoryCreator.objects.get(user=request.user)
    mem = Memory.objects.filter(user=request.user)
    memcount = mem.count()

    return render(request,"main.html",{'user':user,'memories':mem,'memoriesCount':memcount})

@login_required(login_url='/login/')
def getAllImages(request,id):
    mem = Memory.objects.get(pk=id)
    imagesOfMemory = Images.objects.filter(memory=mem)
    mylist = []
    myImagename = []
    for image in imagesOfMemory:
        mylist.append(image.image)
        myImagename.append(image.nameImage)
    return render(request,'getImages.html',{'imagesofMemory':imagesOfMemory,'myImages':mylist,'imageNames':myImagename,'idash':id,'imagecount':len(mylist)})



@login_required(login_url='/login/')
def addMemory(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        backgroundImage = request.FILES.get('backgroundImage')
        images = request.FILES.getlist('imagesMultiple')

        # Saving a memory in database:
        mem =  Memory.objects.create(user = request.user,title = title,descrition = description,backgroundImage = backgroundImage)
        mem.save()

        #saving multiple images mapped to above created memory:
        for i in images:
            image = Images.objects.create(memory=mem,image = i)
            image.save()
        mem.save()
    return redirect('/')


@login_required(login_url='/login/')
def addImages(request,id):
    memory = Memory.objects.get(pk=id)
    images = request.FILES.getlist('imagesMultiple')
    for i in images:
            image = Images.objects.create(memory=memory,image = i)
            image.save()
    memory.save()
    return redirect('/getImages/'+id+"/")


@login_required(login_url='/login/')
def addToFav(request,id):
    memory = Memory.objects.get(pk=id)
    memory.favourite = True
    memory.save()
    time.sleep(2)
    return redirect('/')


@login_required(login_url='/login/')
def removeFav(request,id):
    memory = Memory.objects.get(pk=id)
    memory.favourite = False
    memory.save()
    time.sleep(2)
    return redirect('/showfavourites/')


@login_required(login_url='/login/')
def showFav(request):
    memory = Memory.objects.filter(favourite=True)
    print(memory)
    return render(request,'fav.html',{'memories':memory,'memoriesCount':memory.count()})


@unauthenticated_user
def loginPage(request):

    if request.method=="POST":
        name = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request,username=name,password=passw)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'UserName or Password is Incorrect')

    return render(request,'loginPage.html',{})


@unauthenticated_user
def register(request):

    if request.method=="POST":
        username = request.POST.get('username')
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        u = User.objects.create_user(username, email, password)
        u.first_name=firstname
        u.last_name=lastname
        u.save()

        user = MemoryCreator.objects.create(user=u)
        user.save()
        messages.success(request,'Account Created for'+username)
        return redirect('/login/')
    else:
        pass
        # messages.error(request,'not valid try again')    
    return render(request,'register.html')
     
@login_required(login_url='/login/')
def loggingOut(request):
    logout(request)
    return render(request,'loginPage.html',{})

@login_required(login_url='/login/')
def delete(request,id):
    memory = Memory.objects.get(pk=id)
    if memory:
        memory.delete()
    return redirect('/')
