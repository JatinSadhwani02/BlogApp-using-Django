# Generated by Django 3.2.11 on 2022-01-26 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0008_posts_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author_name',
        ),
    ]