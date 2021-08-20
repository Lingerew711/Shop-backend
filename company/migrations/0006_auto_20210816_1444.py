# Generated by Django 3.2.6 on 2021-08-16 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20210815_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='product_name',
            field=models.ManyToManyField(to='company.Product'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='company.product'),
        ),
    ]
