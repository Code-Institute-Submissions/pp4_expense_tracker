# Generated by Django 5.0.4 on 2024-04-29 14:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0005_alter_wallet_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.CharField(default='default wallet', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='wallet',
            unique_together={('user', 'name')},
        ),
    ]