# Generated by Django 5.0.6 on 2024-06-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
