from django.http import JsonResponse
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.forms import FormEmpresas
from core.erp.models import Empresa
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

class CreateViewEmpresa(LoginRequiredMixin,CreateView):
    model = Empresa
    form_class = FormEmpresas
    template_name = 'empresa/create.html'
    success_url = reverse_lazy('erp:empresa_list')
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar nueva Compania"
        context['entidad'] = 'Empresas'
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
class ListViewEmpresa(LoginRequiredMixin,ListView):
    model = Empresa
    template_name = 'empresa/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
   
   
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for index,value in enumerate(Empresa.objects.all()):
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
        context['title'] = 'Listado de Empresas'
        context['create_url'] = reverse_lazy('erp:empresa_create')
        context['list_url'] = reverse_lazy('erp:empresa_list')
        context['entidad'] = 'Empresas'
        return context
class UpdateViewEmpresa(LoginRequiredMixin,UpdateView):
    model = Empresa
    form_class = FormEmpresas
    template_name = 'empresa/create.html'
    success_url = reverse_lazy('erp:empresa_list')
   
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
        context['title'] = 'Edición de una Empresa'
        context['entidad'] = 'Empresas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
class DeleteViewEmpresa(LoginRequiredMixin,DeleteView):
    model = Empresa
    template_name = 'empresa/delete.html'
    success_url = reverse_lazy('erp:empresa_list')
    
    url_redirect = success_url


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Empresa'
        context['Entidad'] = 'Empresas'
        context['list_url'] = self.success_url
        return context