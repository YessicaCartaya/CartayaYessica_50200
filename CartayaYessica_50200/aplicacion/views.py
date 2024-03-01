from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")


#_____________Plantas_____________#

@login_required
def plantas(request):
    contexto = {'plantas': Planta.objects.all()}
    return render(request, "aplicacion/plantas.html", contexto)


@login_required
def createPlantas(request):
    if request.method == "POST":
        miForm = PlantaForm(request.POST)
        if miForm.is_valid():
            planta_nombre = miForm.cleaned_data.get("nombre")
            planta_ambiente = miForm.cleaned_data.get("ambiente")
            planta_riego = miForm.cleaned_data.get("riego")
            planta_iluminacion = miForm.cleaned_data.get("iluminacion")
            planta_tamaño = miForm.cleaned_data.get("tamaño")
            planta = Planta(nombre=planta_nombre, ambiente=planta_ambiente, riego=planta_riego, iluminacion= planta_iluminacion, tamaño=planta_tamaño)
            planta.save()
            return redirect(reverse_lazy('plantas'))
            # return render(request,"aplicacion/home.html")
    else:
        miForm = PlantaForm()
    return render(request, "aplicacion/plantasForm.html",{"form":miForm})


@login_required
def updatePlantas(request, id_planta):
    planta = Planta.objects.get(id=id_planta)
    if request.method == "POST":
        miForm = PlantaForm(request.POST)
        if miForm.is_valid():
            planta.nombre = miForm.cleaned_data.get("nombre")
            planta.ambiente = miForm.cleaned_data.get("ambiente")
            planta.riego = miForm.cleaned_data.get("riego")
            planta.iluminacion = miForm.cleaned_data.get("iluminacion")
            planta.tamaño = miForm.cleaned_data.get("tamaño")
            planta.save()
            return redirect(reverse_lazy('plantas'))
    else:
        miForm = PlantaForm(initial={
            'nombre': planta.nombre,
            'ambiente': planta.ambiente,
            'riego': planta.riego,
            'iluminacion': planta.iluminacion,
            'tamaño': planta.tamaño,
        })
    return render(request, "aplicacion/plantasForm.html",{"form":miForm})


@login_required
def deletePlantas(request, id_planta):
    planta = Planta.objects.get(id=id_planta)
    planta.delete()
    return redirect(reverse_lazy('plantas'))
    

#_____________Buscar Plantas_____________#

@login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")


