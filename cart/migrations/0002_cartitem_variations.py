# Generated by Django 4.2.5 on 2023-09-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variationmanager'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
