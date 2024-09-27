# Instrucciones para usar el proyecto

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Configuración del entorno

1. Clona el repositorio en tu máquina local:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
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

    - En macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Instala las dependencias del proyecto:

    ```sh
    pip install -r requirements.txt
    ```

5. Configura las variables de entorno:

    - Crea un archivo [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FAsus%2FOneDrive%20-%20Universidad%20Se%C3%B1or%20de%20Sip%C3%A1n%2F8%20CICLO%2FCALIDAD%20DE%20SOFTWARE%2FAPI-REST-2%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22db04f15c-95e3-4ed1-92f1-6ab29d3395ac%22%5D "c:\Users\Asus\OneDrive - Universidad Señor de Sipán\8 CICLO\CALIDAD DE SOFTWARE\API-REST-2\.env") en la raíz del proyecto y añade las variables necesarias. Puedes usar el archivo `.env.example` como referencia si está disponible.

6. Ejecuta la aplicación:

    ```sh
    python run.py
    ```

## Desactivar el entorno virtual

Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual con el siguiente comando:

```sh
deactivate