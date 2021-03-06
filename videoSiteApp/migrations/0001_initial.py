# Generated by Django 2.0.2 on 2018-03-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, null=True, unique=True)),
                ('name', models.TextField()),
                ('numberofsubscribers', models.IntegerField(blank=True, db_column='numberOfSubscribers', null=True)),
                ('averageviewsallvideos', models.IntegerField(blank=True, db_column='averageViewsAllVideos', null=True)),
            ],
            options={
                'db_table': 'channel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idsubject', models.IntegerField(db_column='idSubject')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Todayvideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtodayvideo', models.IntegerField(db_column='idTodayVideo')),
                ('name', models.TextField()),
                ('url', models.TextField()),
                ('channelurl', models.TextField(blank=True, db_column='channelUrl', null=True)),
                ('numberofviews', models.IntegerField(blank=True, db_column='numberOfViews', null=True)),
                ('date', models.TextField()),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('dislikes', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'todayVideo',
                'managed': False,
            },
        ),
    ]
