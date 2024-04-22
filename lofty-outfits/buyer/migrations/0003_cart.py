# Generated by Django 5.0.3 on 2024-04-19 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_customersmodel_is_added_address'),
        ('buyer', '0002_contactusmodel_status'),
        ('seller', '0002_remove_productsmodel_id_productsmodel_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customersmodel')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.productsmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
