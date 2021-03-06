# Generated by Django 3.0.4 on 2020-04-27 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='restaurant_restaurant_id',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_account_account_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order_list',
            old_name='food_food_id',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='order_list',
            old_name='order_order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='owner_account_account_id',
            new_name='owner',
        ),
    ]
