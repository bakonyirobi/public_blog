# Generated by Django 3.2.16 on 2023-03-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20230301_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(default='default-movie.jpg', upload_to=''),
        ),
    ]
