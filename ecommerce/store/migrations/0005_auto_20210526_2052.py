# Generated by Django 3.2.3 on 2021-05-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210526_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_orderd',
            new_name='date_ordered',
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
