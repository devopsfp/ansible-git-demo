# Guión de despliegue automatizado de servidores web en la nube

## Presentación inicial y puesta en contexto
* Hemos desplegado N servidores, y ahora toca configurarlos

* Plantear las distintas opciones
  * Enfoque tradicional: Entrar máquina a máquina
    * Editar los ficheros de configuración de apache
    * Descargar contenido a servir en cada servidor web
    * Microgestión por SSH
    * Requiere la atención total del administrador de sistemas
  * Automatización tradicional
    * Programar un script que automatice la configuración
    * Desarrollar los scripts lleva tiempo
    * Los scripts son muy sensibles a diferencias entre las máquinas
    * Ejecutar los scripts se hace de uno en uno por cada máquina
  * Situación ideal
    * Definir la configuración que tiene que tener el servidor
    * Aplicarla de un plumazo a todos los servidores
    * Que si algo ya está configurado se adapte y lo ignore
    * Que el estado final de la aplicación de la configuración deje todos los servidores en el mismo estado y no tener servidores con distintas configuraciones
    * Esto se llama: Gestión de configuración
* Conceptos básicos de gestión de la configuración
  * Recetas declarativas
  * Automatización de aplicación de las recetas
  * Idempotencia
  * La configuración se convierte en código

## Ansible

* Presentación de Ansible
* Ansible como herramienta para gestión de la configuración
* Principales características
* Requisitos para usar ansible
* ¿Cómo funciona?
* Conceptos de Ansible
  * Instalación
  * Comandos básicos
  * Módulos
  * Inventarios
  * Playbooks (recetas)

## Videos

* Instalación de ansible (sudo pip install ansible)
* Ejecución de ansible en la máquina local
  * Ejecución de un comando en máquina local
  * Ejecución de un módulo ansible en máquina local
* Ejecución de ansible en máquinas remotas
  * Crear una máquina nueva en DigitalOcean
  * Crear un inventario con la nueva máquina
    * maquina1 ansible_host=104.248.87.200 ansible_user=root ansible_python_interpreter=python3
  * Ejecutar un comando en máquina remota
    * ansible -i inventario -a "uname -a" maquina1
  * Ejecutar un módulo de ansible en máquina remota
    * ansible -i inventario -m ping maquina1
* Creación de un playbook simple
  * Añadir al playbook el módulo ping
  * Ejecución del playbook en máquina remota
  * Lectura de la salida
  * Introducción de error deliberado
    * Intentar iniciar un servicio que no está instalado
  * Ejecución del playbook en máquina remota
  * Lectura de la salida
* Creación de un playbook para desplegar servidor web
  * Instalación del paquete de Apache
  * Ejecutar el playbook
  * Lectura de la salida
  * Activación del servicio de Apache
  * Ejecutar el playbook
  * Lectura de la salida
    * Recalcar que la instalación del paquete ya estaba hecha
  * Comprobar que el servidor web está activo
* Añadir contenido al servidor web
  * Editar fichero PHP <?php phpinfo(); ?>
  * Añadir al playbook la copia de la configuración
  * Añadir al playbook la copia del contenido
  * Ejecutar playbook
  * El servidor no mostrará el fichero PHP porque no tenemos PHP instalado
* Instalar PHP en el servidor
  * Añadir al playbook instalación de paquete php
  * Modificar activación de Apache para que reinicie el servicio
  * Ejecutar playbook
  * El servidor web mostrará el fichero PHP

* Ejecución de playbook en el inventario generado por el script de dígital ocean de Alberto
  * Generar un inventario con el script de creación de varias máquinas
  * Ejecutar playbook del servidor web en dicho inventario
  * Lectura de la salida
  * Comprobación de los distintos servidores