# myra

## Librerias
radio player echo con:
* PySide6            6.9.3
* PyYAML             6.0.3



# NOTAS

avance del proyecto

## INTERFAZ
### PLAYLIST
- se creo el widget playlist
    - botones
    - ajuste de columnas

- se agrego la ventana modal, para agregar una Url
- la ventana modal ya agrega el item a la lista
- el icono se puede redimensionar con un slider
- orden a la playlist (interfaz) widgets en modulos
- crea playlist `.m3u`
- carga archivo `.m3u`
- ahora se puede mover los items arriba, abajo (mover el icono falla, lo deje comentado)
- en lugar de crear un widget persoanlizado use la nueva propidad de icono para le widget
- modifique un poco la manera de mover los iconos (arriba, abajo) ya que ahora ya no se usa un widget en la celda si no un icono propio del item
- [x] guardar items en un archivo `playlist.m3u`
- [x] cambiar el modo de agregar icono a la playlist (el modo actual tiene errores al mover el item de icono el resto funciona) **FIXED**
- al momento de asignar el icono es mejor usar el maximo valor de un inicio , porque luego ya no se puede redimensionar mas grande si el valor es intermedio
- al hacer doble click se obtiene info de la fila
- se puede vaciar la lista (clear items playlist)
- se puede borrar la fila seleccionada
- agregue tamaño inicial de los icono se puede asignar `init_row_height`
- [x] abrir dialogo para guardar un archivo `.m3u`
- cambie el modo de obtener data de la fila para guardar la playlist como .m3u (seguia con el anterior, ya lo actualize)
- [x] save cambiar modo de obtener data de una fila **FIXED**
- agregue iconos, incluyendo el logo del programa
- [x] cambiar el icono y nombre de la variable de editar por guardar 
- cambie de 3 columnas a 2, quitando la columna icono que ya no era necesaria
- mejore el dialogo para agregar nueva url
    - agregue boton pegar desde clipboard
    - la imagen ahora es de 150x150
    - en lugar de seleccionar se puede usar arrastrar la imagen sobre la ventana del dialogo d agregar url
    - ahora carga una imagen por defecto, para agregar una nueva url


### PLAYER
- ya agregue el cambio de icono a play y stop al player
- implemente el core para reproducir url de radio
- corregi agregar imagen al player al seleccinar un item y presioanar play (con doble click no habia problema)
- agregue un `lb_info` en la parte superior derecha
- cambie el ajuste de los labels (name y title)
- agrugue la funcion de `next` y `previous`
- al llegar al primero o al ultimo los botones de next y previous, muestran un mensaje en el label superior "NO NEXT", "NO PREVIOUS" respectivamente
- [ ] el slider de volumen tiene un range de 1-100, creo que se puede extender a 200
- [ ] ordenar y limpiar (todas estas funciones estan como en borrador)
- al label de info le agregue un margen derecho de 4 para que no este muy apegado al borde, ademas que reduje la entrelinea
- [ ] colocar imagen por defecto al agregar una nueva url
- [ ] para editar un item (seria mas facil copiar la url con click derecho, crear uno nuevo y borrar el anterior) **revisar**
- [ ] en caso de hacer lo de copiar la url se necesita agregar la funcion de copiar al url con click derecho
- funciona reproducir: haciendo doble click o presionando play con item seleccionado
- al slider de volumen le agregue un tooltip para mostrar el valor (solo funciona al hacer hover)
- [ ] al tooltip del slider revisar si se puede mostrar mientras se mueve (realizar de ser posible)
- quite lo de deshabilitar los botones de next y previous, porque al estar usando `flat` no se nota el cambio a `disabled`
- agregue shortcut de borrar elemento seleccionado de la playlist con `delete`


### MENUS
- estan agregados los textos
- [ ] falta enlazar a funciones
    - [x] abrir url
- [ ] para about falta crear una dialogo o ventana con info del programa y mpv version


### UTIL
- he creado el modulo `read_write` para crear archivos y leer archivos de configuracion, asi tambien para guardar la playlist
- he creado un modulo para leer y escribir archivos `.m3u`


### To do
- [ ] crear archivo `yml` con configuraciones
- [ ] playlist: abrir y borrar anterior playlist
- [ ] playlist: abrir y agregar a la anterior playlist
- [ ] orden y documentar metodos
- [ ] crear archivo de configuracion, asi como los metodos
- [ ] cargar estilos, por defecto
- [ ] agreger metodo de recargar ui (playlist)
- [ ] asignar size a la playlist
- [x] cambiando de 3 columnas a 2

