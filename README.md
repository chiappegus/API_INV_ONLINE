# Cartera en InvertirOnline

## Requisitos de Instalación

Antes de ejecutar el código, necesitas instalar los siguientes paquetes de Python. Puedes hacerlo fácilmente utilizando el archivo `requirements.txt`. Para instalar las dependencias, ejecuta el siguiente comando en tu terminal:

```sh
pip install -r requirements.txt

```
## Configuración de Credenciales

Para interactuar con la plataforma de InvertirOnline, necesitas proporcionar tus credenciales. Crea un archivo llamado config.py en el mismo directorio que el código principal y añade tus credenciales de la siguiente manera:

```sh
# config.py
USERNAME = "tu_usuario"
PASSWORD = "tu_contraseña"
```

Descripción del Código

El código proporcionado se conecta a la plataforma de InvertirOnline, extrae datos de tu portafolio y genera varios gráficos para visualizar la información de tus inversiones.
Pasos del Código

    Importación de Módulos: Se importan los módulos necesarios para la ejecución del código: pandas, ipywidgets, matplotlib, numpy y config.

Ejecución del Script Principal: Se ejecuta el script mainapi.py que se supone contiene la lógica para conectarse a la API de InvertirOnline y extraer el portafolio.

Extracción de Datos: Se extraen los datos del portafolio y se almacenan en un diccionario.

Creación del DataFrame: Los datos del diccionario se convierten en un DataFrame de pandas para facilitar su manipulación.

Filtrado de Datos: Se filtran los datos para excluir ciertos tipos de activos, en este caso, los 'TitulosPublicos'.

Generación de Gráficos: Se crean varios gráficos de torta y un gráfico de barras para visualizar diferentes aspectos de las inversiones.
