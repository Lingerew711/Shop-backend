# Generated by Django 3.2.6 on 2021-08-15 19:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.TextField()),
                ('product_name', models.TextField()),
                ('date', models.DateField(default=datetime.datetime.utcnow)),
                ('description', models.TextField()),
                ('category', models.TextField()),
                ('price', models.FloatField()),
                ('condition', models.TextField()),
                ('delivery_available', models.BooleanField(default=False)),
                ('discount', models.TextField(default=0.0)),
                ('product_count', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime.utcnow)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='company.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_city',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_title',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
