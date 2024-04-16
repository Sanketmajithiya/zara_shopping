# Generated by Django 5.0.3 on 2024-04-15 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_customersmodel_is_activate'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customersmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
