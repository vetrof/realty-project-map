# Generated by Django 4.2.5 on 2023-09-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_realty_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='latitude',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='realty',
            name='longitude',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
