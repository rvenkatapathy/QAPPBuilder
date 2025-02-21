from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
# NOTE: Sections A9 and A10 are static/readonly with boilerplate
from qapp_builder.models import SectionA1, SectionA2, SectionA3, SectionA4, \
    SectionA5, SectionA6, SectionA7, SectionA8, SectionA11, SectionA12
import qapp_builder.forms.section_a_forms as forms


class SectionTemplateView(LoginRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(self.previous_url_name,
                                          kwargs=self.kwargs)
        context['next_url'] = reverse(self.next_url_name,
                                      kwargs=self.kwargs)
        return context


class SectionCreateBase(LoginRequiredMixin, CreateView):
    template_name = 'qapp/sectiona/a_generic_form.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if self.model.objects.filter(qapp_id=self.kwargs['pk']).exists():
            # Redirect to the detail view if the object exists
            return redirect(reverse(self.detail_url_name,
                                    kwargs={'pk': self.kwargs['pk']}))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(self.previous_url_name,
                                          kwargs=self.kwargs)
        return context

    def form_valid(self, form):
        # Set the qapp field based on the URL path/PK
        form.instance.qapp_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(self.next_url_name, kwargs={'pk': self.object.qapp.pk})


class SectionUpdateBase(LoginRequiredMixin, UpdateView):
    template_name = 'qapp/sectiona/a_generic_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(self.previous_url_name,
                                          kwargs=self.kwargs)
        return context

    def get_success_url(self):
        return reverse(self.detail_url_name, kwargs={'pk': self.object.qapp.pk})


