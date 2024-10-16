# Instrucciones para usar el proyecto

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Configuración del entorno

1. Clona el repositorio en tu máquina local:

    ```sh
    git clone https://github.com/Bjohan23/API-REST-PIZA4.git
    cd API-REST-PIZA4
    ```

2. Crea un entorno virtual:

    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:

        ```sh
        source venv/Scripts/activate
        ```

        > **Nota:** Si el comando `source venv/Scripts/activate` no funciona, puedes intentar con el siguiente:
        >
        > ```cmd
        > .\venv\Scripts\activate
        >

    - En macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Instala las dependencias del proyecto:

    ```sh
    pip install -r requirements.txt
    ```

5. Configura las variables de entorno:

    - Crea un archivo [`.env`]
    añade las variables necesarias. Puedes usar el archivo `.env.example` como referencia si está disponible.

6. Ejecuta la aplicación:

    ```sh
    python run.py
    ```

## Desactivar el entorno virtual

Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual con el siguiente comando:

```sh
deactivate
```

## Crear archivo requeriments.txt

Si deseas modificar el proyecto y has agregado nuevos paquetes, genera el archivo `requirements.txt` con el siguiente comando:

```sh
   pip freeze > requirements.txt
```
