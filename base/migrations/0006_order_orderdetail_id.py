# Generated by Django 4.0.6 on 2022-08-16 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_category_order_orderdetail_product_remove_loan_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderDetail_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.orderdetail'),
        ),
    ]
