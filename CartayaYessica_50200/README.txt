# Nombre Proyecto: Viveros Verde es Vida
# Alumno: Yessica Cartaya
# Curso: Python
# Comision:50200
# Fecha: 29/02/2024
# Version: Proyecto Final

# Aplicacion que permite registrar las plantas, Macetas, Fettilizantes y Plaguicidas disponiles en Stock para un Vivero

- Los modelos que posee esta aplicacion son:
    - Planta
    - Maceta
    - Fertilizante
	- Plaguicida

- Prueba de la aplicacion: 
    - Se ingresa al http://localhost:8000/aplicacion/, donde encontraremos en el menu los siguientes botones:
		- Boton Login: (http://localhost:8000/aplicacion/login/) donde podremos loguearnos para dar inicio a la navegacion del proyecto, para este proyecto 
				se creo el siguiente usuario para el acceso:
				- Usuario: admin
				- Password: coder50200
				
		- Boton Registro: (http://localhost:8000/aplicacion/registro/) donde podremos registrarnos como nuevos usuarios 
	
	- Una vez logueados tendremos acceso al siguiente menu:
	
        - Inicio:  Muestra el Home de la aplicacion, el cual contiene el diseño que se hereda en las demas opciones del Menu
                   y el nombre del proyecto. 
				   
        - Plantas: Lleva a la pagina de Plantas (http://localhost:8000/aplicacion/plantas/) donde podemos visualizar todas las plantas registradas en 
				   la Base de Datos. En esta pagina podemos encontrar las acciones de:
				   - Crear: (http://localhost:8000/aplicacion/plantas_crear/) donde podemos realizar el registro de los datos de una nueva planta.
				   - Actualizar: (http://localhost:8000/aplicacion/plantas_actualizar/<id_planta>) donde se puede actualizar los datos de una maceta ya registrada
				   - Borrar: (http://localhost:8000/aplicacion/plantas_borrar/<id_planta>) con el que podremos borrar de la base de datos la maceta seleccionada
				   
        - Macetas: Lleva a la pagina de Macetas (http://localhost:8000/aplicacion/macetas/) donde podemos visualizar todas las macetas registradas en 
				   la Base de Datos. En esta pagina podemos encontrar las acciones de:
				   - Crear: (http://localhost:8000/aplicacion/macetas_crear/) donde podemos realizar el registro de los datos de una nueva maceta.
				   - Actualizar: (http://localhost:8000/aplicacion/macetas_actualizar/<id_maceta>) donde se puede actualizar los datos de una planta ya registrada
				   - Borrar: (http://localhost:8000/aplicacion/macetas_borrar/<id_maceta>) con el que podremos borrar de la base de datos la planta seleccionada
				   
        - Fertilizantes: Lleva a la pagina de Fertilizantes (http://localhost:8000/aplicacion/fertilizantes/) donde podemos visualizar todas los fertilizantes
				   registrados en la Base de Datos. En esta pagina podemos encontrar las acciones de:
				   - Crear: (http://localhost:8000/aplicacion/fertilizantes_crear/) donde podemos realizar el registro de los datos de un nuevo fertilizante.
				   - Actualizar: (http://localhost:8000/aplicacion/fertilizantes_actualizar/<id_fertilizante>) donde se puede actualizar los datos de 
							un fertilizante ya registrado
				   - Borrar: (http://localhost:8000/aplicacion/fertilizantes_borrar/<id_fertilizante>) con el que podremos borrar de la base de datos el fertilizante
							seleccionado.
							
        - Plaguicida: Lleva a la pagina de Plaguicidas (http://localhost:8000/aplicacion/plaguicidas/) donde podemos visualizar todas los plaguicidas
				   registrados en la Base de Datos. En esta pagina podemos encontrar las acciones de:
				   - Crear: (http://localhost:8000/aplicacion/plaguicidas_crear/) donde podemos realizar el registro de los datos de un nuevo plaguicida.
				   - Actualizar: (http://localhost:8000/aplicacion/plaguicidas_actualizar/<id_plaguicida>) donde se puede actualizar los datos de 
							un plaguicida ya registrado
				   - Borrar: (http://localhost:8000/aplicacion/plaguicidas_borrar/<id_plaguicida>) con el que podremos borrar de la base de datos el plaguicida
							seleccionado.
				   
        - Buscar:  lleva al formulario donde se realiza el patron de busqueda por nombre de planta (http://localhost:8000/aplicacion/buscar/)
                   al presionar buscar, realiza la buscada de las plantas existentes en la Base de Datos con ese patron de busqueda
		
		- Avatar:  (http://localhost:8000/aplicacion/agregar_avatar/) Donde podremos cambiar la imagen del Avatar de nuestra preferencia.
		
		- Boton de Perfil: (http://localhost:8000/aplicacion/editar_perfil/) Que nos permite editar los datos del usuario que se encuetra logueado.
		
		- Boton de Logout: El cual nos desloguea y nos redirecciona nuevamnete al incio del proyecto donde se solicita loguearse para acceder nuevamente.


Nota: El video se encuentra alojado en mi Drive comparto el enlace de acceso (https://drive.google.com/drive/folders/13LVPdEYefVYukHrc7ZVQNPXQwHpX7-R9?usp=sharing) 
      ya que no lo pude subir al github por lo pesado que es.
		
		

