from django.forms import ModelForm
from django import forms
from .models import User
class FormUser(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = User
        fields = 'first_name','last_name','email','username','password','image','groups'
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus nombres'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus apellidos'
                }
            ),
            'email' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese sus correo',
                    'type':'email'
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese su nombre de usuario',
                   
                }
            ),
            'password':forms.PasswordInput(render_value=True,attrs={
                'placeholder':'Ingrese su contraseña'
            }),
            'groups': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple'
            })
        }
        exclude = ['user_permissions','last_login','date_joined','is_superuser','is_active','is_staff']
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password!=pwd:
                        u.set_password(pwd)
                u.save()
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['e'] = str(e)
        return data
