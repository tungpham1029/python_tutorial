# Generated by Django 3.0 on 2020-01-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscoverTheWorld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='discover')),
                ('flag', models.CharField(max_length=100)),
                ('subname', models.CharField(max_length=100)),
                ('catename', models.CharField(max_length=100)),
                ('numpro', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PerfectHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
                ('img', models.ImageField(upload_to='perfecthotel')),
            ],
        ),
        migrations.CreateModel(
            name='TopDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifi', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('bathroom', models.BooleanField(default=False)),
                ('content', models.TextField(max_length=100)),
                ('img', models.ImageField(upload_to='topdestination')),
                ('name', models.CharField(max_length=100)),
                ('star', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='USP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=100)),
                ('img', models.ImageField(upload_to='usp')),
            ],
        ),
        migrations.CreateModel(
            name='VisitorExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='visitexp')),
                ('name', models.CharField(max_length=100)),
                ('firm', models.CharField(max_length=100)),
                ('context', models.TextField(max_length=100)),
            ],
        ),
    ]
