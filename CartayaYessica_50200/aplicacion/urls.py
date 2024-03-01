from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = "home"),

#________________Plantas________________#
    path('plantas/', plantas, name = "plantas"),
    path('plantas_crear/', createPlantas, name = "plantasCrear"),
    path('plantas_actualizar/<id_planta>', updatePlantas, name = "plantasActualizar"),
    path('plantas_borrar/<id_planta>', deletePlantas, name = "plantasBorrar"),
    

    path('buscar/', buscar, name = "buscar"),
    path('buscarPlantas/', buscarPlantas, name = "buscarPlantas"),


#________________Macetas________________#
    path('macetas/', macetas, name = "macetas"),
    path('macetas_crear/', createMacetas, name = "macetasCrear"),
    path('macetas_actualizar/<id_maceta>', updateMacetas, name = "macetasActualizar"),
    path('macetas_borrar/<id_maceta>', deleteMacetas, name = "macetasBorrar"),


#_____________Fertilizantes_____________#
    path('fertilizantes/', fertilizantes, name = "fertilizantes"),
    path('fertilizantes_crear/', createFertilizantes, name = "fertilizantesCrear"),
    path('fertilizantes_actualizar/<id_fertilizante>', updateFertilizantes, name = "fertilizantesActualizar"),
    path('fertilizantes_borrar/<id_fertilizante>', deleteFertilizantes, name = "fertilizantesBorrar"),


#_____________Plaguicidas_____________#
    path('plaguicidas/', plaguicidas, name = "plaguicidas"),
    path('plaguicidas_crear/', createPlaguicidas, name = "plaguicidasCrear"),
    path('plaguicidas_actualizar/<id_plaguicida>', updatePlaguicidas, name = "plaguicidasActualizar"),
    path('plaguicidas_borrar/<id_plaguicida>', deletePlaguicidas, name = "plaguicidasBorrar"),


#_____________Login, Logout, Registro_____________#
    path('login/', login_request, name = "login"),
    path('registro/', register, name = "registro"),
    path('logout/', custom_logout, name = "logout"),
    #path('logout/', LogoutView.as_view(template_name = "aplicacion/logout.html"), name = "logout"),

#_____________Editar Perfil_____________#
    path('editar_perfil/', editarPerfil, name = "editar_perfil"),

#_____________Avatar_____________#
    path('agregar_avatar/', agregarAvatar, name = "agregar_avatar"),

#_____________Sobre Mí_____________#
    path('sobreMi/', sobreMi, name = "sobreMi"),

    
]