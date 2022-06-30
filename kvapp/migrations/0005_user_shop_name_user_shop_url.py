# Generated by Django 4.0.5 on 2022-06-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvapp', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shop_name',
            field=models.CharField(default='#', max_length=225),
        ),
        migrations.AddField(
            model_name='user',
            name='shop_url',
            field=models.URLField(default='#', max_length=1000),
        ),
    ]
