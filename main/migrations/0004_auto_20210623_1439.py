# Generated by Django 3.1.4 on 2021-06-23 11:39

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210623_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.generate_filename, verbose_name='Изображение'),
        ),
    ]
