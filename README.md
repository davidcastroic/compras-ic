
# Bienvenido a tu primer Hola Mundo en App Engine

## Este código realiza un despliegue de un "Hola Mundo" en App Engine en su versión Standard.

## Mientras este proyecto no tenga un trafico que supere el Free Trier de Google App Engine, esta aplicación no generará ningun cargo a tu cuenta de Billing.   Más información aquí -> [link](https://cloud.google.com/free/)

### Clona este Repo, configura y personaliza tu propio Hola Mundo:


1. Crea una cuenta en GCP y activa el billing de dicha cuenta. Si es tu primera cuenta con GCP obtenras 300 USD gratis para hacer uso de la plataforma y sus servicios.

Crea tu cuenta aquí -> [link](https://console.cloud.google.com/)

2. Crea tu primer proyecto en GCP y obten el project ID.

2. Descarga e instala el Google Cloud SDK para tener acceso a las herramientas que te permitirán desplegar tu Hola Mundo.

Más información aquí -> [link](https://cloud.google.com/sdk/)

3. Abre tu linea de comandos preferida y has login con tu cuenta en GCP, corriendo el siguiente comando:
```shell
gcloud auth login
```

4. Configura el proyecto en el que vas a trabajar, utilizando el project ID que obtuvimos en el paso 2.
```shell
gcloud config set project "projectID"
```

5. Colocate al mismo nivel en donde se encuentra el archivo "app.yaml"

6. Realiza el despliegue de tu Hola Mundo con:
```shell
gcloud app deploy
```

7. Ahora en tu navegador coloca la dirección "projectID".appspot.com y observa tu primer hola mundo.
(Recuerda remplazar projectID por el ID de tu proyecto actual)

### ¡Felicidades!
## Acabas de desplegar tu Hola Mundo en la WEB haciendo uso de Google App Engine
