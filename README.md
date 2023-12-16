## Final Proyect

## Descripción
Nuestro script es una herramienta de Python diseñada para realizar scraping de datos de cursos en línea en diferentes plataformas como Domestika, Coursera y Udemy. Utiliza Selenium para la automatización web y pandas para el manejo y análisis de datos.

## Características
- **Scraping Web**: Automatiza la navegación en páginas de cursos en línea para extraer información relevante como lo son el costo por el curso, el sitio web el cual se esta extrayendo la información (Página de cursos de la que se esta hablando:  Domestika, Coursera y Udemy) y la calificación que posee dicho curso. 
- **Análisis de Datos**: Utiliza pandas y pandasql para analizar y manipular los datos recopilados.
- **Generación de Reportes**: Produce un archivo CSV con los datos recopilados y realiza varias consultas SQL para el análisis. 

## Requisitos para su correcto funcionamiento
- Python 3.x
- Bibliotecas de Python: `selenium`, `pandas`, `pandasql`
- [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) compatible con tu versión de Google Chrome.

## Instalación de Dependencias
Instala las dependencias necesarias utilizando pip:
```
ie: pip install selenium pandas pandasql
```

## Funcionamiento del Script
El script realiza las siguientes operaciones:
1. Inicializa Selenium WebDriver.
2. Realiza scraping de sitios web específicos para cursos en línea.
3. Recopila datos como el título del curso, descripción, precio y calificaciones.
4. Combina y guarda los datos en un archivo CSV.
5. Realiza consultas SQL para analizar los datos.
6. Imprime los resultados de las consultas SQL.
