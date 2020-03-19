FROM imdb.models import *

def get_one_bar_plot_data():
    import json
    FROM imdb.models import Movie,Director,Actor
    # collections= Movie.objects.values_list('collections',flat=True)
    collections = """ 
            SELECT avg
            FROM(
                    SELECT AVG(collections) as avg
                        FROM imdb_movie 
                        GROUP BY genere 
                        ORDER BY genere
                )
            ORDER BY avg DESC  LIMIT 10
            """
    collect=execute_sql_query(collections)
    genere= """
            SELECT genere
            FROM(
                    SELECT AVG(collections) as avg,genere
                        FROM imdb_movie 
                        GROUP BY genere 
                        ORDER BY genere
                )
            ORDER BY avg DESC  LIMIT 10
                """
    genere=execute_sql_query(genere)
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

def get_two_bar_plot_data():
    import json
    FROM imdb.models import Movie,Director
    data1 ="""
    SELECT (
                SELECT COUNT(*)
                FROM imdb_movie as dataset
                INNER JOIN imdb_director as d
                    ON dataset.director_id = d.id
                WHERE d.gender = 'female' 
                and dataset.year_of_release = m.year_of_Release
                GROUP BY dataset.year_of_release 
            )
        FROM imdb_movie as m
        INNER JOIN imdb_director as dd
            ON m.director_id = dd.id
        GROUP BY m.year_of_release
        ORDER BY m.year_of_release DESC 
        LIMIT 10
    """
    data2="""
    SELECT (
            SELECT COUNT(*)
            FROM imdb_movie as dataset
            INNER JOIN imdb_director as d
                ON dataset.director_id = d.id
            WHERE d.gender = 'male' 
            and dataset.year_of_release = m.year_of_Release
            GROUP BY dataset.year_of_release 
        )
        FROM imdb_movie as m
        INNER JOIN imdb_director as dd
            ON m.director_id = dd.id
        GROUP BY m.year_of_release
        ORDER BY m.year_of_release DESC 
        LIMIT 10
    """
    year_of_release ="""
            SELECT distinct year_of_release
            FROM imdb_movie 
            ORDER BY year_of_release DESC 
            LIMIT 10
    """
    data=execute_sql_query(year_of_release)
    data1=execute_sql_query(data1)
    data2 = execute_sql_query(data2)
    multi_bar_plot_data = {
        "labels": data,
        "datasets": [
            {
                "label": "Male",
                "data": data2,
                "borderColor": "rgba(0, 100, 100, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 100, 100,0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "Female",
                "data": data1,
                "borderColor": "rgba(0,200,0,0.49)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,200,0,0.34)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Percentage of Directors per year_of_release based on gender'
    }


def get_multi_line_plot_data():
    import json
    data="""
        SELECT SUM(budget)
        FROM imdb_movie 
        WHERE country like 'South Korea' 
        GROUP BY year_of_release
        ORDER BY year_of_release DESC
        """
    year_of_release ="""
            SELECT distinct year_of_release
            FROM imdb_movie 
            ORDER BY year_of_release DESC 
            LIMIT 10
    """
    data3=execute_sql_query(year_of_release)
    data1="""
        SELECT SUM(collections*10000000)  
        FROM imdb_movie 
        WHERE country like 'South Korea' 
        GROUP BY year_of_release
        ORDER BY year_of_release DESC
    """
    data1=execute_sql_query(data1)
    data=execute_sql_query(data)
    multi_line_plot_data = {
        "labels":list(data3),
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "sum of collections",
            "data": list(data1),
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "sum of budget",
            "data": list(data),
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 6,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }
        ]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Comparison of budget and collections per year for Movies in South Korea'
    }


def get_area_plot_data():
    import json
    
    year_of_release ="""
            SELECT year_of_release
            FROM imdb_movie 
            GROUP BY year_of_release
            ORDER BY year_of_release DESC 
            LIMIT 10
    """
    remuneration ="""
        SELECT (
                SELECT COUNT(*)
                FROM imdb_movie as m
                WHERE director_id = 39 
                    and m.year_of_release = m1.year_of_release
                GROUP BY year_of_release
            )
            FROM imdb_movie as m1
            GROUP BY year_of_release
            ORDER BY year_of_release DESC 
            LIMIT 10
            """
    remuneration=execute_sql_query(remuneration)
    data = execute_sql_query(year_of_release)
    area_plot_data = {
        "labels":data,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": remuneration,
            "label": "COUNT",
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
        'area_plot_data_one_title': 'COUNT of movies in a decade by Steven Spielberg'
    }
def get_pie_chart_data():
    import json
    data=""" 
        SELECT 100.0*COUNT(gender)/(
                                        SELECT COUNT(*) 
                                            FROM imdb_director
                                    ) 
        FROM imdb_director 
        GROUP BY gender 
        ORDER BY gender
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
    FROM imdb.utils import Movie,Director,Actor,Cast
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` FROM django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    FROM django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows


def populate_database():
    import json
    f=open('/home/geetha/Desktop/complete_data/actors_5000.json','r')
    actors_list=json.load(f)
    f=open('/home/geetha/Desktop/complete_data/directors_5000.json','r')
    directors_list =json.load(f)
    f=open('/home/geetha/Desktop/complete_data/movies_5000.json','r')
    movies_list =json.load(f)
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
        year_of_release_of_release=movies["year_of_release_of_release"],
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
	