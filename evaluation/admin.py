from django.contrib import admin
from .models import QualityProfile, Criterion, Property, Application, AnswerOption, Evaluation

# Register your models here.
admin.site.register(QualityProfile)
admin.site.register(Criterion)
admin.site.register(Property)
admin.site.register(Application)
admin.site.register(AnswerOption)
admin.site.register(Evaluation)
