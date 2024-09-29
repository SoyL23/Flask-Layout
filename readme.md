Flask-Layout

    Plantilla de Aplicación de Backend con Arquitectura Limpia para Flask
    Esta plantilla es orientada a objetos.

Resumen

    Flask-Layout es una plantilla de aplicación de backend para Flask que sigue un patrón de arquitectura limpia. Proporciona una base sólida para construir aplicaciones backend escalables y mantenibles.

Estructura de Directorios

    El proyecto se organiza en los siguientes directorios:

        config: Archivos de configuración para la aplicación
        controllers: Controladores que manejan solicitudes entrantes y interactúan con servicios
        dao: Objetos de Acceso a Datos que encapsulan interacciones con la base de datos
        dto: Objetos de Transferencia de Datos que definen la estructura de datos intercambiados entre capas
        interfaces: Definiciones de interfaz para servicios y repositorios
        models: Modelos de base de datos que definen la estructura de datos almacenados en la base de datos
        routes: Definiciones de rutas para la aplicación
        services: Servicios de lógica empresarial que interactúan con controladores y repositorios
        utils: Funciones y clases de utilidad que se pueden utilizar en toda la aplicación

Archivos Principales

    app.py: Configura la aplicación de Flask
    index.py: Inicia la aplicación
    main.py: Conecta a la base de datos y configura la aplicación

CRUD de Usuario

    La plantilla incluye un CRUD (Crear, Leer, Actualizar, Eliminar) de usuario, que permite administrar usuarios en la base de datos, por defecto esta configurada para trabajar con PostgreSQL, pero trabaja con SQLALCHEMY, así que
    es posible trabajar con cualquier gestor que admita la libreria.

Dependencias

    La plantilla utiliza las siguientes bibliotecas, que se encuentran en el archivo requirements.txt:

Comenzar

    Para comenzar con Flask-Layout, sigue estos pasos:

        Clona el repositorio: git clone https://github.com/SoyL23/Flask-Layout.git
        Crea un entorno virtual y asegurate que este activo.
        Instala las dependencias requeridas: pip install -r requirements.txt

        Configura la aplicación: Actualiza las variables de entorno

        Inicia la aplicación: python index.py

Contribuir

    Las contribuciones a Flask-Layout son bienvenidas. Si deseas contribuir, por favor bifurca el repositorio y envía una solicitud de pull.
