# Orbit Viewer

Aplicación web para explorar y visualizar información de sistemas planetarios y exoplanetas a partir de un catálogo astronómico.

## Descripción

Orbit Viewer combina un frontend de visualización con una API REST desarrollada en Python y Flask. La aplicación permite consultar estrellas anfitrionas, sistemas planetarios y datos individuales de exoplanetas para representarlos posteriormente mediante una interfaz gráfica.

El backend utiliza **Pandas** para procesar el catálogo de datos y **Flask** para proporcionar los endpoints consumidos por el frontend. Se habilita **CORS** para facilitar la comunicación entre la interfaz web y la API.

## Estructura principal

```text
orbit-viewer/
├── api.py
├── data.py
├── exoplanets.js
├── head.html
├── intefaz.js
├── style.css
├── logo.jpg
├── visualizacionexoPLa.ipynb
├── PSCompPars_2024.09.30_17.09.44.csv
└── PSCompPars_2024.09.30_17.09.44.json
```

### Backend

- `api.py`: API REST encargada de consultar y filtrar el catálogo.
- `data.py`: herramienta auxiliar para analizar el catálogo y comprobar el rango de temperaturas estelares.

### Frontend

- `head.html`: estructura principal de la interfaz.
- `intefaz.js`: lógica de interacción de la interfaz.
- `exoplanets.js`: funciones relacionadas con la representación de los exoplanetas.
- `style.css`: estilos visuales.
- `logo.jpg`: recurso gráfico del proyecto.

### Datos y análisis

- `PSCompPars_2024.09.30_17.09.44.csv`: catálogo original en formato CSV.
- `PSCompPars_2024.09.30_17.09.44.json`: versión JSON Lines utilizada por la API.
- `visualizacionexoPLa.ipynb`: notebook utilizado para exploración o visualización de los datos.

## Tecnologías

- Python
- Flask
- Pandas
- Flask-CORS
- JavaScript
- HTML5
- CSS3
- Jupyter Notebook

## API

Los principales endpoints disponibles son:

| Endpoint | Función |
|---|---|
| `GET /api/hostnames` | Lista los nombres únicos de las estrellas anfitrionas. |
| `GET /api/solar-system-data` | Devuelve información básica de todos los sistemas. |
| `GET /api/solar-system/<hostname>` | Consulta los planetas asociados a una estrella. |
| `GET /api/planet-data/<pl_name>` | Obtiene información detallada de un planeta. |
| `GET /api/hostname-or-planet?hostname=...` | Busca información mediante el nombre de una estrella. |
| `GET /api/hostname-or-planet?plname=...` | Busca información mediante el nombre de un planeta. |

## Ejecución

Instala las dependencias necesarias:

```bash
pip install flask flask-cors pandas
```

Desde el directorio raíz del repositorio, ejecuta:

```bash
python orbit-viewer/api.py
```

La API se iniciará utilizando el servidor de desarrollo de Flask.

> **Nota:** `api.py` utiliza rutas relativas para localizar el archivo JSON. Por ello, debe ejecutarse desde el directorio raíz del proyecto o adaptarse la ruta del catálogo según la ubicación desde la que se ejecute.

## Objetivo del proyecto

El proyecto busca proporcionar una representación interactiva de sistemas planetarios utilizando datos astronómicos reales. La separación entre frontend, backend y datos permite consultar la información de manera estructurada y utilizarla posteriormente en diferentes componentes de visualización.

## Estado

Proyecto de visualización y exploración de datos astronómicos. La versión incluida en este repositorio corresponde al estado actual del desarrollo.
