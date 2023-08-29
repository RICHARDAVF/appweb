from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from crum import get_current_request
from config.settings import MEDIA_URL, STATIC_URL
# Create your models here.
# class Rol(models.Model):
#     rol = models.CharField(max_length=50,verbose_name="Rol")
#     def __str__(self):
#         return self.rol
#     def toJSON(self):
#         item = model_to_dict(self)
#         return item
#     class Meta:
#         verbose_name = "Rol"
#         verbose_name_plural = "Roles"
#         db_table = "roles"
#         ordering = ["id"]
class User(AbstractUser):
    dni = models.CharField(max_length=10,verbose_name="Documento",null=True,blank=True)
    area = models.CharField(max_length=255,null=True,blank=True,verbose_name="Area")
    # rol = models.ForeignKey(Rol,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Rol")
    image = models.ImageField(upload_to='users/',null=True,blank=True,verbose_name="Imagen")
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True,verbose_name="Token")
    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        # item['rol'] = self.rol.toJSON() if self.rol else {'rol':'Ninguna'}
       
        return item
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass
