from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.contrib import messages
from apps.archivo.forms import ArchivoForm, ProquestForm
from apps.archivo.models import Archivo, Proquest
from apps.archivo.xml_create.creator import CreateXML
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
 
# Vistas basadas en Metodos
def archivo(request):
    archivo = Archivo.objects.all()
    registro = Proquest.objects.all()
    contexto = {'archivos':archivo, 'registros':registro}
    return render(request, 'archivo/archivo.html', contexto)

def proquest_zip(request, pk):
    registros = Proquest.objects.filter( id = pk)
    parse_result = CreateXML().queryset_to_xml(registros[0])
    return redirect('/archivo/media/%s/%s' % ('files_zip', parse_result))

def download_file(request, path_f, file_name):
    path_to_file = 'media/%s/%s' % (path_f,file_name)
    file_download = open(path_to_file, 'rb')
    #myfile = open(f)
    response = HttpResponse(file_download, content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    #response['X-Sendfile'] = smart_str(path_to_file)
    return response


#Vistas basadas en Clases
class Archivo_form(BSModalCreateView):
    form_class = ArchivoForm
    template_name = 'archivo/archivo_form.html'
    success_message = 'Archivo guardado.'
    success_url = reverse_lazy('archivo:index')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            parse_result = None
            parse_result = None
            for filename, file in request.FILES.items():
                parse_result = CreateXML().csv_to_xml(request.FILES[filename].file, filename)
            return self.form_valid(form)
        return self.form_invalid(form)

class Proquest_form(CreateView):
    form_class = ProquestForm
    template_name = 'archivo/proquest_form.html'
    success_message = 'Se creo el registro correctamente'
    success_url = reverse_lazy('archivo:single')

class Proquest_update(UpdateView):
    form_class = ProquestForm
    model = Proquest
    template_name = 'archivo/proquest_form.html'
    success_message = 'Registro actualizado'
    success_url = reverse_lazy('archivo:index')


# Vistas basadas en Metodos

#def archvo_form(request):
    # if request.method == 'POST':
    #     form = ArchivoForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print (request.FILES.items())
    #         parse_result = None
    #         for filename, file in request.FILES.items():
    #             parse_result = CreateXML().csv_to_xml(request.FILES[filename].file, filename)
    #         if parse_result is not None:
    #             messages.error(request, parse_result)
    #             #error_message = parse_result
    #             #return redirect(reverse("archivo:nuevo"))
    #         #form.save()
    #     #return redirect('archivo:index')
    # else:
    #     form = ArchivoForm()
    
    #return render(request, 'archivo/archivo_form.html', {'form':form})    