# Generated by Django 5.0.7 on 2024-07-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "account_transfare_app",
            "0002_accounts_created_at_accounts_updated_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounts",
            name="id",
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
