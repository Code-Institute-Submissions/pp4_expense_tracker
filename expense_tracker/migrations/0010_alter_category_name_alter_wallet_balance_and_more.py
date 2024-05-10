# Generated by Django 5.0.6 on 2024-05-10 19:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0009_alter_transaction_amount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='The unique name of the category.', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='The initial balance of the wallet.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.CharField(default='your bank account', help_text='The name of the wallet.', max_length=100),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(help_text='The user to whom the wallet belongs.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
