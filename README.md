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



Asi se ve el dato en la API


![image](https://github.com/user-attachments/assets/27d67961-856d-4c32-a792-5b837eb431ed)

Y asi se ve el funcionamiento en el sistema

![image](https://github.com/user-attachments/assets/6a1e7263-7b37-457a-b512-3232c571365a)




