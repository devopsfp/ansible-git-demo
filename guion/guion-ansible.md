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

* Ejecución de un comando en máquina remota
* Ejecución de un módulo ansible en máquina remota
* Creación de un playbook simple
* Ejecución del playbook en máquina remota
* Lectura de la salida
* Introducción de error deliberado
* Ejecución del playbook en máquina remota
* Lectura de la salida
* Creación de un playbook para desplegar servidor web
* Ejecución del playbook en máquina remota
* Ejecución de playbook en el inventario generado por el script de dígital ocean de Alberto
* Lectura de la salida
* Comprobación de los distintos servidores
* Paso la parte de balanceador de carga