# Generated by Django 2.2.2 on 2019-07-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0004_auto_20190714_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]