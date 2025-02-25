# Generated by Django 5.1.5 on 2025-02-25 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qapp_builder', '0011_sectiona10'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentrecord',
            name='section_a12',
        ),
        migrations.AddField(
            model_name='documentrecord',
            name='qapp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp'),
            preserve_default=False,
        ),
    ]
