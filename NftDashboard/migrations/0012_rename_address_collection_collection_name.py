# Generated by Django 4.1.2 on 2022-10-31 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NftDashboard', '0011_collection_open_sea_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='address',
            new_name='collection_name',
        ),
    ]
