# Generated by Django 5.1.1 on 2024-10-01 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0003_rename_product_fk_stock_product_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='product',
            new_name='product_fk',
        ),
    ]
