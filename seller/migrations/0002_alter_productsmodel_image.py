# Generated by Django 5.0.3 on 2024-04-10 07:51

import master.utils.LO_UNIQUE.unique_filename
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='image',
            field=models.ImageField(upload_to=master.utils.LO_UNIQUE.unique_filename.genrate_unique_filename),
        ),
    ]
