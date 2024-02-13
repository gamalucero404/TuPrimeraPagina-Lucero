from django import forms

class  Form_Producto(forms.Form):
    producto = forms.CharField()
    categoria = forms.CharField()

class  Form_Tiendas(forms.Form):
    tienda = forms.CharField()
    caro = forms.BooleanField(label='Caro', required=False, widget=forms.CheckboxInput())
    barato = forms.BooleanField(label='Barato', required=False, widget=forms.CheckboxInput())

class  Form_Descuentos(forms.Form):
    tiendas = forms.CharField()
    productos_desc = forms.CharField()