# Generated by Django 5.0.4 on 2024-05-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0003_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='image',
            field=models.ImageField(blank=True, upload_to='admin_module/images'),
        ),
    ]