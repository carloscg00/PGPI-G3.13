# Generated by Django 3.2.12 on 2022-12-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]