from imdb.models import *
from django.db.models import Q
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractQuarter, ExtractWeek,
ExtractWeekDay, ExtractIsoYear, ExtractYear,)

def get_one_bar_plot_data():
    import json
    from imdb.models import Movie,Director,Actor
    # collections= Movie.objects.values_list('collections',flat=True)
    collections = """ 
                select AVG(collections) 
                    from imdb_movie 
                    group by genere """
    collect=execute_sql_query(collections)
    year ="""
        select strftime("%Y",release_date)
            from imdb_movie as m  
                INNER JOIN imdb_director as d 
                    on m.director_id = d.id
                    """
    genere= Movie.objects.values_list('genere',flat=True).distinct()
    name = execute_sql_query(year)
    single_bar_chart_data = {
        "labels": list(genere),
        "datasets":
        [
            {
                "label":"Average collections(in crores) for the genre",
                "data":list(collect),
                "name": "Single Bar Chart",
                "borderColor": "rgba(255, 255, 255, 0.9)",
                "border_width": "10",
                "backgroundColor": "rgba(255,91, 70,0.9)"
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Collections for Genre'
    }


def get_polar_chart_data():
    import json
    from imdb.models import Movie
    collections = """ 
                select AVG(collections) 
                    from imdb_movie 
                    group by genere """
    collect=execute_sql_query(collections)
    gener= Movie.objects.values_list('genere',flat=True).distinct()
    # name = execute_sql_query(year)
    # collections= Movie.objects.values_list('collections',flat=True)
    # name = Movie.objects.values_list('name',flat=True)
    polar_chart_data = {
        "datasets": [{
            "data": list(collect),
            "backgroundColor": [
                "rgba(123, 123, 0,0.9)",
                "rgba(123, 0, 255,0.8)",
                "rgba(0, 1, 0,0.7)",
                "rgba(0,0,153,0.2)",
                "rgba(90, 123, 255,0.5)"
            ]

        }],
        "labels": list(gener)
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }

def get_two_bar_plot_data():
    import json
    from imdb.models import Movie,Director
    data1 ="""
        select 100.0*COUNT(dataset.gender)/(
                                        select COUNT(*) 
                                            from imdb_director
                                    ) 
        from (select collections,
                    gender,
                    strftime("%Y",release_date) as year 
                from imdb_movie as m  
                    INNER JOIN imdb_director as d 
                        on m.director_id = d.id 
            ) as dataset
        where gender='Male'
        group by dataset.year,gender
        order by dataset.year
    
    """
    " WHERE dataset.gender ='Male'"
    data2 ="""
        select 100.0*COUNT(dataset.gender)/(
                                        select COUNT(*) 
                                            from imdb_director
                                    ) 
        from (select collections,
                    gender,
                    strftime("%Y",release_date) as year 
                from imdb_movie as m  
                    INNER JOIN imdb_director as d 
                        on m.director_id = d.id 
            ) as dataset
        WHERE dataset.gender = 'Female'
        group by dataset.year 
        order by dataset.year
    
    """
    year ="""
            select distinct strftime("%Y",release_date) as year 
            from imdb_movie as m
            order by year
    """
    data=execute_sql_query(year)
    data1=execute_sql_query(data1)
    data2 = execute_sql_query(data2)
    multi_bar_plot_data = {
        "labels": data,
        "datasets": [
            {
                "label": "Male",
                "data": list(data1),
                "borderColor": "rgba(0, 100, 100, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 100, 100,0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "Female",
                "data": list(data2),
                "borderColor": "rgba(0,200,0,0.49)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,200,0,0.34)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Percentage of Directors per year based on gender'
    }


def get_multi_line_plot_data():
    import json
    data=Cast.objects.values_list('pay_actor',flat=True)[:10]
    data1=Cast.objects.values_list('pay_direct',flat=True)[:10]
    data2 =Movie.objects.values_list('collections',flat=True)[:10]
    data3=Cast.objects.values_list('movie_id',flat=True).distinct()[:10]
    multi_line_plot_data = {
        "labels":list(data3),
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "actors pay",
            "data": list(data),
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "directors pay",
            "data": list(data1),
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 6,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        },
        {
            "label": "collections",
            "data": list(data2),
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(255,167,0,0.9)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 6,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(255,167,0,0.75)',
        }
        ]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Title'
    }


def get_area_plot_data():
    import json
    
    year ="""
            select distinct strftime("%Y",release_date) as year 
            from imdb_movie as m
            order by year
    """
    remuneration= """ select pay_actor from imdb_cast where actor_id =4"""
    remuneration=execute_sql_query(remuneration)
    data = execute_sql_query(year)
    area_plot_data = {
        "labels":data,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": list(remuneration),
            "label": "Remuneration",
            "backgroundColor": 'rgba(100,103,255,.15)',
            "borderColor": 'rgba(30,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(255,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'Earnings of Theo James for the timeline'
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "My Second dataset",
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Title'
    }


def get_doughnut_chart_data():
    import json
    doughnut_graph_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4"
        ]
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Title'
    }


