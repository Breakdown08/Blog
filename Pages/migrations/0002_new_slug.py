# Generated by Django 3.2 on 2022-11-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='slug',
            field=models.SlugField(max_length=150, null=True, unique=True, verbose_name='URL поста'),
        ),
    ]
