# Generated by Django 5.0.3 on 2024-04-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_facturare_pers_fizica_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='denumire_produs',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='pret',
            field=models.FloatField(null=True),
        ),
    ]