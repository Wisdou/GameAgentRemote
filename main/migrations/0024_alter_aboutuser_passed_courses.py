# Generated by Django 4.0.1 on 2022-05-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_tasks_defaultcode_tasks_tests'),
        ('main', '0023_achievement_condition_achievement_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuser',
            name='passed_courses',
            field=models.ManyToManyField(blank=True, default=[], related_name='users_set', to='course.Articles'),
        ),
    ]
