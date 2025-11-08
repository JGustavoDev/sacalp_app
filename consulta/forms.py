from django import forms
from .models import Anamnese

class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese
        exclude = ['cliente', 'data_consulta']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            
          
            elif isinstance(field, forms.DateField):
                field.widget.attrs['type'] = 'date'
            
          
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            
            
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 3