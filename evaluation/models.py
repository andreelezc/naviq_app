from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Modelo para QualityProfile
class QualityProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    custom = models.BooleanField(default=False)
    criteria = models.ManyToManyField('Criterion', related_name='quality_profiles')

    def create_profile(self, name, description, custom=False, criteria_list=None):
        self.name = name
        self.description = description
        self.custom = custom
        self.save()

        if criteria_list is None:
            criteria_list = []

        # Asociar los criterios proporcionados
        for criterion in criteria_list:
            self.criteria.add(criterion)

    # Permiten la modificación de los criterios asociados a un perfil de calidad ya existente.
    def add_criteria(self, criterion):
        self.criteria.add(criterion)
        self.save()

    def remove_criteria(self, criterion):
        self.criteria.remove(criterion)
        self.save()

    def update_profile(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def list_all_profiles(cls):
        return cls.objects.all()


# Modelo EvaluativeEntity (abstracto)
class EvaluativeEntity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract = True

    def create_entity(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight
        self.save()

    def update_entity(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    def delete_entity(self):
        self.delete()

    @classmethod
    def list_all_entities(cls):
        return cls.objects.all()

    def calculate_score(self, *args, **kwargs):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")


# Modelo Criteria heredando de EvaluativeEntity
class Criterion(EvaluativeEntity):
    # Considerando que una propiedad puede estar asociada a múltiples criterios
    properties = models.ManyToManyField('Property', related_name="criteria")

    def add_property(self, property):
        self.properties.add(property)

    def remove_property(self, property):
        self.properties.remove(property)

    def calculate_score(self):
        total_score = 0
        for property in self.properties.all():
            total_score += property.calculateScore() * property.weight
        return total_score

    class Meta:
        verbose_name_plural = "criteria"


# Modelo Property heredando de EvaluativeEntity
class Property(EvaluativeEntity):
    # No se necesita definir una relación a Criteria ya que ya está definida en Criteria.
    # Si se desea acceder a los criterios asociados desde una propiedad, usar el related_name "criterias".
    applications = models.ManyToManyField('Application', related_name="properties")

    def add_application(self, application):
        self.applications.add(application)

    def remove_application(self, application):
        self.applications.remove(application)

    def calculate_score(self):
        total_score = 0
        for application in self.applications.all():
            total_score += application.calculateScore() * application.weight
        return total_score

    class Meta:
        verbose_name_plural = 'properties'


# Modelo Application heredando de EvaluativeEntity
class Application(EvaluativeEntity):
    RESPONSE_TYPE_CHOICES = [
        ('single', 'Single Choice'),
        ('multiple', 'Multiple Choice'),
    ]

    response_type = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPE_CHOICES,
        default='single',
        help_text="Tipo de respuesta: única o múltiple."
    )

    def calculate_score(self, selected_options):
        total_value = sum((option.get_value() or 0) for option in selected_options if option.application == self)
        return total_value * self.weight


# Modelo para AnswerOption
class AnswerOption(models.Model):
    application = models.ForeignKey(Application, related_name='answer_options', on_delete=models.CASCADE)
    description = models.TextField()
    value = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def get_value(self):
        return self.value


# Modelo para Evaluation
class Evaluation(models.Model):
    user = models.ForeignKey(User, related_name='evaluations', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    result = models.TextField(blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    file = models.URLField(verbose_name="File URL")
    selected_options = models.ManyToManyField(AnswerOption, related_name='evaluations')
    quality_profile = models.ForeignKey(QualityProfile, related_name='evaluations', on_delete=models.PROTECT)

    def create_evaluation(self, file, user, quality_profile):
        self.file = file
        self.user = user
        self.qualityProfile = quality_profile
        self.save()

    def calculate_final_score(self):
        total_score = 0
        for criteria in self.qualityProfile.criterias.all():
            total_score += criteria.calculateScore() * criteria.weight
        self.score = total_score
        self.save()  # Guardamos el resultado en la base de datos
        return total_score
