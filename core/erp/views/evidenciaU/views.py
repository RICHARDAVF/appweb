from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.core.files.storage import default_storage
from core.erp.forms import FormEvidenciaU
from core.erp.models import EvidenciaUnica
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os
class CreateViewEvidenciaU(CreateView):
    model = EvidenciaUnica
    form_class = FormEvidenciaU
    template_name = 'evidenciaU/create.html'
    success_url = reverse_lazy('erp:eu_list')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "Evidencia Unica"
        context['entidad'] = 'Evidencias'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context
    def post(self, request, *args, **kwargs) :
        data = {}
        try:
            action =request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No se a ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)
class ListViewEvidenciaU(ListView):
    model = EvidenciaUnica
    template_name = 'evidenciaU/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for index,value in enumerate(EvidenciaUnica.objects.filter(usuario_id=self.request.user.id)):
                    item = value.toJSON()
                    item['position'] = index
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
  
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Lista de Evidencias Unicas'
        context['create_url'] = reverse_lazy('erp:eu_create')
        context['list_url'] = reverse_lazy('erp:eu_list')
        context['entidad'] = 'Evidencia Unica'
        return context
class UpdateViewEvidenciaU(UpdateView):
    model = EvidenciaUnica
    form_class = FormEvidenciaU
    template_name = 'evidenciaU/create.html'
    success_url = reverse_lazy('erp:eu_list')
   
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Evidencia Unica'
        context['entidad'] = 'Evidencias'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewEvidenciaU(DeleteView):
    model = EvidenciaUnica
    template_name = 'evidenciaA/delete.html'
    success_url = reverse_lazy('erp:eu_list')
    url_redirect = success_url

    def delete_files(self):
        fields = ['propuesta', 'desvinculacion']
        for field in fields:
            file = getattr(self.object, field)
            if file and default_storage.exists(file.name):
                default_storage.delete(file.name)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.delete_files()
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Evidencia Unica'
        context['entidad'] = 'Evidencias'
        context['list_url'] = self.success_url
        return context