# Generated by Django 2.1.7 on 2019-04-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0004_auto_20190430_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='transaction_id',
            field=models.CharField(default='ADD1FCED4659', max_length=14, null=True),
        ),
    ]
