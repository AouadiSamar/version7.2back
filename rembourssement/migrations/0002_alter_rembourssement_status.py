# Generated by Django 4.2.7 on 2024-04-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rembourssement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rembourssement',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('sent_to_merchant', 'Sent to Merchant'), ('processing_by_SMT', 'Processing by SMT'), ('processing_by_bank', 'Processing by Bank'), ('won', 'Won'), ('lost', 'Lost'), ('cancelled', 'Cancelled'), ('reactivate', 'Reactivate')], max_length=100, null=True, verbose_name='Status'),
        ),
    ]
