# Generated by Django 5.0.6 on 2024-08-08 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
    ]