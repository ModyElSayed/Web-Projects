# Generated by Django 4.0.1 on 2022-04-05 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_listingcomments_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingcomments',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.auctionlistings'),
        ),
    ]
