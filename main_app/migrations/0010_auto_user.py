# Generated by Django 4.1.2 on 2022-10-10 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0009_alter_auto_condition_alter_auto_coverage_preference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
