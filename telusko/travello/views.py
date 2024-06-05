from django.shortcuts import render, redirect
from django.conf import settings
import os
from .models import Destination

def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def addDestination(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        imagen = request.FILES['imagen']  # Aquí debes usar request.FILES para acceder a la imagen enviada
        descripcion = request.POST['descripcion']
        precio = int(request.POST['precio'])
        oferta = bool(request.POST['oferta'])

        # Generamos la ruta completa donde se guardará la imagen en la carpeta 'pics' dentro del directorio de medios (MEDIA_ROOT)
        img_path = os.path.join(settings.MEDIA_ROOT, 'pics', imagen.name)

        # Guardamos la imagen en la ruta especificada
        with open(img_path, 'wb') as img_file:
            for chunk in imagen.chunks():
                img_file.write(chunk)

        # Creamos el objeto Destination con la ruta de la imagen
        destino = Destination(name=nombre, img=os.path.join('pics', imagen.name), desc=descripcion, price=precio, offer=oferta)
        destino.save()
        print('Imagen creada')
        return redirect('index')
    else:   
        destino = Destination()
    return render(request, 'addDest.html', {'destino': destino})
