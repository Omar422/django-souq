# Generated by Django 3.2.6 on 2021-09-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210901_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prdbestseller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='prdisnew',
            field=models.BooleanField(default=True, verbose_name='New'),
        ),
    ]
