# Generated by Django 5.0.2 on 2024-03-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaznitu', '0016_remove_slide_image_slide_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo_for_news/')),
            ],
        ),
        migrations.DeleteModel(
            name='SlideEvent',
        ),
    ]