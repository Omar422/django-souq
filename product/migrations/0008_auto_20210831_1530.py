# Generated by Django 3.2.6 on 2021-08-31 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20210831_1530'),
        ('product', '0007_auto_20210830_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prdbrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='prdcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category'),
        ),
    ]