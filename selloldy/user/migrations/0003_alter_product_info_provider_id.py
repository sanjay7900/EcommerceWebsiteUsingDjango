# Generated by Django 4.0.2 on 2022-04-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_product_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='provider_id',
            field=models.IntegerField(),
        ),
    ]
