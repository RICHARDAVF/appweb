from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,View
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
from core.user.forms import FormUser
from core.user.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ListViewUser(LoginRequiredMixin,ListView):
    model = User
    template_name = 'user/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
           
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
            
        except Exception as e:
            data['error'] = str(e)
       
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = reverse_lazy('user:user_create')
        context['list_url'] = reverse_lazy('user:user_list')
        context['entidad'] = 'Usuarios'
        return context
class CreateViewUser(LoginRequiredMixin,CreateView):
    model = User
    form_class = FormUser
    template_name = 'user/create.html'
    success_url = reverse_lazy('user:user_list')
   
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Usuario'
        context['entidad'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
class UpdateViewUser(UpdateView):
    model = User
    form_class = FormUser
    template_name = 'user/create.html'
    success_url = reverse_lazy('user:user_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
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
        context['title'] = 'Edición de un Usuario'
        context['entidad'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class DeleteViewUser(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user:user_list')
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
        context['title'] = 'Eliminación de un Usuario'
        context['entidad'] = 'Usuarios'
        context['list_url'] = self.success_url
        return context

class UserChangeGroup(View):

    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('user:user_list'))