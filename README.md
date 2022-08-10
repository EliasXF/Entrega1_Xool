# Entrega intermedia del proyecto final

## Contenido
- Carpeta del proyecto que incluye las aplicaciones creadas con sus respectivos *models*, *templates*, base de datos en db.sqlite3
- README.md 

## Integrantes
 - Elias Xool - Creador del proyecto

## Accesos impórtantes 
- http://127.0.0.1:8000/index/ - *Template* principal del proyecto.
- Datos de administrador (http://127.0.0.1:8000/admin/)
    - usuario: adminuser
    - contraseña: admin123

## Funcionalidad

1. Acceso
    * En la terminal, entrar a la carpeta InterProject.
    * Poner el comando 'python manage.py runserver' para correr el servidor.
    * En un navegador, poner en el buscador 'http://127.0.0.1:8000/index/' para acceder a la página principal.
 
2. Contenido

    1. Inicio tendremos:
        * Una barra de navegación con ocho elementos presentes en todos los *templates* utilizados. 
            * Inicio
                * Nos redirecciona al *template* principal
            * Crear personajes
                * Nos redirecciona al *template* para crear personajes
                    * Encontraremos un *template* con un formulario a llenar para crear al objeto.
            * Crear vehículo
                * Nos redirecciona al *template* para crear vehículos
                    * Encontraremos un *template* con un formulario a llenar para crear al objeto.
            * Crear mascota
                * Nos redirecciona al *template* para crear mascotas
                    * Encontraremos un *template* con un formulario a llenar para crear al objeto.
            * Listas creadas
                * Nos redirecciona al *template* que contiene tres accesos para mandar a la lista de cada uno.
            * Una barra de búsqueda
                * Nos permite escribir para encontrar el contenido configurado.
                    * personajes: por nombre
                    * vehículos: por tipo
                    * mascota: por tipo
            * Un botón de búsqueda
                * Nos redirecciona al *template* de 'searh.html' para mostrar el contenido previamente escrito.
            * Un botón de acceso 
            * Nos redirecciona al panel de administración (http://127.0.0.1:8000/admin/)
                * Los accesos se encuentran en el apartado "Funcionalidad" de este documento. 

        * Un mensaje de bienvenida en el que podemos encontrar tres oraciones que, al igual que los tres elementos de la barra de navegación, nos redireccionaran al template para crear la opción seleccionada.
            * Crea tu propio personaje de RPG (Elemento "Crear personajes").
            * Crea el vehículo ideal (Elemento "Crear vehículo").
            * Crea tu mascota ideal (Elemento "Crear mascota").
        
        * Un footer 
       
3. Ejemplo de usabilidad
    
    * *click* en cualquira de las tres opciones para que nos redireccione al su respectivo *template* de creación.
    
    * Cada *temnplate* de creación contiene un formulario para crear un nuevo objeto. 

    * Llenaremos el formulario con los datos solicitados.

    * *click* en crear.
    
    * Creado el nuevo objeto, nos redireccionará al listado correspondiente (personaje, vehículo, mascota).

    * Se desplegarán los objetos en formato cascada.
    
    * Cada objeto tiene un butón para seleccionar, sin embargo, este no realiza ninguna acción.
    
    * Si se quiere crear un nuevo objeto, hacer *click* en "inicio" o en cualquiera de los tres elementos de "Crear ..." que se encuentran en el navbar.

    * Si se quiere ver las listas creadas, hacer *click* en "Listas" creadas para ser redireccionado a las opciones disponibles, hacer *click* en la deseada para ser mandado a su lista respectiva.

    * Haremos click en "Sign in" para ser direccionado al *template* de acceso del panel de administración. Llenaremos los campos de usuariop y contraseña con los datos proporcionados en el apartado "Funcionalidad" de este documento. 

    * En el panel, podemos ver nuestro usuario creado, los grupos de los objetos creados.
