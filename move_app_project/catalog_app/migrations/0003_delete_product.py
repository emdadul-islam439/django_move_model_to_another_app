# Generated by Django 4.1.5 on 2023-01-26 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_remove_product_category'),
        ('sale_app', '0002_alter_sale_product'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Product',
                ),
            ],
            database_operations=[]
        )
    ]