class SectionDetailBase(LoginRequiredMixin, DetailView):

    template_name = 'qapp/sectiona/a_generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.section_title
        context['previous_url'] = reverse(self.previous_url_name,
                                          kwargs=self.kwargs)
        context['next_url'] = reverse(self.next_url_name,
                                      kwargs=self.kwargs)
        context['edit_url'] = reverse(self.edit_url_name,
                                      kwargs=self.kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        # Check if the object already exists
        if not self.model.objects.filter(qapp_id=self.kwargs['pk']).exists():
            # Redirect to the desired URL if the object exists
            return redirect(reverse(self.create_url_name,
                                    kwargs={'pk': self.kwargs['pk']}))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        # Explicitly retrieve the object based on qapp_id
        obj = get_object_or_404(self.model, qapp_id=self.kwargs['pk'])
        return obj


class SectionA1Create(SectionCreateBase):

    model = SectionA1
    form_class = forms.SectionA1Form
    template_name = 'qapp/sectiona/a1_form.html'
    section_title = 'Section A.1'
    previous_url_name = 'qapp_detail'
    detail_url_name = 'sectiona1_detail'
    next_url_name = 'sectiona2_create'


class SectionA1Update(SectionUpdateBase):

    model = SectionA1
    form_class = forms.SectionA1Form
    template_name = 'qapp/sectiona/a1_form.html'
    section_title = 'Section A.1'
    previous_url_name = 'qapp_detail'
    detail_url_name = 'sectiona1_detail'
    next_url_name = 'sectiona2_create'


class SectionA1Detail(SectionDetailBase):

    model = SectionA1
    section_title = 'Section A.1'
    edit_url_name = 'sectiona1_edit'
    create_url_name = 'sectiona1_create'
    previous_url_name = 'qapp_detail'
    next_url_name = 'sectiona2_detail'


class SectionA2Create(SectionCreateBase):

    model = SectionA2
    form_class = forms.SectionA2Form
    section_title = 'Section A.2'
    previous_url_name = 'sectiona1_detail'
    detail_url_name = 'sectiona2_detail'
    next_url_name = 'sectiona3_create'


class SectionA2Update(SectionUpdateBase):

    model = SectionA2
    form_class = forms.SectionA2Form
    template_name = 'qapp/sectiona/a2_form.html'
    section_title = 'Section A.2'
    previous_url_name = 'sectiona1_detail'
    detail_url_name = 'sectiona2_detail'
    next_url_name = 'sectiona3_create'


class SectionA2Detail(SectionDetailBase):

    model = SectionA2
    section_title = 'Section A.2'
    edit_url_name = 'sectiona2_edit'
    create_url_name = 'sectiona2_create'
    previous_url_name = 'sectiona1_detail'
    next_url_name = 'sectiona3_detail'


class SectionA3Create(SectionCreateBase):
    model = SectionA3
    form_class = forms.SectionA3Form
    section_title = 'Section A.3'
    previous_url_name = 'sectiona2_detail'
    detail_url_name = 'sectiona3_detail'
    next_url_name = 'sectiona4_create'


class SectionA3Update(SectionUpdateBase):
    model = SectionA3
    form_class = forms.SectionA3Form
    template_name = 'qapp/sectiona/a3_form.html'
    section_title = 'Section A.3'
    previous_url_name = 'sectiona2_detail'
    detail_url_name = 'sectiona3_detail'
    next_url_name = 'sectiona4_create'


class SectionA3Detail(SectionDetailBase):
    model = SectionA3
    section_title = 'Section A.3'
    edit_url_name = 'sectiona3_edit'
    create_url_name = 'sectiona3_create'
    previous_url_name = 'sectiona2_detail'
    next_url_name = 'sectiona4_detail'


class SectionA4Create(SectionCreateBase):
    model = SectionA4
    form_class = forms.SectionA4Form
    section_title = 'Section A.4'
    previous_url_name = 'sectiona3_detail'
    detail_url_name = 'sectiona4_detail'
    next_url_name = 'sectiona5_create'


class SectionA4Update(SectionUpdateBase):
    model = SectionA4
    form_class = forms.SectionA4Form
    template_name = 'qapp/sectiona/a4_form.html'
    section_title = 'Section A.4'
    previous_url_name = 'sectiona3_detail'
    detail_url_name = 'sectiona4_detail'
    next_url_name = 'sectiona5_create'


class SectionA4Detail(SectionDetailBase):
    model = SectionA4
    section_title = 'Section A.4'
    edit_url_name = 'sectiona4_edit'
    create_url_name = 'sectiona4_create'
    previous_url_name = 'sectiona3_detail'
    next_url_name = 'sectiona5_detail'


class SectionA5Create(SectionCreateBase):
    model = SectionA5
    form_class = forms.SectionA5Form
    section_title = 'Section A.5'
    previous_url_name = 'sectiona4_detail'
    detail_url_name = 'sectiona5_detail'
    next_url_name = 'sectiona6_create'


class SectionA5Update(SectionUpdateBase):
    model = SectionA5
    form_class = forms.SectionA5Form
    template_name = 'qapp/sectiona/a5_form.html'
    section_title = 'Section A.5'
    previous_url_name = 'sectiona4_detail'
    detail_url_name = 'sectiona5_detail'
    next_url_name = 'sectiona6_create'


class SectionA5Detail(SectionDetailBase):
    model = SectionA5
    section_title = 'Section A.5'
    edit_url_name = 'sectiona5_edit'
    create_url_name = 'sectiona5_create'
    previous_url_name = 'sectiona4_detail'
    next_url_name = 'sectiona6_detail'


class SectionA6Create(SectionCreateBase):
    model = SectionA6
    form_class = forms.SectionA6Form
    section_title = 'Section A.6'
    previous_url_name = 'sectiona5_detail'
    detail_url_name = 'sectiona6_detail'
    next_url_name = 'sectiona7_create'


class SectionA6Update(SectionUpdateBase):
    model = SectionA6
    form_class = forms.SectionA6Form
    template_name = 'qapp/sectiona/a6_form.html'
    section_title = 'Section A.6'
    previous_url_name = 'sectiona5_detail'
    detail_url_name = 'sectiona6_detail'
    next_url_name = 'sectiona7_create'


class SectionA6Detail(SectionDetailBase):
    model = SectionA6
    section_title = 'Section A.6'
    edit_url_name = 'sectiona6_edit'
    create_url_name = 'sectiona6_create'
    previous_url_name = 'sectiona5_detail'
    next_url_name = 'sectiona7_detail'


class SectionA7Create(SectionCreateBase):
    model = SectionA7
    form_class = forms.SectionA7Form
    section_title = 'Section A.7'
    previous_url_name = 'sectiona6_detail'
    detail_url_name = 'sectiona7_detail'
    next_url_name = 'sectiona8_create'


class SectionA7Update(SectionUpdateBase):
    model = SectionA7
    form_class = forms.SectionA7Form
    template_name = 'qapp/sectiona/a7_form.html'
    section_title = 'Section A.7'
    previous_url_name = 'sectiona6_detail'
    detail_url_name = 'sectiona7_detail'
    next_url_name = 'sectiona8_create'


class SectionA7Detail(SectionDetailBase):
    model = SectionA7
    section_title = 'Section A.7'
    edit_url_name = 'sectiona7_edit'
    create_url_name = 'sectiona7_create'
    previous_url_name = 'sectiona6_detail'
    next_url_name = 'sectiona8_detail'


class SectionA8Create(SectionCreateBase):
    model = SectionA8
    form_class = forms.SectionA8Form
    section_title = 'Section A.8'
    previous_url_name = 'sectiona7_detail'
    detail_url_name = 'sectiona8_detail'
    next_url_name = 'sectiona9_detail'


class SectionA8Update(SectionUpdateBase):
    model = SectionA8
    form_class = forms.SectionA8Form
    template_name = 'qapp/sectiona/a8_form.html'
    section_title = 'Section A.8'
    previous_url_name = 'sectiona7_detail'
    detail_url_name = 'sectiona8_detail'
    next_url_name = 'sectiona9_detail'


class SectionA8Detail(SectionDetailBase):
    model = SectionA8
    section_title = 'Section A.8'
    edit_url_name = 'sectiona8_edit'
    create_url_name = 'sectiona8_create'
    previous_url_name = 'sectiona7_detail'
    next_url_name = 'sectiona9_detail'


# NOTE: Section A9 is readonly/boilerplate

class SectionA9Detail(SectionTemplateView):
    section_title = 'Section A.9'
    previous_url_name = 'sectiona8_detail'
    next_url_name = 'sectiona10_detail'


class SectionA10Detail(SectionTemplateView):
    section_title = 'Section A.10'
    previous_url_name = 'sectiona9_detail'
    next_url_name = 'sectiona11_detail'


class SectionA11Create(SectionCreateBase):
    model = SectionA11
    form_class = forms.SectionA11Form
    section_title = 'Section A.11'
    previous_url_name = 'sectiona10_detail'
    detail_url_name = 'sectiona11_detail'
    next_url_name = 'sectiona12_create'


class SectionA11Update(SectionUpdateBase):
    model = SectionA11
    form_class = forms.SectionA11Form
    template_name = 'qapp/sectiona/a11_form.html'
    section_title = 'Section A.11'
    previous_url_name = 'sectiona10_detail'
    detail_url_name = 'sectiona11_detail'
    next_url_name = 'sectiona12_create'


class SectionA11Detail(SectionDetailBase):
    model = SectionA11
    section_title = 'Section A.11'
    edit_url_name = 'sectiona11_edit'
    create_url_name = 'sectiona11_create'
    previous_url_name = 'sectiona10_detail'
    next_url_name = 'sectiona12_detail'


class SectionA12Create(SectionCreateBase):
    model = SectionA12
    form_class = forms.SectionA12Form
    section_title = 'Section A.12'
    previous_url_name = 'sectiona11_detail'
    detail_url_name = 'sectiona12_detail'
    next_url_name = 'qapp_complete'  # Assuming this is the final section


class SectionA12Update(SectionUpdateBase):
    model = SectionA12
    form_class = forms.SectionA12Form
    template_name = 'qapp/sectiona/a12_form.html'
    section_title = 'Section A.12'
    previous_url_name = 'sectiona11_detail'
    detail_url_name = 'sectiona12_detail'
    next_url_name = 'qapp_complete'  # Assuming this is the final section


class SectionA12Detail(SectionDetailBase):
    model = SectionA12
    section_title = 'Section A.12'
    edit_url_name = 'sectiona12_edit'
    create_url_name = 'sectiona12_create'
    previous_url_name = 'sectiona11_detail'
    next_url_name = 'qapp_complete'  # Assuming this is the final section
