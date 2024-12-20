# RedSocialEV4
Evaluación 4 Backend

Pasos para configurar e iniciar el proyecto:

Tener instalado python y agregado en el PATH
Abrimos una terminal y usamos la siguiente linea de comando

pip install django
Con este comando se nos instala django para poder usar sus funcionalidades

Luego de que se instale , seguimos las siguientes lineas de comando
git clone https://github.com/JuanPadillax/RedSocialEV4.git

cd RedSocialEV4

python manage.py runserver

Abrimos la direccion ip que nos entrega y ya tendriamos activo el proyecto.

Descripción de los modelos

Usuario:
username: Nombre de usuario
email: Correo electrónico
password: Contraseña del usuario

Destino:
pais: Nombre del país
ciudad: Nombre de la ciudad.
descripcion: Breve descripcion del destino

Publicacion:
usuario: Clave foranea del modelo usuario
destino: Clave foranea del modelo Destino
texto: Descripción de la experiencia
fecha: Fecha de publicación de la experiencia

Ejemplos de uso de la API
![image](https://github.com/user-attachments/assets/96fa1c21-852a-4f44-95f9-3286c522cce7)



