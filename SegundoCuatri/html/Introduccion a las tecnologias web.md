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

    

- **Etiqueta !DOCTYPE html:** Le va a indicar al navegador que el documento es de tipo HTML5.
- **Etiqueta html:** Es la raiz del documento HTML. Todo el contenido debe estar dentro de esta etiqueta.
- **Atributo lang="es":** Indica el idioma principal del contenido del documento, en este caso, español
- **Seccion head:** Contiene metadatos sobre el documento.
- **Meta etiqueta charset= "UTF-8":** Define el conjunto de caracteres utilizado en el documento.UTF-8 es una codificación de caracteres ampliamente utilizada.
- **Meta etiqueta viewport:** Configura cómo se debe mostrar la página en dispositivos móviles. width=device-width hace que el ancho de la página sea igual al ancho de la pantalla del dispositivo, y initial-scale=1.0 establece el nivel de zoom inicial.
- Etiqueta title: Define el título de la página que aparece en la pestaña del navegador y en los resultados de búsqueda.
- **Sección body:** Contiene todo el contenido visible de la página web, como texto, imágenes, videos, enlaces, etc.
- **Etiqueta h1:** Representa el encabezado principal de la página. Es el título más importante y generalmente se utiliza una sola vez por página.
- **Etiqueta p:** Define un párrafo de texto. Es una de las etiquetas más comunes para mostrar bloques de texto.


## 2.  Etiquetas HTML:

**¿Qué son las etiquetas en HTML y cómo se utilizan?**
 Una etiqueta HTML está compuesta por un nombre de etiqueta encerrado entre corchetes angulares (< >). La mayoría de las etiquetas vienen en pares: una etiqueta de apertura y una etiqueta de cierre, con el contenido entre ellas.

 **Como se utilizan las etiquetas:**
 - **Etiqueta de apertura:** indica el inicio de un elemento HTML
 - **Etiqueta de cierre:** La etiqueta de cierre marca el final del elemento HTML. Es similar a la etiqueta de apertura, pero con una barra inclinada.
 - **Contenido entre las etiquetas:** Entre la etiqueta de apertura y la de cierre, se coloca el contenido que se desea mostrar o estructurar en la página.
 - **Etiquetas auto-cerradas:** Algunas etiquetas no requieren un par de cierre porque no contienen contenido entre ellas. Estas se denominan etiquetas auto-cerradas y suelen incluir una barra inclinada antes del cierre del corchete angular.
 - **Atributos en las etiquetas:** Las etiquetas HTML también pueden tener atributos, que proporcionan información adicional sobre el elemento

**Menciona y describe brevemente al menos cinco etiquetas comunes en HTML.**
- **`<h1> a <h6>`:** Estas etiquetas se utilizan para definir encabezados o títulos en una página web. `<h1>` es el nivel mas importante y suele usarse para el titulo principal, a su vez `<h6>` es el nivel menos importante.
- **`<p>`:** Define un párrafo de texto.
- **`<a>`:** Crea un enlace a otra página. El atributo `href` especifica la URL del destino.
- **`<div>`:** Define una sección o un contenedor en un documento. Se utiliza para agrupar contenido, es un elemento de bloque.
- **`<img>`:** Se usa para insertar imágenes en una página web. Los atributos comunes incluyen `src` (es la fuente de la imagen) y `alt` (describe la imagen).

## 3. Atributos HTML:
**¿Qué son los atributos en HTML y para qué se utilizan?**
Los atributos en HTML son componentes adicionales que se agregan a las etiquetas HTML para proporcionar informacion y controlar su comportamiento o apariencia.

**Se utilizan para:**
- Proporcionar Información Adicional
- Modificar el Comportamiento de un Elemento
- Definir Características Visuales
- Identificación y Referencia
- Accesibilidad

**Da un ejemplo de una etiqueta HTML con atributos y explica su función**
   `<a href="https://www.paginaejemplo.com" target="_blank" title="Pagina">Pagina</a>`

- **Etiqueta `<a>`:** Es la etiqueta que define un hipervínculo o enlace en HTML. El contenido entre la etiqueta de apertura `<a>` y la etiqueta de cierre `</a>` se muestra como un enlace.

**Atributos:**
- **`href="https://www.paginaejemplo.com"`:** Especifica la URL a la que se dirige el enlace.
- **`target="_blank"`:**  Indica cómo se debe abrir el enlace. El valor `_blank` indica que el enlace se abrirá en una nueva pestaña o ventana del navegador.
- **`title="Pagina"`:**  Proporciona una breve descripción emergente que puede ayudar al usuario a entender mejor el propósito del enlace antes de hacer clic en él.


## Unidad 3: CSS3

## Definición y Uso de CSS:
**¿Qué es CSS y cuál es su papel en el diseño de páginas web?**

CSS(Cascading style sheets) s un lenguaje utilizado para describir la presentación visual de un documento HTML. Mientras que HTML se encarga de la estructura y el contenido de la página, CSS define como se mostraran esos elementos en termino de diseño, colores, fuentes, disposicion y espaciado.
