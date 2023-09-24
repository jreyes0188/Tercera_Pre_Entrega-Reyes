# Tercera_Pre_Entrega-Reyes
Python+Django

Pasos para utilizar la pagina y la base de datos

- Correr el servidor con el comando = python manage.py runserver
- Podremos ver que los templates HTML se estan heredando ya que podemos desplazarnos uno por uno (Hacer click en las vistas de la barra de navegacion)
- Se simulo un ecommerce de un local de ventas de cafe y comida
- En la Pagina de inicio podemos ver el titulo mas el logo del ecommerce

  AGREGAR PRODCUTOS DESDE LA WEB A LA BD
  
- En las pestaña de Cafe Caliente, Cafe Frio y Comida tenemos los respectivos formularios para agregar productos a la base de datos (rellenamos la informacion y hacemos click en Enviar)
- Hacemos la prueba rellenando cualquier o todos los formularios con la informacion que corresponda depende de la vista donde nos encontremos en la web
- Dejamos de correr el servidor haciendo Ctrl + C
- Despues creamos un usuario y contraseña para poder acceder a la base de datos con el comando ---> python manage.py createsuperuser
- Volvemos a correr el servidor = python manage.py runserver
- Accedemos a la base de datos con la url ---> http://127.0.0.1:8000/admin
- Y colocamos el usuario y la contraseña
- Al ingresar a la base de datos observaremos en nuestros productos (Cafe Caliente, Cafe Frio, Comida)
- Al hacer click en cualquiera de ella vamos a observar que estan guardados los productos que agregamos en nuestro formulario en la pagina web

  BUSQUEDA DE LOS PRODCUTOS DESDE LA WEB
  
- Para buscar los productos agregados, nos dirigimos a cualquiera de las pestañas (Cafe Caliente, Cafe Frio, Comida)
- En la parte de abajo observaremos un formulario o filtro para buscar los productos que agregamos a la base de datos anteriormente
- Colocamos el nombre del producto que almacenamos en la BD y hacemos click en "Buscar"
- El resultado sera el nombre del producto mas el precio
