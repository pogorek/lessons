# Generated by Django 4.0.1 on 2022-02-01 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_listing_bid_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid_current',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
    ]
