# Generated by Django 5.0.2 on 2024-10-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0004_rename_product_stock_product_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10),
        ),
    ]
