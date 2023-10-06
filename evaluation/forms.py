from django import forms
from .models import QualityProfile, Criterion, Property, Application, AnswerOption, Evaluation, User


# Formulario para QualityProfile
class QualityProfileForm(forms.ModelForm):
    class Meta:
        model = QualityProfile
        fields = ['name', 'description', 'custom', 'criteria']

    # Para personalizar cómo se presentan ciertos campos,
    # especificar el widget y otros atributos.
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del perfil'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4})
    )
    custom = forms.BooleanField(required=False)
    criteria = forms.ModelMultipleChoiceField(
        queryset=Criterion.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


# Formulario para Criterion
class CriterionForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre del criterio'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Peso'}))
    properties = forms.ModelMultipleChoiceField(queryset=Property.objects.all(), widget=forms.CheckboxSelectMultiple,
                                                required=False)

    class Meta:
        model = Criterion
        fields = ['name', 'description', 'weight', 'properties']


# Formulario para Property
class PropertyForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre de la propiedad'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Peso'}))
    applications = forms.ModelMultipleChoiceField(queryset=Application.objects.all(),
                                                  widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Property
        fields = ['name', 'description', 'weight', 'applications']


# Formulario para Application
class ApplicationForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre de la aplicación'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Peso'}))
    response_type = forms.ChoiceField(choices=Application.RESPONSE_TYPE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Application
        fields = ['name', 'description', 'weight', 'response_type']


# Formulario para AnswerOption
class AnswerOptionForm(forms.ModelForm):
    application = forms.ModelChoiceField(queryset=Application.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4}))
    value = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Valor'}))

    class Meta:
        model = AnswerOption
        fields = ['application', 'description', 'value']


# Formulario para Evaluation
class EvaluationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    file = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'URL del archivo'}))
    selected_options = forms.ModelMultipleChoiceField(queryset=AnswerOption.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple)
    quality_profile = forms.ModelChoiceField(queryset=QualityProfile.objects.all())

    class Meta:
        model = Evaluation
        fields = ['user', 'file', 'selected_options', 'quality_profile']
