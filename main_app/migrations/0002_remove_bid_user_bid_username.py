# Generated by Django 4.1.2 on 2022-10-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.AddField(
            model_name='bid',
            name='username',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
