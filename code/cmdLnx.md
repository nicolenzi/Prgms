COMANDOS LINUX

sudo: abrebiatura para super usuario, permite realizar tareas de superusuario

sudo (resto comando)
se puede añadir opcion:

-k o reset-timestamp invalida el archivo timestamp.
-g o -group=group ejecuta comandos como un nombre o ID de grupo especificado.
-h o -host=host ejecuta comandos del host.
__


pwd: muestra la ruta actual en la que se esta trabajando, las rutas comiezan con "/".

pwd (opcion)

opciones a añadir:
-L o -logical imprime contenido de las variables de entorno incluido enlases simbolicos.
-P o -physical imprime la ruta real del directorio actual.
__


cd: entra y navega en las rutas.

cd .. para ir a un directorio hacia arriba.
cd- para ir a un directorio anterior.

ls: muestra el contedido del directorio,

ls -R lista todos los archivos en los subdirectorios.
ls -a muestra los archivos ocultos.
ls -al lista los archivos y derectorios con informacion detallada con permisos, tamaño, propietario, etc.
__


cat:
combina el contenido de los archivos, tambien lee y crea archivos con el contenido deseado.

cat eje1.txt eje2.txt > destino.txt : para combinar dos archivos y crear un destino o sobreescribir.
cat > ejemplo.txt : para crear el archivo o sobreescribir. despues de ejecutar el comando se escribe dentro
del texto, para finalizar precionar ctl + D y se guarda en eachivo junto con el contenido.
ls -l :visualiza el archivo si no se encuentra.
cat eje.txt : leer archivo.
cat eje.txt > ejesalida.txt : trasfiere todo el contedido del primer archivo al segundo(<<?)