"""
URL configuration for naviq_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from evaluation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="base"),
    path('qualityprofile/create/', QualityProfileCreateView.as_view(), name='quality_profile_create'),
    path('qualityprofile/', QualityProfileListView.as_view(), name='quality_profile_list'),
    path('qualityprofile/<int:pk>/edit/', QualityProfileUpdateView.as_view(), name='quality_profile_edit'),
    path('qualityprofile/<int:pk>/delete/', QualityProfileDeleteView.as_view(), name='quality_profile_delete'),
    path('criterion/create/', CriterionCreateView.as_view(), name='criterion_create'),
    path('criterion/', CriterionListView.as_view(), name='criterion_list'),
    path('criterion/<int:pk>/edit/', CriterionUpdateView.as_view(), name='criterion_edit'),
    path('criterion/<int:pk>/delete/', CriterionDeleteView.as_view(), name='criterion_delete'),
    path('property/create/', PropertyCreateView.as_view(), name='property_create'),
    path('property/', PropertyListView.as_view(), name='property_list'),
    path('property/<int:pk>/edit/', PropertyUpdateView.as_view(), name='property_edit'),
    path('property/<int:pk>/delete/', PropertyDeleteView.as_view(), name='property_delete'),
    path('application/create/', ApplicationCreateView.as_view(), name='application_create'),
    path('application/', ApplicationListView.as_view(), name='application_list'),
    path('application/<int:pk>/edit/', ApplicationUpdateView.as_view(), name='application_edit'),
    path('application/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
    path('answer_option/create/', AnswerOptionCreateView.as_view(), name='answer_option_create'),
    path('answer_option/', AnswerOptionListView.as_view(), name='answer_option_list'),
    path('answer_option/<int:pk>/edit/', AnswerOptionUpdateView.as_view(), name='answer_option_edit'),
    path('answer_option/<int:pk>/delete/', AnswerOptionDeleteView.as_view(), name='answer_option_delete'),
    path('evaluation/create/', EvaluationCreateView.as_view(), name='evaluation_create'),
    path('evaluation/', EvaluationListView.as_view(), name='evaluation_list'),
    path('evaluation/<int:pk>/edit/', EvaluationUpdateView.as_view(), name='evaluation_edit'),
    path('evaluation/<int:pk>/delete/', EvaluationDeleteView.as_view(), name='evaluation_delete'),

]
