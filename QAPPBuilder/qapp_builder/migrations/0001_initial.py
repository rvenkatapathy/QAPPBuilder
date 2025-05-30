# Generated by Django 5.1.5 on 2025-02-28 15:35

import constants.utils
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym_abbrev', models.TextField()),
                ('definition', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Measurement and Monitoring', 'Measurement and Monitoring'), ('Social Sciences', 'Social Sciences'), ('Existing Data', 'Existing Data'), ('Code-Based Modeling', 'Code-Based Modeling'), ('Model Application and Evaluation', 'Model Application and Evaluation'), ('Software and Application Development', 'Software and Application Development'), ('Environmental Technology', 'Environmental Technology')], max_length=36)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_org', models.TextField()),
                ('email', models.TextField()),
                ('roles', models.TextField()),
                ('responsibilities', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QappDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.TextField()),
                ('responsible_party', models.TextField()),
                ('location_proj_file', models.TextField()),
                ('file_format', models.TextField()),
                ('special_handling', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HardwareSoftware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.TextField()),
                ('os', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.TextField()),
                ('responsible_party', models.TextField()),
                ('in_proj_file', models.TextField()),
                ('file_type', models.TextField()),
                ('special_handling', models.BooleanField(default=False)),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('org', models.TextField()),
                ('email', models.TextField()),
                ('proj_role', models.TextField()),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AcronymAbbreviation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym_abbreviation', models.TextField()),
                ('definition', models.TextField()),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QappSharingTeamMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('can_edit', models.BooleanField(default=True)),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qapp_teams2', to='qapp_builder.qapp')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_qapp2', to='teams.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='qapp',
            name='teams',
            field=models.ManyToManyField(through='qapp_builder.QappSharingTeamMap', to='teams.team'),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.TextField()),
                ('description', models.TextField()),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleResponsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('org', models.TextField()),
                ('proj_role', models.TextField()),
                ('proj_responsibilities', models.TextField()),
                ('qapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ord_center', models.CharField(choices=[('Center for Computational Toxicology & Exposure', 'Center for Computational Toxicology & Exposure'), ('Center for Environmental Measurement and Modeling', 'Center for Environmental Measurement and Modeling'), ('Center for Environmental Solutions & Emergency Response', 'Center for Environmental Solutions & Emergency Response'), ('Center for Public Health and Environmental Assessments', 'Center for Public Health and Environmental Assessments'), ('Office of Resource Management', 'Office of Resource Management'), ('Office of Science Advisor, Policy & Engagement', 'Office of Science Advisor, Policy & Engagement')], max_length=55)),
                ('division', models.TextField()),
                ('branch', models.TextField()),
                ('ord_national_program', models.TextField()),
                ('version_date', models.DateField()),
                ('proj_qapp_id', models.TextField()),
                ('qa_category', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('intra_or_extra', models.CharField(choices=[('Intramurally', 'Intramurally'), ('Extramurally', 'Extramurally')], max_length=12)),
                ('vehicle_num', models.TextField(blank=True, null=True)),
                ('non_epa_org', models.TextField(blank=True, null=True)),
                ('period_performance', models.TextField(blank=True, null=True)),
                ('accessibility', models.BooleanField(default=False)),
                ('disciplines', models.ManyToManyField(to='qapp_builder.discipline')),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a1', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_chart', models.FileField(blank=True, null=True, upload_to=constants.utils.get_attachment_storage_path)),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a10', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a11', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ord_technical_lead', models.TextField()),
                ('ord_tl_supervisor', models.TextField()),
                ('ord_qa_manager', models.TextField()),
                ('extramural_technical_manager', models.TextField(blank=True, null=True)),
                ('extramural_qa_manager', models.TextField(blank=True, null=True)),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a2', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdditionalSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('section_a2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.sectiona2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_background', models.TextField()),
                ('project_purpose', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a4', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks_summary', models.TextField()),
                ('start_fy', models.CharField(blank=True, max_length=4, null=True)),
                ('start_q', models.CharField(blank=True, max_length=2, null=True)),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a5', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionA6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a6', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b1', models.TextField()),
                ('b2', models.TextField()),
                ('b3', models.TextField()),
                ('b4', models.TextField()),
                ('b5', models.TextField()),
                ('b6', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_b', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionB7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b71', models.TextField()),
                ('b72', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c2', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_c', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SectionD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.TextField()),
                ('d2', models.TextField()),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_d', to='qapp_builder.qapp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks_desc', models.TextField()),
                ('fy_q_0', models.TextField(blank=True, null=True)),
                ('fy_q_1', models.TextField(blank=True, null=True)),
                ('fy_q_2', models.TextField(blank=True, null=True)),
                ('fy_q_3', models.TextField(blank=True, null=True)),
                ('fy_q_4', models.TextField(blank=True, null=True)),
                ('fy_q_5', models.TextField(blank=True, null=True)),
                ('fy_q_6', models.TextField(blank=True, null=True)),
                ('fy_q_7', models.TextField(blank=True, null=True)),
                ('section_a5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qapp_builder.sectiona5')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
