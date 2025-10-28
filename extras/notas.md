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


### UTIL
- he creado el modulo `read_write` para crear archivos y leer archivos de configuracion, asi tambien para guardar la playlist
- he creado un modulo para leer y escribir archivos `.m3u`

### To do
- [ ] crear archivo `yml` con configuraciones
- [ ] abrir dialogo para guardar un archivo `.m3u` (de momento solo crea el m3u por defecto)


