# Generated by Django 5.0.3 on 2024-04-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_motorcycles_horsepower_alter_motorcycles_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_motorcycle'),
        ),
    ]
