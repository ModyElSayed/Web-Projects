# Generated by Django 4.0.1 on 2022-04-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_listingcomments_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='final_bid',
            field=models.FloatField(),
        ),
    ]
