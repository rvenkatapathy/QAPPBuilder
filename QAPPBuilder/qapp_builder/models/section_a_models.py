from django.db import models
from .qapp_models import Qapp
from .utility_models import EpaBaseModel
from constants.qapp_section_b_const import DISCIPLINE_CHOICES, \
    DISCIPLINE_MAX_LEN


class Discipline(EpaBaseModel):

    name = models.CharField(
        blank=False, null=False, max_length=DISCIPLINE_MAX_LEN,
        choices=DISCIPLINE_CHOICES)


class SectionA1(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a1')
    ord_center = models.TextField(blank=False, null=False)
    division = models.TextField(blank=False, null=False)
    branch = models.TextField(blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    ord_national_program = models.TextField(blank=False, null=False)
    version_date = models.DateField(blank=False, null=False)
    proj_qapp_id = models.TextField(blank=False, null=False)
    qa_category = models.CharField(blank=False, null=False, max_length=1)
    # Intramurally or Extramurally
    intra_or_extra = models.CharField(blank=False, null=False, max_length=12)
    # If extramurally:
    vehicle_num = models.TextField(blank=True, null=True)
    non_epa_org = models.TextField(blank=True, null=True)
    period_performance = models.TextField(blank=True, null=True)
    # Accessibility is "I do NOT want this QAPP internally shared and
    #                   accessible on the ORD intranet site."
    accessibility = models.BooleanField(default=False)
    disciplines = models.ManyToManyField(Discipline)
    # TODO: Measurement and Monitoring splits in two sub-options:
    #       Analytical Methods Development
    #       Animal/Cell Culture Studies
    # TODO: The CESER template has an "Other" option with user defined name...


class AdditionalSignature(EpaBaseModel):

    title = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)


class SectionA2(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a2')
    # Required Signatures:
    ord_technical_lead = models.TextField(blank=False, null=False)
    ord_tl_supervisor = models.TextField(blank=False, null=False)
    ord_qa_manager = models.TextField(blank=False, null=False)
    # Extramural signatures:
    extramural_technical_manager = models.TextField(blank=True, null=True)
    extramural_qa_manager = models.TextField(blank=True, null=True)
    # Optional additional signatures:
    additional_signatures = models.ManyToManyField(AdditionalSignature)


class SectionA3(EpaBaseModel):
    """A3: Table of Contents, Document Format, and Document Control"""

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a3')
    # Revisions one-to-many
    # Acronyms/Abbreviations/Definitions one-to-many


class Revision(EpaBaseModel):

    section_a3 = models.ForeignKey(SectionA3, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    qapp_id = models.TextField(blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)


class AcronymAbbreviation(EpaBaseModel):

    section_a3 = models.ForeignKey(SectionA3, on_delete=models.CASCADE)
    acronym_abbreviation = models.TextField(blank=False, null=False)
    definition = models.TextField(blank=False, null=False)


class SectionA4(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a4')
    project_background = models.TextField(blank=False, null=False)
    project_purpose = models.TextField(blank=False, null=False)


class SectionA5(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a5')
    tasks_summary = models.TextField(blank=False, null=False)
    # Table 1. Project Completion Timeline
    start_fy = models.CharField(blank=True, null=True, max_length=4)
    start_q = models.CharField(blank=True, null=True, max_length=2)


class Task(EpaBaseModel):

    section_a5 = models.ForeignKey(SectionA5, on_delete=models.CASCADE)
    tasks_desc = models.TextField(blank=False, null=False)
    fy_q_0 = models.TextField(blank=True, null=True)
    fy_q_1 = models.TextField(blank=True, null=True)
    fy_q_2 = models.TextField(blank=True, null=True)
    fy_q_3 = models.TextField(blank=True, null=True)
    fy_q_4 = models.TextField(blank=True, null=True)
    fy_q_5 = models.TextField(blank=True, null=True)
    fy_q_6 = models.TextField(blank=True, null=True)
    fy_q_7 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tasks_desc


class SectionA6(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a6')
    information = models.TextField(blank=False, null=False)


class SectionA7(EpaBaseModel):
    """Distribution List"""

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a7')
    # Table 2. Distribution List
    # TODO: When this section is saved, populate some of the table defaults


class Distribution(EpaBaseModel):

    section_a7 = models.ForeignKey(SectionA7, on_delete=models.CASCADE)
    name_and_org = models.TextField(blank=False, null=False)
    email = models.TextField(blank=False, null=False)
    proj_role = models.TextField(blank=False, null=False)


class SectionA8(EpaBaseModel):
    """Project Organization"""

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a8')
    # Table 3. Environmental Information Roles and Responsibilities
    # TODO: When this section is saved, populate some of the table defaults


class RoleResponsibility(EpaBaseModel):

    section_a8 = models.ForeignKey(SectionA8, on_delete=models.CASCADE)
    name_and_org = models.TextField(blank=False, null=False)
    proj_role = models.TextField(blank=False, null=False)
    proj_responsibilities = models.TextField(blank=False, null=False)


# SectionA9 is static content, no input.

# SectionA10 is an optional(?) org chart


class SectionA11(EpaBaseModel):

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a11')
    information = models.TextField(blank=False, null=False)


class SectionA12(EpaBaseModel):
    """Documents and Records"""

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, related_name='section_a12')
    # Table 4. Documents and Records
    # TODO: When this section is saved, populate some of the table defaults
    # Table 5. Project's Record Schedule
    # Table 5 is static depending on QA Cat (A or B), I think?


class DocumentRecord(EpaBaseModel):

    section_a12 = models.ForeignKey(SectionA12, on_delete=models.CASCADE)
    record_type = models.TextField(blank=False, null=False)
    responsible_party = models.TextField(blank=False, null=False)
    in_proj_file = models.TextField(blank=False, null=False)
    file_type = models.TextField(blank=False, null=False)
    special_handling = models.BooleanField(default=False)
