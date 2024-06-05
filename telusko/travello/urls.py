from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('addDest/', views.addDestination, name="addDest"),
    path('listaDest/', views.listarDestinos, name="listaDest"),
    path('editDest/<int:id_destino>', views.editDestinos, name="editDest"),
    path('actDest/<int:id_destino>', views.actualizarDestinos, name="actDest"),
    path('elimDest/<int:id_destino>', views.eliminarDest, name="delDest"),
]