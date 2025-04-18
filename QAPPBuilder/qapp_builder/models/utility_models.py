from django.db import models
from django.utils.safestring import mark_safe
from simple_history.models import HistoricalRecords

IGNORE_FIELDS_PROGRESS = ['id']


class EpaBaseModel(models.Model):
    """Abstract class to be inherited by all EPA/QAPP Models."""

    history = HistoricalRecords(inherit=True)

    def render_details(self):
        return render_model_details(self)

    def get_progress(self):
        total_fields = 0
        empty_fields = 0
        for field in self._meta.get_fields():
            if (
                isinstance(field,
                           (models.ForeignKey, models.OneToOneField,
                            models.ManyToManyRel, models.ManyToOneRel,
                            models.AutoField)) or
                field.name in IGNORE_FIELDS_PROGRESS or
                getattr(field, 'null', True) or getattr(field, 'blank', True)
            ):
                continue

            total_fields += 1
            value = getattr(self, field.name, None)
            if value in [None, '', []]:  # Check for empty or null values
                empty_fields += 1

        if total_fields == 0:
            return 0  # Avoid division by zero

        progress = (total_fields - empty_fields) / total_fields * 100
        return progress

    class Meta:
        abstract = True


class Definition(EpaBaseModel):
    """Represents a Definition for an Acronym, Abbreviation, or Term"""

    acronym_abbrev = models.TextField(blank=False, null=False)
    definition = models.TextField(blank=False, null=False)


class Participant(EpaBaseModel):
    """Represents an entry in the distribution list (TODO what section?)"""

    name_and_org = models.TextField()
    email = models.TextField()
    roles = models.TextField()
    responsibilities = models.TextField()


class QappDocument(EpaBaseModel):
    """
    Represents a Document or Record. SectionA12 will contain a table
    (i.e. many-to-many relationship) of documents/records.
    """
    record_type = models.TextField()
    responsible_party = models.TextField()
    location_proj_file = models.TextField()
    file_format = models.TextField()
    # TODO: Special handling should be Y or N
    special_handling = models.TextField()


def render_field(label, value):
    extra_class = 'long-text'
    if len(str(value)) > 100:
        extra_class = 'long-text-12'
    return f'''
    <div class="usa-form-group">
        <label class="usa-label">{label}</label>
        <div class="usa-input {extra_class}">{value}</div>
    </div>
    '''


def get_model_custom_label(instance, field_name):
    # NOTE: Custom code for handling labels in the model rendering
    if hasattr(instance, 'labels') and field_name in instance.labels:
        return instance.labels[field_name]


def render_model_details(instance):
    """
    Returns the details of a model instance with USWDS styling.
    """
    output = []
    for field in instance._meta.fields:
        value = getattr(instance, field.name)
        if field.many_to_many:
            value = ', '.join([str(obj) for obj in value.all()])
        # TODO Figure out datetime formatting...
        # elif isinstance(value, (models.DateField, models.DateTimeField)):
        #     value = date_format(value, DATETIME_FORMAT)
        field_label = get_model_custom_label(instance, field.name)
        if not field_label:
            field_label = field.verbose_name.capitalize()
        output.append(render_field(field_label, value))
    return mark_safe('\n'.join(output))
