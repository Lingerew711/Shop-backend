# Generated by Django 3.2.6 on 2021-08-16 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20210816_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='id',
            new_name='wishlist_id',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id', to='company.product'),
        ),
    ]