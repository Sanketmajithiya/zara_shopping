# Generated by Django 5.0.4 on 2024-05-01 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_auth_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='p_id',
            field=models.CharField(default=10, max_length=100, primary_key=True, serialize=False),
        ),
    ]