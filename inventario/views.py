from django.shortcuts import render, get_list_or_404, redirect
from .models import productoForms
from .forms import ProductoForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/producto_list.html', {'object_list': productos})

def producto_detail(request, pk):
    producto = get_list_or_404(producto, pk=pk)
    return render(request,'inventario/producto_detail.html', {'object': producto})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
        return render(request, 'inventario/producto_form.html', {'form': form})

def producto_update(request,pk):
    producto = get_list_or_404 (producto,pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            return redirect('producto_list')

    else:
        form = ProductoForm(instance=producto)
        return render(request, 'inventario/producto_form.html', {'form':form})

def producto_delete(request,pk):
    producto= get_list_or_404(producto,pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')

    return render(request, 'inventario/producto_confirm_delete.html', {'object': producto})
