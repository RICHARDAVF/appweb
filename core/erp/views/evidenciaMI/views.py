from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.core.files.storage import default_storage
from core.erp.forms import FormEvidenciaMI
from core.erp.models import EvidenciaMensualI
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
class CreateViewEvidenciaMI(CreateView):
    model = EvidenciaMensualI
    form_class = FormEvidenciaMI
    template_name = 'evidenciaMI/create.html'
    success_url = reverse_lazy('erp:emi_list')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "Evidencia Mensual Impuestos"
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
class ListViewEvidenciaMI(ListView):
    model = EvidenciaMensualI
    template_name = 'evidenciaMI/list.html'
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
                    for index,value in enumerate(EvidenciaMensualI.objects.all()):
                        item = value.toJSON()
                        item['cumplimiento'] = True
                        for val in item.values():
                            if val == '':
                                item['cumplimiento'] = False
                                break
                        item['position'] = index
                        data.append(item)
                else:
                    for index,value in enumerate(EvidenciaMensualI.objects.filter(usuario_id=self.request.user.id)):
                        item = value.toJSON()
                        item['cumplimiento'] = True
                        for val in item.values():
                            if val == '':
                                item['cumplimiento'] = False
                                break
                        item['position'] = index
                        data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Lista de Evidencias Mensuales Impuestos'
        context['create_url'] = reverse_lazy('erp:emi_create')
        context['list_url'] = reverse_lazy('erp:emi_list')
        context['entidad'] = 'Evidencia Mensual'
        return context
class UpdateViewEvidenciaMI(UpdateView):
    model = EvidenciaMensualI
    form_class = FormEvidenciaMI
    template_name = 'evidenciaMI/create.html'
    success_url = reverse_lazy('erp:emi_list')
   
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
        context['title'] = 'Edición de una Evidencia Mensual Impuestos'
        context['entidad'] = 'Evidencias'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewEvidenciaMI(DeleteView):
    model = EvidenciaMensualI
    template_name = 'evidenciaMI/delete.html'
    success_url = reverse_lazy('erp:emi_list')
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
            #self.delete_files()
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Evidencia Mensual Impuestos'
        context['entidad'] = 'Evidencias'
        context['list_url'] = self.success_url
        return context