# Generated by Django 4.2.1 on 2023-06-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customer_date_of_birth_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='employeeassistant',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='technician',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
