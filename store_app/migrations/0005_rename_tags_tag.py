# Generated by Django 5.0.6 on 2024-08-01 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_rename_images_product_image_images_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]