def get_multi_line_plot_with_area_data():
    import json
    multi_line_plot_with_area_data = {
        "labels": [
            "January", "February", "March", "April", "May", "June",
            "July"],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "My First dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data": [22, 44, 67, 43, 76, 45, 12]
            },
            {
                "label": "My Second dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [16, 32, 18, 26, 42, 33, 44]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Title'
    }


def get_pie_chart_data():
    import json
    data=""" 
        select 100.0*COUNT(gender)/(
                                        select COUNT(*) 
                                            from imdb_director
                                    ) 
                from imdb_director 
                    group by gender 
                    order by gender
        """
    data=execute_sql_query(data)
    pie_chart_data = {
        "datasets": [{
            "data": data,
            "backgroundColor": [
                "rgba(255, 123, 255,0.6)",
                "rgba(0, 123, 255,0.7)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 0,0,0.9)",
                "rgba(0, 123, 0,0.7)"
            ]

        }],
        "labels": [
            "Female",
            "Male"
            
        ]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Percentage of Directors grouped by Gender'
    }

def execute_sql_query(sql_query):
    from imdb.utils import Movie,Director,Actor,Cast,Rating
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows


def populate_database():
    import json
    f=open('/home/geetha/Desktop/complete_data/actors_5000.json','r')
    # actors_list=json.load(f)
    f=open('/home/geetha/Desktop/complete_data/directors_5000.json','r')
    # directors_list =json.load(f)
    f=open('/home/geetha/Desktop/complete_data/movies_5000.json','r')
    movies_list =json.load(f)
    actors_list,directors_list=[],[]
    for actor in actors_list:
        Actor.objects.create(name=actor["name"],actor_id=actor["actor_id"],gender=actor['gender'],
        fb_likes=actor['fb_likes'])
		
    for actor in directors_list:
        Director.objects.create(name=actor['name'],gender=actor['gender'],
        no_of_facebook_likes=actor['no_of_facebook_likes'])
	
    for movies in movies_list:
        x= Movie.objects.create(name=movies["name"],
        movie_id=movies['movie_id'],
        collections=movies["box_office_collection_in_crores"],
        year_of_release=movies["year_of_release"],
        language = movies['language'],
        director=Director.objects.get(name=movies['director_name']),
        country=movies['country'],
        avg_rate=movies['average_rating'],
        imdb_link = movies['imdb_link'],
        budget = movies['budget'],
        genere=movies['genres'][0],
        duration = movies['duration'],
        no_of_users_voted = movies['no_of_users_voted']
        )
        for actor in movies['actors']:
            Cast.objects.create(
                actor=Actor.objects.get(actor_id=actor['actor_id']),
            movie=x,role=actor['role'])
	