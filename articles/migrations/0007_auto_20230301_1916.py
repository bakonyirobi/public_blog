# Generated by Django 3.2.17 on 2023-03-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20230301_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='director',
            field=models.CharField(default='Undefined', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='protagonist',
            field=models.CharField(default='Undefined', max_length=100),
        ),
    ]
