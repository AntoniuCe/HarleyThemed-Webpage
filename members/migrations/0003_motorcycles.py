# Generated by Django 5.0.3 on 2024-04-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe_of_motorcycle', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('is_available', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]