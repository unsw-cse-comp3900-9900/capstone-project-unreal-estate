# Generated by Django 2.2.2 on 2019-07-16 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suburb', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('latitude', models.FloatField(default=None)),
                ('longitude', models.FloatField(default=None)),
                ('post_code', models.IntegerField(default=None)),
                ('num_room', models.IntegerField(default=None)),
                ('num_bathroom', models.FloatField(default=None)),
                ('num_guests', models.IntegerField(default=None)),
                ('description', models.CharField(max_length=1500)),
                ('space', models.CharField(default=None, max_length=1500)),
                ('name', models.CharField(max_length=100)),
                ('building_type', models.CharField(max_length=20)),
                ('prices', models.FloatField()),
                ('avg_rating', models.FloatField(default=None)),
                ('image', models.URLField(default=None, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('is_anonymous', models.BooleanField(default=False)),
                ('notes', models.CharField(max_length=500)),
                ('property', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertising.Property')),
            ],
        ),
    ]