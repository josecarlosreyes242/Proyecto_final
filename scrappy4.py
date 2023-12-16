from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import pandasql as psql
import time
import datetime

# Configuración del WebDriver
s = Service('/Users/nico/Documents/datosfinal/chromedriver')
driver = webdriver.Chrome(service=s)

# Función para realizar scraping, adaptada para incluir los datos requeridos
def scrape_website(url, curso_selector, titulo_selector, descripcion_selector, precio_selector, estrellas_selector, autoservicio):
    driver.get(url)
    time.sleep(5)  # Espera para que la página cargue completamente

    cursos = driver.find_elements(By.CSS_SELECTOR, curso_selector)
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    data = []
    for curso in cursos:
        titulo = curso.find_element(By.CSS_SELECTOR, titulo_selector).text if curso.find_elements(By.CSS_SELECTOR, titulo_selector) else "No disponible"
        descripcion = curso.find_element(By.CSS_SELECTOR, descripcion_selector).text if curso.find_elements(By.CSS_SELECTOR, descripcion_selector) else "No disponible"
        precio = curso.find_element(By.CSS_SELECTOR, precio_selector).text if curso.find_elements(By.CSS_SELECTOR, precio_selector) else "No disponible"
        estrellas = curso.find_element(By.CSS_SELECTOR, estrellas_selector).text if curso.find_elements(By.CSS_SELECTOR, estrellas_selector) else "No disponible"
        
        data.append([fecha_actual, autoservicio, titulo, descripcion, precio, estrellas])

    return pd.DataFrame(data, columns=['Fecha', 'Autoservicio', 'Producto/Marca', 'Nombre', 'Precio original', 'Estrellas'])

# Realizar scraping de cada sitio web
df_domestika = scrape_website('https://www.domestika.org/es/courses/search/inteligencia%20artificial', '.WrapperCard', 'h3', 'h4', 'span.Button-TextClass', 'span[class*="RatingClass"]', 'Domestika')
df_coursera = scrape_website('https://www.coursera.org/search?query=inteligencia%20artificial&', '.cds-ProductCard-base', 'h3.cds-CommonCard-title', 'p.cds-119.cds-Typography-base', 'span.cds-119.cds-Typography-base', 'div.product-reviews p.cds-119', 'Coursera')
df_udemy = scrape_website('https://www.udemy.com/courses/search/?q=inteligencia+artificial&src=sac&kw=inteligencia', '.course-card-module--container--2MTsr', 'h3[data-purpose="course-title-url"]', 'p[data-purpose="safely-set-inner-html:course-card:course-headline"]', '.price-text--price-part--2npPm', '.star-rating-module--rating-number--2xeHu', 'Udemy')

# Cerrar el navegador
driver.quit()

# Combinar los DataFrames
df_combined = pd.concat([df_domestika, df_coursera, df_udemy])

# Guardar los datos en un archivo CSV
df_combined.to_csv('datos_cursos.csv', index=False)

# Ejemplos de consultas SQL con pandasql
# Por ejemplo, seleccionar cursos de un sitio en particular
# Consulta para separar los cursos por categoría de precio
q3 = """
SELECT *, 
       CASE 
           WHEN `Precio original` = 'Free' THEN 'Gratis' 
           WHEN `Precio original` = 'No disponible' THEN 'Precio no disponible' 
           ELSE 'De pago' 
       END as CategoriaPrecio
FROM df_combined
"""
df_query3 = psql.sqldf(q3, locals())

# Consulta para encontrar el curso con la calificación más alta en cada plataforma
q4 = """
SELECT *, MAX(Estrellas) 
FROM df_combined 
GROUP BY Autoservicio
"""
df_query4 = psql.sqldf(q4, locals())

# Consulta para listar cursos con un enfoque específico, por ejemplo, "Machine Learning"
q5 = """
SELECT * 
FROM df_combined 
WHERE Nombre LIKE '%Machine Learning%'
"""
df_query5 = psql.sqldf(q5, locals())


# Consulta para cursos lanzados recientemente con alta calificación
q6 = """
SELECT * 
FROM df_combined 
WHERE Fecha >= '2023-01-01' AND Estrellas >= '4.5'
ORDER BY Fecha DESC
"""
df_query6 = psql.sqldf(q6, locals())

# Imprimir resultados de las consultas
print("Consulta 1: Cursos por categoría de precio")
print(df_query3)
print("\nConsulta 2: Curso con la calificación más alta en cada plataforma")
print(df_query4)
print("\nConsulta 3: Cursos con enfoque en 'Machine Learning'")
print(df_query5)
print("\nConsulta 4: Cursos lanzados recientemente con alta calificación")
print(df_query6)




print("Scraping completado, datos guardados y consultas SQL realizadas.")
