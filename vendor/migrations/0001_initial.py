# Generated by Django 4.0.5 on 2022-06-30 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_products_per_page', models.IntegerField(default=10)),
                ('street', models.CharField(max_length=500)),
                ('street2', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('show_email_address', models.BooleanField(default=True)),
                ('post_zip_code', models.CharField(max_length=500)),
                ('vendor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_name', models.CharField(max_length=500)),
                ('bank_account_number', models.CharField(max_length=500)),
                ('bank_name', models.CharField(max_length=500)),
                ('bank_address', models.TextField()),
                ('routing_number', models.CharField(max_length=225)),
                ('iban', models.CharField(max_length=225)),
                ('swift_code', models.CharField(max_length=225)),
                ('vendor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]