from django.shortcuts import render,HttpResponse
from imdb.models import *
from imdb.utils import *
# Create your views here.
def home(request):
    list_of_movies = Movie.objects.all()
    otp={'list_of_movies':list_of_movies}
    return render(request,'imdb_home.html',otp)

def movie(request,movie_id):
    list_of_actors = Cast.objects.filter(movie_id=movie_id)
    otp={'movies_list':list_of_actors}
    act= Movie.objects.get(movie_id=movie_id)
    ac = {'lsit':act}
    otp.update(ac)
    return render(request,'imdb_movie.html',otp)

def actor(request,actor_id):
    list_of_movies = Movie.objects.filter(actors__actor_id=actor_id)
    otp={'movies_list':list_of_movies}
    act= Actor.objects.get(actor_id=actor_id)
    ac = {'lsit':act}
    otp.update(ac)
    return render(request,'imdb_actor.html',otp)

def director(request,director_id):
    list_of_movies = Movie.objects.filter(director=director_id)
    otp={'movies_list':list_of_movies}
    act= Director.objects.get(id=director_id)
    ac = {'lsit':act}
    otp.update(ac)
    return render(request,'imdb_director.html',otp)

def analytics(request):
    data=get_one_bar_plot_data()
    data1=get_multi_line_plot_data()
    data2=get_two_bar_plot_data()
    data3=get_area_plot_data()
    data4=get_pie_chart_data()
    data.update(data1)
    data.update(data2)
    data.update(data3)
    data.update(data4)
    return render(request,'analytics.html',context=data)

