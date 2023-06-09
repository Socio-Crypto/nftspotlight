# Generated by Django 4.1.1 on 2022-10-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NftDashboard', '0003_alter_collection_tx_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='floor_price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='collection',
            name='max_price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='collection',
            name='num_of_holders',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='collection',
            name='num_of_sales',
            field=models.IntegerField(default=None),
        ),
    ]
