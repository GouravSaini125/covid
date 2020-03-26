from django.urls import path
from . import views

urlpatterns = [

    path('advisory', views.AdvisoryList.as_view()),
    path('advisory/create', views.AdvisoryCreate.as_view()),

    path('awareness', views.AwarenessList.as_view()),
    path('awareness/create', views.AwarenessCreate.as_view()),

    path('govt', views.GovtDataList.as_view()),
    path('govt/create', views.GovtDataCreate.as_view()),

    path('precaution', views.PrecautionList.as_view()),
    path('precaution/create', views.PrecautionCreate.as_view()),

    path('audio/create', views.CoronaAudioCreate.as_view()),

]