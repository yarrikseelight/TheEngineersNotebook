# Generated by Django 4.1.1 on 2023-02-20 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(auto_created=True, default=None),
        ),
    ]