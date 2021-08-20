# Generated by Django 3.2.6 on 2021-08-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20210820_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='wishlist_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='company.product'),
        ),
    ]