# Generated by Django 4.0.2 on 2022-03-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterDeliveryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Register Delivery Users',
            },
        ),
    ]
