# Generated by Django 4.0.2 on 2022-03-23 01:39

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_is_delivered_remove_order_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_location',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=3),
        ),
    ]
