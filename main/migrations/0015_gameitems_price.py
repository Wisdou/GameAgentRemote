# Generated by Django 4.0.1 on 2022-05-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_aboutuser_active_back_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameitems',
            name='price',
            field=models.SmallIntegerField(default=0),
        ),
    ]
