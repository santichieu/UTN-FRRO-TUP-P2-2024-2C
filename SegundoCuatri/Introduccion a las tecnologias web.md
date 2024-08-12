# Introduccion a las tecnologias web

## 1. •	¿Qué es Internet y cuál es su importancia en la infraestructura de la Web?

- Internet es un conjunto descentralizado de comunicaciones interconectadas, que utilizan protocolos TCP/IP. Es una red de computadoras interconectadas entre si a nivel mundial con el objetivo de hacer común información de acceso público.

- La importancia del internet en la infraestructura de la web es la de interconectar globalmente redes y dispositivos en todo el mundo, proporcionar acceso a información y recursos, facilitación de aprendizaje y educación a distancia y recursos para realizar capacitaciones
**•	Describe brevemente la evolución de ARPANET a Internet.**

- **ARPANET** fue la primera red de computadoras, creada en 1969 por el Departamento de Defensa de EE. UU. para conectar centros de investigación.
- Introdujo tecnologías clave como el conmutado de paquetes y el protocolo TCP/IP, que permitieron la interconexión de diferentes redes.
- En 1983, ARPANET adoptó TCP/IP, sentando las bases para Internet.
- ARPANET fue desmantelada en 1990.

## 2. Protocolos de Comunicación

**Explica la función del protocolo TCP/IP en Internet.**

TCP e IP son protocolos separados que trabajan juntos para garantizar que los datos se entreguen a su destino previsto dentro de una red

**¿Qué es una dirección IP y cuál es la diferencia entre una IP pública y una privada?**

 - Una dirección ip es una dirección única que identifica a un dispositivo en internet o en una red local.

- Una dirección IP privada se utiliza dentro de una red privada para conectarse de forma segura a otros dispositivos dentro de esa misma red. Una dirección IP pública te identifica ante el resto de Internet para que toda la información que buscas pueda encontrarte.


## 3. Infraestructura de Internet

**¿Qué elementos componen la infraestructura de comunicación de Internet?**

- Los elementos que componen una infraestructura en internet son los centros de datos, servidores, dispositivos de almacenamiento, routers, cables, repetidores, módems, satélites, antenas y cables submarinos





**Menciona y explica brevemente el rol de los satélites, antenas y cables submarinos en Internet.**

-	**Satélites:** Los satélites en orbita de la tierra permiten la comunicación y transmisión de entre puntos distantes, especialmente en áreas remotas donde la infraestructura terrestre es inexistente. Los satélites reciben señales de una extracción terrestre y las retrasmiten a otra estación terrestre.

-	**Antenas:** Las antenas son dispositivos que transmiten y reciben señales de radiofrecuencia, permitiendo la conexión inalámbrica a Internet. Son utilizados en redes wifi, celulares y otras formas de comunicación inalámbrica

-	**Cables submarinos:** Los cables submarinos son el medio principal para la transmisión de datos a través de océanos o grandes cuerpos de agua, conectando continentes y facilitando datos a gran velocidad, son cables de fibra ópticas, tendidos por el lecho marino que transportan la mayoría del trafico de datos a nivel internacional, permitiendo una comunicación rápida y eficiente entre diferentes partes del mundo.

## 4. Conceptos Básicos de la Web

**Define y explica la importancia de los siguientes términos: HTML, URL, y HTTP/HTTPS.**

-    **HTML (lenguaje de Marcas de Hipertexto):**  Es el componente más básico de la web, define el significado y la estructura del contenido web, generalmente se utilizan otras tecnologías para describir la apariencia (CSS) o la funcionalidad/comportamiento (JavaScript). La importancia de HTML es su estructuración, accesibilidad, interoperabilidad.

-   **URL (Uniform Resoursce Locator):** Una URL es la dirección específica de un recurso en Internet. Indica la ubicación exacta de una página web, un archivo o un servicio en la web. La importancia de las URL son la de acceso a recursos, navegación web, redireccionamiento y enlaces y SEO(optimización para motores de búsqueda)

-    **HTTP/HTTPS (HyperText Transfer Protocol/ HyperText Transfer Protocol Secure):**
HTTP es un protocolo de comunicación usado para transferir datos en la web, HTTPS es una versión segura de HTTP que utiliza un cifrado SSL/TLS (Secure Sockets Layer/Transport Layer Security) para proteger la transmisión de datos entre el navegador y el servidor web. La importancia de HTTP/HTTPS es su transferencia de datos, seguridad (en el caso de HTTPS), rendimiento.

**¿Cuál es la relación entre Internet y la Web?**

Internet es una inmensa red de computadoras interconectadas entre si alrededor de todo el mundo, en cambio la web es una enorme colección de paginas que se asienta sobre esa red de computadores, es decir que cuando navegas desde tu computadora o celular usas internet para acceder a la web.



## UNIDAD 2: HTML 5

## 1. Estructura de HTML:
**¿Qué es HTML y cuál es su propósito principal en la Web?**
- El Lenguaje de Marcado de Hipertexto (HTML) es el código que se utiliza para estructurar y desplegar una página web y sus contenidos.

**Escribe una estructura básica de un documento HTML y explica cada una de sus partes principales.**

    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Título de la página</title>
    </head>
    <body>
        <h1>Encabezado principal</h1>
        <p>Este es un párrafo de ejemplo.</p>
    </body>
    </html>

-       <!DOCTYPE html>:
- **Doctype:** Define el tipo de documento y la versión de HTML que se está utilizando. En este caso, <!DOCTYPE html> indica que el documento está escrito en HTML5.