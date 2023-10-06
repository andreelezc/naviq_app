from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import QualityProfile, Criterion, Property, Application, AnswerOption, Evaluation
from .forms import QualityProfileForm, CriterionForm, PropertyForm, ApplicationForm, AnswerOptionForm, EvaluationForm


# Home
def homepage(request):
    return render(request, 'base.html')


# Vistas para Quality Profile
class QualityProfileCreateView(CreateView):
    model = QualityProfile
    form_class = QualityProfileForm
    template_name = 'quality_profile_form.html'
    success_url = reverse_lazy('quality_profile_list')  # Redigir a la lista de perfiles de calidad


class QualityProfileListView(ListView):
    model = QualityProfile
    template_name = 'quality_profile_list.html'
    context_object_name = 'qualityprofiles'  # Nombre de la variable en la plantilla.


class QualityProfileUpdateView(UpdateView):
    model = QualityProfile
    form_class = QualityProfileForm
    template_name = 'quality_profile_form.html'
    success_url = reverse_lazy('quality_profile_list')


class QualityProfileDeleteView(DeleteView):
    model = QualityProfile
    template_name = 'quality_profile_confirm_delete.html'
    success_url = reverse_lazy('quality_profile_list')


# Vistas para Criterion
class CriterionCreateView(CreateView):
    model = Criterion
    form_class = CriterionForm
    template_name = 'criterion_form.html'
    success_url = reverse_lazy('criterion_list')


class CriterionListView(ListView):
    model = Criterion
    template_name = 'criterion_list.html'
    context_object_name = 'criteria'


class CriterionUpdateView(UpdateView):
    model = Criterion
    form_class = CriterionForm
    template_name = 'criterion_form.html'
    success_url = reverse_lazy('criterion_list')


class CriterionDeleteView(DeleteView):
    model = Criterion
    template_name = 'criterion_confirm_delete.html'
    success_url = reverse_lazy('criterion_list')


# Vistas para Property
class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = reverse_lazy('property_list')


class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'


class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property_form.html'
    success_url = reverse_lazy('property_list')


class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'property_confirm_delete.html'
    success_url = reverse_lazy('property_list')


# Vistas para Application
class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')


class ApplicationListView(ListView):
    model = Application
    template_name = 'application_list.html'
    context_object_name = 'applications'


class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')


class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('application_list')


# Vistas para AnswerOption
class AnswerOptionCreateView(CreateView):
    model = AnswerOption
    form_class = AnswerOptionForm
    template_name = 'answer_option_form.html'
    success_url = reverse_lazy('answer_option_list')


class AnswerOptionListView(ListView):
    model = AnswerOption
    template_name = 'answer_option_list.html'
    context_object_name = 'answer_options'


class AnswerOptionUpdateView(UpdateView):
    model = AnswerOption
    form_class = AnswerOptionForm
    template_name = 'answer_option_form.html'
    success_url = reverse_lazy('answer_option_list')


class AnswerOptionDeleteView(DeleteView):
    model = AnswerOption
    template_name = 'answer_option_confirm_delete.html'
    success_url = reverse_lazy('answer_option_list')


# Vistas para Evaluation
class EvaluationCreateView(CreateView):
    model = Evaluation
    form_class = EvaluationForm
    template_name = 'evaluation_form.html'
    success_url = reverse_lazy('evaluation_list')


class EvaluationListView(ListView):
    model = Evaluation
    template_name = 'evaluation_list.html'
    context_object_name = 'evaluations'


class EvaluationUpdateView(UpdateView):
    model = Evaluation
    form_class = EvaluationForm
    template_name = 'evaluation_form.html'
    success_url = reverse_lazy('evaluation_list')


class EvaluationDeleteView(DeleteView):
    model = Evaluation
    template_name = 'evaluation_confirm_delete.html'
    success_url = reverse_lazy('evaluation_list')
