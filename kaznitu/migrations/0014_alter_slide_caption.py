# Generated by Django 5.0.2 on 2024-03-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaznitu', '0013_slide_delete_slideshowimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='caption',
            field=models.TextField(),
        ),
    ]
