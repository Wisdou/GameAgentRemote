# Generated by Django 3.2.3 on 2022-04-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_aboutuser_subs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('icon', models.ImageField(upload_to='Achievements')),
            ],
        ),
    ]
