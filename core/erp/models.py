from django.db import models
from django.forms import model_to_dict
from config.settings import MEDIA_URL
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.user.models import User
# Create your models here.
class Empresa(models.Model):
    empresa = models.CharField(max_length=255,verbose_name="Nombre de la Compania")
    ruc = models.CharField(max_length=255,verbose_name="RUC de la Compania")
    supervisor = models.CharField(max_length=255,verbose_name="Supervisor de la Compania",null=True,blank=True)
    encargado = models.CharField(max_length=255,verbose_name="Encargado de la Compania",null=True,blank=True)
    planillero = models.CharField(max_length=255,verbose_name="Planillero de la Compania",null=True,blank=True)
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    def __str__(self) -> str:
        return self.empresa
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = "Empresas"
        db_table = 'empresas'
        ordering = ['id']

class EvidenciaUnica(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    propuesta = models.FileField(upload_to='evidencia-unica/',null=True,blank=True,verbose_name="Propuesta del Servicio")
    fecha = models.DateField(auto_now=True,verbose_name="Fecha de Firma")
    desvinculacion = models.FileField(upload_to='evidencia-unica/',null=True,blank=True,verbose_name="Desvinculacion")
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    def __str__(self) -> str:
        return self.propuesta
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        item['propuesta'] = self.get_file(self.propuesta)
        item['fecha'] = self.fecha
        item['desvinculacion'] = self.get_file(self.desvinculacion)
        return item
    def get_file(self,file):
        if file:
            return f"{MEDIA_URL}{file}"
        return ""
    @receiver(pre_delete, sender=Empresa)
    def delete_related_evidencias(sender, instance, **kwargs):
        evidencias = EvidenciaUnica.objects.filter(empresa=instance)
        for evidencia in evidencias:
            # Eliminar archivos físicamente
            if evidencia.propuesta and evidencia.propuesta.path:
                os.remove(evidencia.propuesta.path)
            if evidencia.desvinculacion and evidencia.desvinculacion.path:
                os.remove(evidencia.desvinculacion.path)
        evidencias.delete()
    class Meta:
        verbose_name = "EvidenciaUnica"
        verbose_name_plural = "EvidenciasUnicas"
        db_table = "evidencia_unica"
        ordering = ['id']
class EvidenciaMensualI(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    enero = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Enero")
    febrero = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Febrero")
    marzo = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Marzo")
    abril = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Abril")
    mayo = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Mayo")
    junio = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Junio")
    julio = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Julio")
    agosto = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Agosto")
    septiembre = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Septiembre")
    octubre = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Octubre")
    noviembre = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Noviembre")
    diciembre = models.FileField(upload_to='evidencia-mensualI/',null=True,blank=True,verbose_name="Diciembre")
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    class Meta:
        verbose_name = 'EvidenciaMensualImpuesto'
        verbose_name_plural = 'EvidenciasMensualesImpuestos'
        db_table = 'evidencia_mensual_i'
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        item['enero'] = self.get_file(self.enero)
        item['febrero'] = self.get_file(self.febrero)
        item['marzo'] = self.get_file(self.marzo)
        item['abril'] = self.get_file(self.abril)
        item['mayo'] = self.get_file(self.mayo)
        item['junio'] = self.get_file(self.junio)
        item['julio'] = self.get_file(self.julio)
        item['agosto'] = self.get_file(self.agosto)
        item['septiembre'] = self.get_file(self.septiembre)
        item['octubre'] = self.get_file(self.octubre)
        item['noviembre'] = self.get_file(self.noviembre)
        item['diciembre'] = self.get_file(self.diciembre)
        return item
    def get_file(self,file):
        if file:
            return f"{MEDIA_URL}{file}"
        return ""
class EvidenciaMensualEF(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    enero = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Enero")
    febrero = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Febrero")
    marzo = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Marzo")
    abril = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Abril")
    mayo = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Mayo")
    junio = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Junio")
    julio = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Julio")
    agosto = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Agosto")
    septiembre = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Septiembre")
    octubre = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Octubre")
    noviembre = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Noviembre")
    diciembre = models.FileField(upload_to='evidencia-mensualEF/',null=True,blank=True,verbose_name="Diciembre")
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    class Meta:
        verbose_name = 'EvidenciaMensualEF'
        verbose_name_plural = 'EvidenciasMensualesEF'
        db_table = 'evidencia_mensual_ef'
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        item['enero'] = self.get_file(self.enero)
        item['febrero'] = self.get_file(self.febrero)
        item['marzo'] = self.get_file(self.marzo)
        item['abril'] = self.get_file(self.abril)
        item['mayo'] = self.get_file(self.mayo)
        item['junio'] = self.get_file(self.junio)
        item['julio'] = self.get_file(self.julio)
        item['agosto'] = self.get_file(self.agosto)
        item['septiembre'] = self.get_file(self.septiembre)
        item['octubre'] = self.get_file(self.octubre)
        item['noviembre'] = self.get_file(self.noviembre)
        item['diciembre'] = self.get_file(self.diciembre)
        return item
    def get_file(self,file):
        if file:
            return f"{MEDIA_URL}{file}"
        return ""
class EvidenciaMensualRC(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    enero = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Enero")
    febrero = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Febrero")
    marzo = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Marzo")
    abril = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Abril")
    mayo = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Mayo")
    junio = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Junio")
    julio = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Julio")
    agosto = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Agosto")
    septiembre = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Septiembre")
    octubre = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Octubre")
    noviembre = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Noviembre")
    diciembre = models.FileField(upload_to='evidencia-mensualRC/',null=True,blank=True,verbose_name="Diciembre")
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    class Meta:
        verbose_name = 'EvidenciaMensualRC'
        verbose_name_plural = 'EvidenciasMensualesRC'
        db_table = 'evidencia_mensual_rc'
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        item['enero'] = self.get_file(self.enero)
        item['febrero'] = self.get_file(self.febrero)
        item['marzo'] = self.get_file(self.marzo)
        item['abril'] = self.get_file(self.abril)
        item['mayo'] = self.get_file(self.mayo)
        item['junio'] = self.get_file(self.junio)
        item['julio'] = self.get_file(self.julio)
        item['agosto'] = self.get_file(self.agosto)
        item['septiembre'] = self.get_file(self.septiembre)
        item['octubre'] = self.get_file(self.octubre)
        item['noviembre'] = self.get_file(self.noviembre)
        item['diciembre'] = self.get_file(self.diciembre)
        return item
    def get_file(self,file):
        if file:
            return f"{MEDIA_URL}{file}"
        return ""
class EvidenciaMensualPI(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    enero = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Enero")
    febrero = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Febrero")
    marzo = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Marzo")
    abril = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Abril")
    mayo = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Mayo")
    junio = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Junio")
    julio = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Julio")
    agosto = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Agosto")
    septiembre = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Septiembre")
    octubre = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Octubre")
    noviembre = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Noviembre")
    diciembre = models.FileField(upload_to='evidencia-mensualPI/',null=True,blank=True,verbose_name="Diciembre")
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)

    class Meta:
        verbose_name = 'EvidenciaMensualPI'
        verbose_name_plural = 'EvidenciasMensualesPI'
        db_table = 'evidencia_mensual_pi'
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        item['enero'] = self.get_file(self.enero)
        item['febrero'] = self.get_file(self.febrero)
        item['marzo'] = self.get_file(self.marzo)
        item['abril'] = self.get_file(self.abril)
        item['mayo'] = self.get_file(self.mayo)
        item['junio'] = self.get_file(self.junio)
        item['julio'] = self.get_file(self.julio)
        item['agosto'] = self.get_file(self.agosto)
        item['septiembre'] = self.get_file(self.septiembre)
        item['octubre'] = self.get_file(self.octubre)
        item['noviembre'] = self.get_file(self.noviembre)
        item['diciembre'] = self.get_file(self.diciembre)
        return item
    def get_file(self,file):
        if file:
            return f"{MEDIA_URL}{file}"
        return ""
class EvidenciaAnual(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    evidencia_comunicacion = models.FileField(upload_to='evidencia-anual/',null=True,blank=True,verbose_name="Evidencia de la comunicacion")
    evidencia_presentacion = models.FileField(upload_to='evidencia-anual/',null=True,blank=True,verbose_name="Evidencia de la presentacion")
    evidencia_startup = models.FileField(upload_to='evidencia-anual/',null=True,blank=True,verbose_name="Evidencia Start Up")
    evidencia_eeff = models.FileField(upload_to='evidencia-anual/',null=True,blank=True,verbose_name="Evidencia de EEFF")
    evidencia_dja = models.FileField(upload_to='evidencia-anual/',null=True,blank=True,verbose_name="Evidencia de DJA")
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self) -> str:
        return self.evidencia_comunicacion
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        item['evidencia_comunicacion'] = self.get_file(self.evidencia_comunicacion)
        item['evidencia_presentacion'] = self.get_file(self.evidencia_presentacion)
        item['evidencia_startup'] = self.get_file(self.evidencia_startup)
        item['evidencia_eeff'] = self.get_file(self.evidencia_eeff)
        item['evidencia_dja'] = self.get_file(self.evidencia_dja)
        
        return item
    
    def get_file(self,file):
        if file:
            return f"{MEDIA_URL}{file}"
        return ""
    @receiver(pre_delete, sender=Empresa)
    def delete_related_evidencias(sender, instance, **kwargs):
        evidencias = EvidenciaAnual.objects.filter(empresa=instance)
        for evidencia in evidencias:
            # Eliminar archivos físicamente
            if evidencia.evidencia_comunicacion and evidencia.evidencia_comunicacion.path:
                os.remove(evidencia.evidencia_comunicacion.path)
            if evidencia.evidencia_presentacion and evidencia.evidencia_presentacion.path:
                os.remove(evidencia.evidencia_presentacion.path)
            if evidencia.evidencia_startup and evidencia.evidencia_startup.path:
                os.remove(evidencia.evidencia_startup.path)
            if evidencia.evidencia_eeff and evidencia.evidencia_eeff.path:
                os.remove(evidencia.evidencia_eeff.path)
            if evidencia.evidencia_dja and evidencia.evidencia_dja.path:
                os.remove(evidencia.evidencia_dja.path)
        evidencias.delete()

    class Meta:
        verbose_name = 'EvidenciaAnual'
        verbose_name_plural = "EvidenciasAnual"
        db_table = 'evidencia_anual'
        ordering = ['id']

@receiver(post_save, sender=Empresa)
def crear_evidencia_unica(sender, instance, created, **kwargs):
    if created:
        EvidenciaUnica.objects.create(empresa=instance)
        EvidenciaAnual.objects.create(empresa=instance)
        EvidenciaMensualI.objects.create(empresa=instance)
        EvidenciaMensualPI.objects.create(empresa=instance)
        EvidenciaMensualEF.objects.create(empresa=instance)
        EvidenciaMensualRC.objects.create(empresa=instance)
    