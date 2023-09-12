from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.core.files.storage import default_storage
from core.erp.forms import FormEvidenciaA
from core.erp.models import EvidenciaAnual
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
class CreateViewEvidenciaA(CreateView):
    model = EvidenciaAnual
    form_class = FormEvidenciaA
    template_name = 'evidenciaA/create.html'
    success_url = reverse_lazy('erp:ea_list')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "Evidencia Anual"
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
class ListViewEvidenciaA(ListView):
    model = EvidenciaAnual
    template_name = 'evidenciaA/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                if self.request.user.is_superuser:
                    for index,value in enumerate(EvidenciaAnual.objects.all()):
                        item = value.toJSON()
                        item['cumplimiento'] = True
                    
                        for val in item.values():
                            if val == '':
                                item['cumplimiento'] = False
                                break
                        data.append(item)
                else:
                    for index,value in enumerate(EvidenciaAnual.objects.filter(usuario_id=self.request.user.id)):
                        item = value.toJSON()
                        item['cumplimiento'] = True
                    
                        for val in item.values():
                            if val == '':
                                item['cumplimiento'] = False
                                break
                        data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Lista de Evidencias Anuales'
        context['create_url'] = reverse_lazy('erp:ea_create')
        context['list_url'] = reverse_lazy('erp:ea_list')
        context['entidad'] = 'Evidencia Anual'
        return context
class UpdateViewEvidenciaA(UpdateView):
    model = EvidenciaAnual
    form_class = FormEvidenciaA
    template_name = 'evidenciaA/create.html'
    success_url = reverse_lazy('erp:ea_list')
   
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
        context['title'] = 'Edición de una Evidencia Anual'
        context['entidad'] = 'Evidencias'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewEvidenciaA(DeleteView):
    model = EvidenciaAnual
    template_name = 'evidenciaA/delete.html'
    success_url = reverse_lazy('erp:ea_list')
    url_redirect = success_url

    def delete_files(self):
        fields = ['evidencia_comunicacion', 'evidencia_presentacion', 'evidencia_startup', 'evidencia_eeff', 'evidencia_dja']
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
        context['title'] = 'Eliminación de una Evidencia'
        context['entidad'] = 'Evidencias'
        context['list_url'] = self.success_url
        return context