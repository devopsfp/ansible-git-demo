<!-- $theme: default -->
<!-- $size: 16:9 -->
<!-- page_number: true -->

<center>

# Curso acelerado para la nube
## Configurando cientos de máquinas con Ansible

Oliver Gutiérrez Suárez

</center>

---

<center>

# Ya tengo máquinas "ilimitadas"


![Unlimited power](imagenes/unlimited_power.jpg)


## ¿Y ahora qué?

</center>

---

<center>

# Configurando a la vieja escuela

![Hackerman](imagenes/hackerman.jpg)

## Entramos al servidor por SSH y configuramos manualmente los servicios

</center>

---

![Skeleton](imagenes/skeleton.png)

---

<center>

# Automatización a la vieja escuela

![Grumpy sysadmin](imagenes/go_away_shell_script.jpg)

## ¡Hacemos un script que trabaje por nosotros!

</center>

---

<center>

![Ansible](imagenes/ansible.svg)

</center>

---

# ¿Qué es Ansible?

* Herramienta de gestión de configuración
    * *"Infrastructure as code"*, *DevOps*, etc.
* Únicos requisitos: Python y SSH
* No requiere instalación en las máquinas remotas
    * Casi todos los sistemas actuales incluyen Python y SSH

---

# Componentes de Ansible

* **Módulos**: Tareas que podemos ejecutar en las máquinas remotas
    * Existen miles de módulos y son parametrizables
* **Playbooks**
    * Describen una política, tarea o grupo de tareas a ejecutar
    * Diseñadas para ser leídas por personas
        * Se usa un lenguaje declarativo (YAML)
    * Idempotencia en múltiples ejecuciones

---

<center>

# ¡DEMO!

</center>

---

<center>

# ¡Gracias!

</center>

* Repositorio con código y diapositivas:
    * https://github.com/devopsfp/tutorial-nube
* Vídeo de la charla de introducción y administración automatizada
    * https://youtu.be/1-kzQ5bhc7I
* Vídeo de la charla de Ansible:
    * https://youtu.be/cqwQPXdqK8k
