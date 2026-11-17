# Portfolio personal — Sergio Rodríguez Geniz

Este repositorio contiene el código de mi sitio profesional: [sergiorg03.github.io](https://sergiorg03.github.io/). Lo mantengo para presentar mi trayectoria, las tecnologías con las que trabajo y los proyectos que he hecho hasta ahora.

La página está pensada como una terminal. Fondo oscuro, texto en un solo color y secciones que se leen como si fueran la salida de un comando. Quería un sitio ligero, fácil de recorrer y distinto de una plantilla genérica, sin depender de un framework.

## Sobre mí

Soy Sergio Rodríguez Geniz, desarrollador backend, titulado en Desarrollo de Aplicaciones Multiplataforma por el IES Velázquez (Sevilla).

En 2023 trabajé como becario de software en Accenture Spain, con Salesforce y Apex, analizando y resolviendo incidencias de la aplicación de producción. Después completé el Máster en Desarrollo de Aplicaciones en Lenguaje Python, centrado en Django, FastAPI, IA Generativa y análisis de datos.

Tengo el C1 de inglés acreditado por la Escuela Oficial de Idiomas de Sevilla y estoy cursando el C2. Actualmente resido en Sevilla. Puedo trabajar en presencial, en híbrido o en remoto, y tengo disponibilidad para moverme geograficamente.

## Tecnologías

La interfaz no usa frameworks. El peso está repartido así:

- HTML para la estructura de `index.html` y `projects.html`.
- CSS escrito a mano en [style/style.css](style/style.css), con JetBrains Mono como tipografía.
- JavaScript en [scripts/script.js](scripts/script.js) para el cursor, la aparición de las secciones al hacer scroll y las barras de competencias.

El formulario de la página de proyectos está en [scripts/projects.js](scripts/projects.js). El calendario de GitHub se dibuja desde [scripts/github-calendar.js](scripts/github-calendar.js).

### Aspecto de la página

El fondo combina una rejilla con una capa de grano, al estilo de un monitor antiguo. El cursor es un punto con un anillo que lo sigue y crece al pasar sobre un enlace. Las barras de competencias y sus porcentajes se animan cuando la sección entra en pantalla, con `IntersectionObserver`. Los enlaces internos dejan un margen superior para no quedar ocultos detrás de la barra de navegación, que permanece fija.

## Qué podemos encontrar en la página

- La página principal reúne la presentación, el perfil, las competencias, el calendario de GitHub, la trayectoria y el contacto.
- [projects.html](projects.html) lista los proyectos. Ahora mismo están este portfolio y [LegalLens](https://github.com/sergiorg03/LegalLens), una aplicación para revisar contratos en PDF con Django, FastAPI, Docker y Nginx. En esa misma página hay un formulario por si alguien quiere proponerme un trabajo.
- El currículum se descarga en PDF desde la página principal: [docs/cv_srg_es.pdf](docs/cv_srg_es.pdf). En `docs/` también está la versión en inglés.
- El calendario de contribuciones no consulta GitHub desde el navegador. Cada día, el flujo de [.github/workflows/update-contributions.yml](.github/workflows/update-contributions.yml) ejecuta [python/update_contributions.py](python/update_contributions.py), guarda el resultado en `data/github-contributions.json` y la página lee ese archivo. El token de la API está guardado como secreto del repositorio.
- HTML, estilos y scripts van en carpetas distintas. [sitemap.xml](sitemap.xml) está publicado para que los buscadores indexen el sitio.

## Estructura del proyecto

```text
.
├── .github/workflows/   Actualización diaria de las contribuciones
├── data/                JSON con las contribuciones de GitHub
├── docs/                Currículum en PDF (español e inglés)
├── img/                 Fotografía de perfil, usada también como favicon
├── python/              Consulta a la API de GitHub
├── scripts/             JavaScript de la página
├── style/               Hoja de estilos
├── index.html           Página principal
├── projects.html        Proyectos y formulario
├── sitemap.xml
└── README.md
```

## Contacto

- Correo: [sergiorodriguezprofesional@gmail.com](mailto:sergiorodriguezprofesional@gmail.com)
- LinkedIn: [Sergio Rodríguez Geniz](https://www.linkedin.com/in/sergio-rodríguez-geniz-4530902a7)
- GitHub: [@sergiorg03](https://github.com/sergiorg03)
