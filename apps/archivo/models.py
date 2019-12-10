from django.db import models
import os
import uuid


# Create your models here.
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = "%s_%s.%s" % (filename, instance.fk, ext)
    else:
        filename = "%s.%s" % (uuid.uuid4().hex, ext)
    
    return os.path.join('files_upload', filename)

class Archivo(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to = content_file_name)

class Proquest(models.Model):
    publishing = models.CharField(max_length = 10)
    embargo = models.CharField(max_length = 10)
    third_party = models.CharField(max_length = 10)
    author_type = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 100)
    fname = models.CharField(max_length = 100)
    middle = models.CharField(max_length = 50, null = True, blank = True)
    page_count = models.CharField(max_length = 50)
    page_type = models.CharField(max_length = 50)
    external_id = models.CharField(max_length = 200)
    apply_copyright = models.CharField(max_length = 10)
    title = models.TextField()
    comp_date = models.CharField(max_length = 20)
    accept_date = models.CharField(max_length = 20)
    languaje = models.CharField(max_length = 10)
    degree = models.CharField(max_length = 50)
    inst_code = models.CharField(max_length = 10)
    inst_name = models.CharField(max_length = 250)
    processing_code = models.CharField(max_length = 50)
    para = models.TextField(blank = True, null = True)
    binary_type = models.CharField(max_length = 10)
    binary = models.CharField(max_length = 100)







