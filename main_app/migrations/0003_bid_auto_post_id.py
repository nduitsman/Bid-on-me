# Generated by Django 4.1.2 on 2022-10-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_bid_user_bid_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='auto_post_id',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
