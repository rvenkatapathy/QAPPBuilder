# Generated by Django 4.1.7 on 2023-03-02 19:50

import constants.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

  table = 'qapp_builder_sectionbtype'
  old = 'Animal Subjects'
  new = 'Animal Cell Studies'
  remove = [
    'Cell Culture Models',
    'Model Development'
  ]
  add = 'Social Science/Qualitative Studies'

  dependencies = [
    migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ('qapp_builder',
     '0007_sectionb_b2_10_sectionb_b2_9_sectionb_b4_6_and_more'),
  ]

  operations = [
    migrations.RunSQL(
      sql=[(f"UPDATE {table} set name='{new}' where name='{old}';")],
      reverse_sql=[(f"UPDATE {table} set name='{old}' where name='{new}';")]
    ),
    migrations.RunSQL(
      sql=[(f"DELETE FROM {table} where name='{remove[0]}';")],
      reverse_sql=[(f"INSERT INTO {table} (name) VALUES ('{remove[0]}')")]
    ),
    migrations.RunSQL(
      sql=[(f"DELETE FROM {table} where name='{remove[1]}';")],
      reverse_sql=[(f"INSERT INTO {table} (name) VALUES ('{remove[1]}')")]
    ),
    migrations.RunSQL(
      sql=[(f"INSERT INTO {table} (name) VALUES ('{add}')")],
      reverse_sql=[(f"DELETE FROM {table} where name='{add};'")]
    )
  ]
