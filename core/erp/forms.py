from django.forms import ModelForm,TextInput
from core.erp.models import Empresa
from core.erp.models import *
class FormEmpresas(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            
            'usuario':TextInput(attrs={
                'type':"hidden" 
            })
        }
    def save(self, commit=True):
        data = {}
        form = super()
    
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
class FormEvidenciaU(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = EvidenciaUnica
        fields = '__all__'
        widgets = {
            'empresa':TextInput(attrs={
                "class":"form-control",
                "readonly":True
            }),
            'usuario':TextInput(attrs={
                'type':"hidden"
            })
        }
    def save(self, commit = True ):
        data = {}
        form = super()
      
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data
class FormEvidenciaMI(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = EvidenciaMensualI
        fields = '__all__'
        widgets = {
            'empresa':TextInput(attrs={
                "class":"form-control",
                "readonly":True
            }),
            'usuario':TextInput(attrs={
                'type':"hidden"
            })
        }
    def save(self, commit = True ):
        data = {}
        form = super()
      
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data
class FormEvidenciaMEF(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = EvidenciaMensualEF
        fields = '__all__'
        widgets = {
            'empresa':TextInput(attrs={
                "class":"form-control",
                "readonly":True
            }),
            'usuario':TextInput(attrs={
                'type':"hidden"
            })
        }
    def save(self, commit = True ):
        data = {}
        form = super()
      
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data
class FormEvidenciaMRC(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = EvidenciaMensualRC
        fields = '__all__'
        widgets = {
            'empresa':TextInput(attrs={
                "class":"form-control",
                "readonly":True
            }),
            'usuario':TextInput(attrs={
                'type':"hidden"
            })
        }
    def save(self, commit = True ):
        data = {}
        form = super()
      
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data
class FormEvidenciaMPI(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = EvidenciaMensualPI
        fields = '__all__'
        widgets = {
            'empresa':TextInput(attrs={
                "class":"form-control",
                "readonly":True
            }),
            'usuario':TextInput(attrs={
                'type':"hidden"
            })
        }
    def save(self, commit = True ):
        data = {}
        form = super()
      
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data
class FormEvidenciaA(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = EvidenciaAnual
        fields = '__all__'
        widgets = {
            'empresa':TextInput(attrs={
                "class":"form-control",
                "readonly":True
            }),
            'usuario':TextInput(attrs={
                'type':"hidden"
            })
        }
    def save(self, commit = True ):
        data = {}
        form = super()
      
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data