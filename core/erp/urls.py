from django.urls import path
from core.erp.views.evidenciaU.views import *
from core.erp.views.empresas.views import *
from core.erp.views.evidenciaA.views import *
from core.erp.views.evidenciaMI.views import *
from core.erp.views.evidenciaMEF.views import *
from core.erp.views.evidenciaMPI.views import *
from core.erp.views.evidenciaMRC.views import *
app_name = 'erp'
urlpatterns = [
    #EMPRESAS
    path('empresa/list/',ListViewEmpresa.as_view(),name='empresa_list'),
    path('empresa/add/',CreateViewEmpresa.as_view(),name='empresa_create'),
    path('empresa/edit/<int:pk>/',UpdateViewEmpresa.as_view(),name='empresa_edit'),
    path('empresa/delete/<int:pk>/',DeleteViewEmpresa.as_view(),name='empresa_delete'),
    #EVIDENCIAS UNICAS
    path('evidenciaU/list/',ListViewEvidenciaU.as_view(),name='eu_list'),
    path('evidenciaU/add/',CreateViewEvidenciaU.as_view(),name='eu_create'),
    path('evidenciaU/edit/<int:pk>/',UpdateViewEvidenciaU.as_view(),name='eu_edit'),
    path('evidenciaU/delete/<int:pk>/',DeleteViewEvidenciaU.as_view(),name='eu_delete'),
    #EVIDENCIAS MENSUALES IMPUESTOS
    path('evidenciaMI/list/',ListViewEvidenciaMI.as_view(),name='emi_list'),
    path('evidenciaMI/add/',CreateViewEvidenciaMI.as_view(),name='emi_create'),
    path('evidenciaMI/edit/<int:pk>/',UpdateViewEvidenciaMI.as_view(),name='emi_edit'),
    path('evidenciaMI/delete/<int:pk>/',DeleteViewEvidenciaMI.as_view(),name='emi_delete'),
    #EVIDENCIAS MENSUALES PRESENTACION DE IMPUESTOS
    path('evidenciaMPI/list/',ListViewEvidenciaMPI.as_view(),name='empi_list'),
    path('evidenciaMPI/add/',CreateViewEvidenciaMPI.as_view(),name='empi_create'),
    path('evidenciaMPI/edit/<int:pk>/',UpdateViewEvidenciaMPI.as_view(),name='empi_edit'),
    path('evidenciaMPI/delete/<int:pk>/',DeleteViewEvidenciaMPI.as_view(),name='empi_delete'),
    #EVIDENCIAS MENSUALES REGISTROS CONTABLES
    path('evidenciaMRC/list/',ListViewEvidenciaMRC.as_view(),name='emrc_list'),
    path('evidenciaMRC/add/',CreateViewEvidenciaMRC.as_view(),name='emrc_create'),
    path('evidenciaMRC/edit/<int:pk>/',UpdateViewEvidenciaMRC.as_view(),name='emrc_edit'),
    path('evidenciaMRC/delete/<int:pk>/',DeleteViewEvidenciaMRC.as_view(),name='emrc_delete'),
    #EVIDENCIAS MENSUALES ESTADOS FINANCIEROS
    path('evidenciaMEF/list/',ListViewEvidenciaMEF.as_view(),name='emef_list'),
    path('evidenciaMEF/add/',CreateViewEvidenciaMEF.as_view(),name='emef_create'),
    path('evidenciaMEF/edit/<int:pk>/',UpdateViewEvidenciaMEF.as_view(),name='emef_edit'),
    path('evidenciaMEF/delete/<int:pk>/',DeleteViewEvidenciaMEF.as_view(),name='emef_delete'),
    #EVIDENCIAS ANUALES
    path('evidenciaA/list/',ListViewEvidenciaA.as_view(),name='ea_list'),
    path('evidenciaA/add/',CreateViewEvidenciaA.as_view(),name='ea_create'),
    path('evidenciaA/edit/<int:pk>/',UpdateViewEvidenciaA.as_view(),name='ea_edit'),
    path('evidenciaA/delete/<int:pk>/',DeleteViewEvidenciaA.as_view(),name='ea_delete'),
]