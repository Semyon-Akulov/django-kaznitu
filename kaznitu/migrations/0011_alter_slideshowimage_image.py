# Generated by Django 5.0.2 on 2024-03-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaznitu', '0010_slideshowimage_delete_carouselevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowimage',
            name='image',
            field=models.ImageField(upload_to='photo_for_news/'),
        ),
    ]