@login_required
def buscarPlantas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        plantas = Planta.objects.filter(nombre__icontains=patron)
        contexto= {"plantas":plantas}
        return render(request, "aplicacion/plantas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


#_____________Macetas_____________#

@login_required
def macetas(request):
    contexto = {'macetas': Maceta.objects.all()}
    return render(request, "aplicacion/macetas.html", contexto)


@login_required
def createMacetas(request):
    if request.method == "POST":
        miForm = MacetaForm(request.POST)
        if miForm.is_valid():
            maceta_material = miForm.cleaned_data.get("material")
            maceta_forma = miForm.cleaned_data.get("forma")
            maceta_tamaño = miForm.cleaned_data.get("tamaño")
            macetas_color = miForm.cleaned_data.get("color")
            maceta = Maceta(material=maceta_material, forma=maceta_forma, tamaño=maceta_tamaño, color= macetas_color)
            maceta.save()
            return redirect(reverse_lazy('macetas')) 
            #return render(request,"aplicacion/home.html")
    else:
        miForm = MacetaForm()
    return render(request, "aplicacion/macetasForm.html",{"form":miForm})


@login_required
def updateMacetas(request, id_maceta):
    maceta = Maceta.objects.get(id=id_maceta)
    if request.method == "POST":
        miForm = MacetaForm(request.POST)
        if miForm.is_valid():
            maceta.material = miForm.cleaned_data.get("material")
            maceta.forma = miForm.cleaned_data.get("forma")
            maceta.tamaño = miForm.cleaned_data.get("tamaño")
            maceta.color = miForm.cleaned_data.get("color")
            maceta.save()
            return redirect(reverse_lazy('macetas'))
    else:
        miForm = MacetaForm(initial={
            'material': maceta.material,
            'forma': maceta.forma,
            'tamaño': maceta.tamaño,
            'color': maceta.color,
        })
    return render(request, "aplicacion/macetasForm.html",{"form":miForm})


@login_required
def deleteMacetas(request, id_maceta):
    maceta = Maceta.objects.get(id=id_maceta)
    maceta.delete()
    return redirect(reverse_lazy('macetas'))


#_____________Fertilizantes_____________#

@login_required
def fertilizantes(request):
    contexto = {'fertilizantes': Fertilizante.objects.all()}
    return render(request, "aplicacion/fertilizantes.html",contexto)


@login_required
def createFertilizantes(request):
    if request.method == "POST":
        miForm = FertilizanteForm(request.POST)
        if miForm.is_valid():
            fertilizante_nombre = miForm.cleaned_data.get("nombre")
            fertilizante_nutrientes = miForm.cleaned_data.get("nutrientes")
            fertilizante_dosis = miForm.cleaned_data.get("dosis")
            fertilizante_precauciones = miForm.cleaned_data.get("precauciones")
            fertilizante = Fertilizante(nombre=fertilizante_nombre, nutrientes=fertilizante_nutrientes, dosis=fertilizante_dosis, precauciones= fertilizante_precauciones)
            fertilizante.save()
            return redirect(reverse_lazy('fertilizantes')) 
            #return render(request,"aplicacion/home.html")
    else:
        miForm = FertilizanteForm()
    return render(request, "aplicacion/fertilizantesForm.html",{"form":miForm})


@login_required
def updateFertilizantes(request, id_fertilizante):
    fertilizante = Fertilizante.objects.get(id=id_fertilizante)
    if request.method == "POST":
        miForm = FertilizanteForm(request.POST)
        if miForm.is_valid():
            fertilizante.nombre = miForm.cleaned_data.get("nombre")
            fertilizante.nutrientes = miForm.cleaned_data.get("nutrientes")
            fertilizante.dosis = miForm.cleaned_data.get("dosis")
            fertilizante.precauciones = miForm.cleaned_data.get("precauciones")
            fertilizante.save()
            return redirect(reverse_lazy('fertilizantes'))
    else:
        miForm = FertilizanteForm(initial={
            'nombre': fertilizante.nombre,
            'nutrientes': fertilizante.nutrientes,
            'dosis': fertilizante.dosis,
            'precauciones': fertilizante.precauciones,
        })
    return render(request, "aplicacion/fertilizantesForm.html",{"form":miForm})


@login_required
def deleteFertilizantes(request, id_fertilizante):
    fertilizante = Fertilizante.objects.get(id=id_fertilizante)
    fertilizante.delete()
    return redirect(reverse_lazy('fertilizantes'))


#_____________Plaguicidas_____________#

@login_required
def plaguicidas(request):
    contexto = {'plaguicidas': Plaguicida.objects.all()}
    return render(request, "aplicacion/plaguicidas.html",contexto)


@login_required
def createPlaguicidas(request):
    if request.method == "POST":
        miForm = PlaguicidaForm(request.POST)
        if miForm.is_valid():
            plaguicida_nombre = miForm.cleaned_data.get("nombre")
            plaguicida_presentacion = miForm.cleaned_data.get("presentacion")
            plaguicida_plaga = miForm.cleaned_data.get("plaga")
            plaguicida_contenidoNeto = miForm.cleaned_data.get("contenidoNeto")
            plaguicida = Plaguicida(nombre=plaguicida_nombre, presentacion=plaguicida_presentacion, plaga=plaguicida_plaga, contenidoNeto= plaguicida_contenidoNeto)
            plaguicida.save()
            return redirect(reverse_lazy('plaguicidas')) 
    else:
        miForm = PlaguicidaForm()
    return render(request, "aplicacion/plaguicidasForm.html",{"form":miForm})


@login_required
def updatePlaguicidas(request, id_plaguicida):
    plaguicida = Plaguicida.objects.get(id=id_plaguicida)
    if request.method == "POST":
        miForm = PlaguicidaForm(request.POST)
        if miForm.is_valid():
            plaguicida.nombre = miForm.cleaned_data.get("nombre")
            plaguicida.presentacion = miForm.cleaned_data.get("presentacion")
            plaguicida.plaga = miForm.cleaned_data.get("plaga")
            plaguicida.contenidoNeto = miForm.cleaned_data.get("contenidoNeto")
            plaguicida.save()
            return redirect(reverse_lazy('plaguicidas'))
    else:
        miForm = PlaguicidaForm(initial={
            'nombre': plaguicida.nombre,
            'presentacion': plaguicida.presentacion,
            'plaga': plaguicida.plaga,
            'contenidoNeto': plaguicida.contenidoNeto,
        })
    return render(request, "aplicacion/plaguicidasForm.html",{"form":miForm})


@login_required
def deletePlaguicidas(request, id_plaguicida):
    plaguicida = Plaguicida.objects.get(id=id_plaguicida)
    plaguicida.delete()
    return redirect(reverse_lazy('plaguicidas'))


#_____________Login, Logout, Registro_____________#

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username = usuario , password = password)
        if user is not None:
            login(request, user)

            #_____________Avatar_____________#
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session ["avatar"] = avatar


            return render(request,'aplicacion/home.html')
        else:
            return redirect(reverse_lazy('login'))

    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html",{"form":miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home')) 
    else:
        miForm = RegistroForm()
    return render(request, "aplicacion/registro.html",{"form":miForm})

def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('home')) 


#_____________Editar Perfil_____________#

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            update_session_auth_hash(request,user)
            return render(request, "aplicacion/home.html")
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html",{"form":form})


#_____________Avatar_____________#

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)
            #_____________Borrar Avatar Anterior_____________#
            avatarViejo=Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar= Avatar(user=usuario,imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_____________Url de Imagen en request_____________#
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/home.html")
    else:
        form = AvatarForm()
    return render(request, "aplicacion/agregarAvatar.html",{"form":form})


def sobreMi(request):
    return render(request, "aplicacion/sobreMi.html")