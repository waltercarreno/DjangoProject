# Generated by Django 4.0.1 on 2022-02-15 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
