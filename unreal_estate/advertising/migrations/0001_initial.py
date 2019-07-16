# Generated by Django 2.2.2 on 2019-07-13 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('avg_Rating', models.IntegerField()),
                ('num_Guests', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=30)),
                ('building_type', models.CharField(max_length=20)),
                ('prices', models.IntegerField()),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='advertising.Feature')),
                ('rating_IDs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='advertising.Rating')),
            ],
        ),
    ]