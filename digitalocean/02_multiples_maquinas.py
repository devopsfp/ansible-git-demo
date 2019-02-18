import os
import digitalocean

# Guardamos el valor de la variable de entorno MI_TOKEN para acceder a la API
MI_TOKEN = os.environ["MI_TOKEN"]

REPLICAS = 5  # Numero de maquinas a crear

# Gestor global para acciones generales como listar maquinas o claves SSH
# disponibles
manager = digitalocean.Manager(token=MI_TOKEN)

# Guardar una lista con todas las claves SSH disponibles en nuestra cuenta
claves_ssh = manager.get_all_sshkeys()

# En lugar de crear una sola maquina, creamos un bucle creando maquinas identicas
for indice in range(REPLICAS):
  maquina = digitalocean.Droplet(
    token=MI_TOKEN,
    # Convertimos el indice en texto para que cada máquina se llame maquina0, maquina1, etc...
    name='maquina' + str(indice),
    region='ams3',
    image='fedora-28-x64',
    size='s-1vcpu-1gb',
    ssh_keys=claves_ssh,
    backups=False
  )
  maquina.create()
