from django import forms
from apps.archivo.models import Archivo, Proquest
from bootstrap_modal_forms.forms import BSModalForm
class ArchivoForm(BSModalForm):

    class Meta:
        model = Archivo

        fields = [
            'nombre',
            'descripcion',
            'archivo'
        ]

        labels = {
            'nombre' : 'Nombre del archivo',
            'descripcion': 'Descripcion del archivo',
            'archivo': 'Archivo'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'archivo': forms.FileInput(attrs={'class':'custom-file-input', 'type' : 'file'})
        }
class ProquestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProquestForm, self).__init__(*args, **kwargs)
        self.fields['middle'].required = False
        self.fields['para'].required = False
        self.fields['accept_date'].required = False
    
    class Meta:
        model = Proquest

        fields = [
            'publishing' ,
            'embargo' ,
            'third_party',
            'author_type',
            'surname',
            'fname',
            'middle',
            'page_count',
            'page_type',
            'external_id' ,
            'apply_copyright' ,
            'title',
            'comp_date' ,
            'accept_date' ,
            'languaje' ,
            'degree',
            'inst_code' ,
            'inst_name' ,
            'processing_code' ,
            'para' ,
            'binary_type' ,
            'binary'
        ]

        labels = {
            'publishing' : 'publishing_option',
            'embargo' : 'embargo_code',
            'third_party' : 'third_party_search',
            'author_type' : 'type',
            'surname' : 'DISS_surname',
            'fname' : 'DISS_fname',
            'middle' : 'DISS_middle',
            'page_count' : 'page_count',
            'page_type' : 'type',
            'external_id' : 'external_id',
            'apply_copyright' : 'apply_for_copyright',
            'title' : 'DISS_title',
            'comp_date' : 'DISS_comp_date',
            'accept_date' : 'DISS_accept_date',
            'languaje' : 'DISS_language',
            'degree' : 'DISS_degree',
            'inst_code' : 'DISS_inst_code',
            'inst_name' : 'DISS_inst_name',
            'processing_code' : 'DISS_processing_code',
            'para' : 'DISS_para',
            'binary_type' : 'type',
            'binary' : 'DISS_binary'
        }

        widgets = {
            'publishing' : forms.TextInput(attrs={'class':'form-control'}),
            'embargo' : forms.TextInput(attrs={'class':'form-control'}),
            'third_party' : forms.TextInput(attrs={'class':'form-control'}),
            'author_type' : forms.TextInput(attrs={'class':'form-control'}),
            'surname' : forms.TextInput(attrs={'class':'form-control'}),
            'fname' : forms.TextInput(attrs={'class':'form-control'}),
            'middle' : forms.TextInput(attrs={'class':'form-control'}),
            'page_count' : forms.TextInput(attrs={'class':'form-control'}),
            'page_type' : forms.TextInput(attrs={'class':'form-control'}),
            'external_id' : forms.TextInput(attrs={'class':'form-control'}),
            'apply_copyright' : forms.TextInput(attrs={'class':'form-control'}),
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'comp_date' : forms.TextInput(attrs={'class':'form-control'}),
            'accept_date' : forms.TextInput(attrs={'class':'form-control'}),
            'languaje' : forms.TextInput(attrs={'class':'form-control'}),
            'degree' : forms.TextInput(attrs={'class':'form-control'}),
            'inst_code' : forms.TextInput(attrs={'class':'form-control'}),
            'inst_name' : forms.TextInput(attrs={'class':'form-control'}),
            'processing_code' : forms.TextInput(attrs={'class':'form-control'}),
            'para' : forms.Textarea(attrs={'class':'form-control', 'rows': '3'}),
            'binary_type' : forms.TextInput(attrs={'class':'form-control'}),
            'binary' : forms.TextInput(attrs={'class':'form-control'})
        }
    