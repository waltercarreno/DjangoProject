# Generated by Django 4.0.1 on 2022-02-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
    ]
