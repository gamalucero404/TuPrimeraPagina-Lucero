from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import forms, models
from AppCoder.models import Productos, Tiendas, Descuentos

def inicio(request):
 

    return render(request, 'index.html')

def lista(request):
    mi_formulario = forms.Form_Producto()
    if request.method == 'POST':
        mi_formulario = forms.Form_Producto(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            print(informacion)
            categoria = informacion["categoria"]

            producto_existente = Productos.objects.filter(categoria=categoria).first()

            producto = models.Productos(nombre=informacion["producto"], categoria=categoria)
            producto.save()
            return render(request, 'lista.html', {'mi_formulario': forms.Form_Producto()})
    else:
        return render(request, "lista.html", {'mi_formulario': mi_formulario})


def buscar_categoria(request):
    return render(request, 'lista.html')

def buscar(request):
    categoria = request.GET.get('categoria')
    if categoria:
        producto = Productos.objects.filter(categoria=categoria)
        if producto:
            return render(request, 'resultado.html', {'producto': producto, 'categoria': categoria})
        else:
            mensaje = f"No se encontraron productos con dicho categoria: {categoria}."
            return HttpResponse(mensaje)
    else:
        mensaje = "No se proporcionó ninguna categoria para buscar."
        return HttpResponse(mensaje)


def tiendas(request):
    mi_formulario = forms.Form_Tiendas()

    if request.method == 'POST':
        mi_formulario = forms.Form_Tiendas(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            print(informacion)

            
            caro = informacion.get("caro", False)
            barato = informacion.get("barato", False)

            
            tienda = models.Tiendas(
                tienda=informacion.get("tienda"),
                caro=caro,
                barato=barato
            )
            tienda.save()

            return render(request, 'tiendas.html', {'mi_formulario': forms.Form_Tiendas()})  

    return render(request, "tiendas.html", {'mi_formulario': mi_formulario})

def descuentos(request):
    mi_formulario = forms.Form_Descuentos()
    if request.method == 'POST':
        mi_formulario = forms.Form_Descuentos(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            print(informacion)
            productos_desc = informacion["productos_desc"]

            producto_existente = Descuentos.objects.filter(productos_desc=productos_desc).first()

            tiendas = models.Descuentos(tiendas=informacion["tiendas"], productos_desc=productos_desc)
            tiendas.save()
            return render(request, 'descuentos.html', {'mi_formulario': forms.Form_Descuentos()})
    else:
        return render(request, "descuentos.html", {'mi_formulario': mi_formulario})