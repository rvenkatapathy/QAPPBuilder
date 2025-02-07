# Generated by Django 5.1.5 on 2025-02-07 19:06

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
        ),
        migrations.CreateModel(
            name='VersionControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qapp_id', models.TextField()),
                ('updated_on', models.DateField()),
                ('authors', models.TextField()),
                ('description', models.TextField()),
            ],
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
        ),
        migrations.AddField(
            model_name='qapp',
            name='teams',
            field=models.ManyToManyField(through='qapp_builder.QappSharingTeamMap', to='teams.team'),
        ),
        migrations.CreateModel(
            name='SectionA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a', to='qapp_builder.qapp')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_org_chart', models.ImageField(upload_to='')),
                ('comms_desc', models.TextField()),
                ('comm_procedures', models.TextField()),
                ('non_epa_comms', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a10', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eio_verifier', models.TextField()),
                ('training_documenter', models.TextField()),
                ('spec_training_certs', models.TextField()),
                ('training_eval', models.TextField()),
                ('training_reqs', models.TextField()),
                ('citi_personnel', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a11', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirements', models.TextField()),
                ('record_sched', models.TextField()),
                ('dc_rm_reqs', models.TextField()),
                ('citation', models.TextField()),
                ('docs_records', models.ManyToManyField(to='qapp_builder.qappdocument')),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a12', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epa_op_man', models.TextField()),
                ('epa_qam', models.TextField()),
                ('non_epa_op_man', models.TextField(blank=True, null=True)),
                ('non_epa_qam', models.TextField(blank=True, null=True)),
                ('supervisor', models.TextField(blank=True, null=True)),
                ('pqapp_dir', models.TextField(blank=True, null=True)),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a2', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backgroun_desc', models.TextField()),
                ('existing_sources', models.TextField()),
                ('other_docs', models.TextField()),
                ('eio_purpose', models.TextField()),
                ('env_decisions', models.TextField()),
                ('needed_info', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a4', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('deliverables', models.TextField()),
                ('tasks_and_sched', models.TextField()),
                ('irb_review', models.TextField()),
                ('irb_exception', models.TextField()),
                ('ord_app_inv_entry', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a5', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dqo', models.TextField()),
                ('criteria', models.TextField()),
                ('dqi', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a6', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor', models.TextField()),
                ('distribution_list', models.ManyToManyField(to='qapp_builder.participant')),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a7', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_chart', models.ImageField(upload_to='')),
                ('qam_oversight', models.TextField()),
                ('qam_authority', models.TextField()),
                ('a_team_rep', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a8', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a9', to='qapp_builder.sectiona')),
            ],
        ),
        migrations.CreateModel(
            name='SectionA1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_date', models.DateField()),
                ('conducting_org_name', models.TextField()),
                ('developing_org_name', models.TextField()),
                ('applicability_period', models.TextField()),
                ('doc_control_identifier', models.TextField()),
                ('agreement_num', models.TextField(blank=True, null=True)),
                ('con_to_num', models.TextField(blank=True, null=True)),
                ('ia_num', models.TextField(blank=True, null=True)),
                ('mou_title', models.TextField(blank=True, null=True)),
                ('mou_date', models.DateField(blank=True, null=True)),
                ('reg_req_cit', models.TextField(blank=True, null=True)),
                ('enf_legal_title', models.TextField(blank=True, null=True)),
                ('enf_legal_date', models.DateField(blank=True, null=True)),
                ('ord_qa_cat', models.TextField(blank=True, null=True)),
                ('ord_program', models.TextField(blank=True, null=True)),
                ('definitions', models.ManyToManyField(to='qapp_builder.definition')),
                ('section_a', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_a1', to='qapp_builder.sectiona')),
                ('versions', models.ManyToManyField(to='qapp_builder.versioncontrol')),
            ],
        ),
    ]
