# catalog-api
 
Api para el registro de productos de catálogo

## Tecnología usadas

-   **Python**: Lenguaje de programación principal del proyecto.
-   **FastAPI**: Framework web para construir APIs rápidas y eficientes.
-   **DynamoDB**: Base de datos NoSQL de AWS utilizada para el almacenamiento de datos.
-   **Arquitectura Hexagonal (Ports and Adapters)**: Diseño de arquitectura que permite mantener el núcleo de la aplicación independiente de los detalles externos.
-   **Inyección de Dependencias**: Patrón de diseño que facilita la gestión y el intercambio de dependencias.
-   **Patrón Repository**: Patrón de diseño que abstrae la capa de persistencia y permite un acceso más flexible a los datos.

### Estructura del Proyecto

El proyecto está estructurado de acuerdo a la arquitectura hexagonal, dividida en las siguientes capas:

1.  **Capa de Dominio**: Contiene las entidades y las reglas de negocio. Es el núcleo de la aplicación y no depende de otras capas.
2.  **Capa de Aplicación**: Contiene los casos de uso de la aplicación. Interactúa con la capa de dominio y define la lógica de la aplicación.
3.  **Capa de Infraestructura**: Contiene implementaciones de los adaptadores que interactúan con los detalles externos como la base de datos y los servicios externos.

### Beneficios de la Arquitectura

-   **Escalabilidad**: La separación clara de responsabilidades y la independencia del núcleo de la aplicación permiten escalar y modificar el sistema sin afectar otras partes.
-   **Cohesión y Bajo Acoplamiento**: Las dependencias están bien gestionadas y los componentes están altamente cohesionados, lo que facilita el mantenimiento y la evolución del sistema.
-   **Flexibilidad**: La inyección de dependencias y el patrón repository permiten cambiar implementaciones de la base de datos o de otros servicios sin modificar el código del núcleo de la aplicación.

### Ejecución del Proyecto

Para ejecutar el proyecto localmente:

1.  Clona el repositorio:
       
    ```bash
    git clone https://github.com/dbsiavichay/catalog-api.git
    cd catalog-api
    ```
    
2.  Construir la imagen docker:
     
	```bash
    docker compose build
    ```
    
3.  Ejecuta la aplicación:
    
    ```bash
    docker compose up -d
    ```
    
4.  Accede a la documentación interactiva de la API en:
    
    `http://127.0.0.1:3000/docs` 

### Registro de usuarios

Accede a `/register` para registrar un nuevo usuario, se debe enviar un correo y contraseña.
Para registrar un usuario administrador se debe hacer con los siguientes correos:

 - a@example.com
 - b@example.com
 - c@example.com
 - d@example.com

De momento los correos admins se definen en la configuración del proyecto, pero fácilmente se puede escalar a la forma tradicional de roles u otro mecanismo.
    
### Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio de GitHub para discutir cualquier cambio o mejora.