# Generated by Django 5.0.2 on 2024-03-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaznitu', '0009_carouselevent_delete_carouselitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slideshow_images/')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.DeleteModel(
            name='CarouselEvent',
        ),
    ]
