# Generated by Django 5.1.5 on 2025-03-19 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qapp_builder', '0003_historicalacronymabbreviation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionb7',
            name='qapp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_b7', to='qapp_builder.qapp'),
        ),
    ]
