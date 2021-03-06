# Generated by Django 4.0.5 on 2022-07-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_brand_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_reviews',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='visibility',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
