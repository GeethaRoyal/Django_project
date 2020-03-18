# Generated by Django 3.0.4 on 2020-03-18 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('fb_likes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('pay_actor', models.FloatField(default=0)),
                ('pay_direct', models.FloatField(default=0)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('no_of_facebook_likes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('collections', models.FloatField()),
                ('year_of_release', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('avg_rate', models.CharField(max_length=100)),
                ('imdb_link', models.URLField()),
                ('budget', models.CharField(max_length=100)),
                ('image', models.URLField(null=True)),
                ('genere', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('no_of_users_voted', models.CharField(max_length=100)),
                ('actors', models.ManyToManyField(through='imdb.Cast', to='imdb.Actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Director')),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Movie'),
        ),
    ]
