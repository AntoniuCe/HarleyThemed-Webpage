# Generated by Django 5.0.3 on 2024-04-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_motorcycles_engine_capacity_motorcycles_horsepower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycles',
            name='horsepower',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='motorcycles',
            name='value',
            field=models.FloatField(null=True),
        ),
    ]