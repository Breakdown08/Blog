# Generated by Django 3.2 on 2022-11-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_alter_new_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image_original',
            field=models.ImageField(default=None, null=True, upload_to='news_images/', verbose_name='Главное изображение новости'),
        ),
    ]
