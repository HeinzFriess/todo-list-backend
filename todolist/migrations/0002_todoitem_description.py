# Generated by Django 4.2.2 on 2023-06-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
