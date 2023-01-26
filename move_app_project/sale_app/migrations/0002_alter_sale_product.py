# Generated by Django 4.1.5 on 2023-01-26 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
        ('sale_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_app.product'),
        ),
    ]
