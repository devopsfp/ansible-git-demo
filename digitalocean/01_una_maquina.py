import os
import digitalocean

# Guardamos el valor de la variable de entorno MI_TOKEN para acceder a la API
MI_TOKEN = os.environ["MI_TOKEN"]

# Gestor global para acciones generales como listar maquinas o claves SSH
manager = digitalocean.Manager(token=MI_TOKEN)

# Guardar una lista con todas las claves SSH disponibles en nuestra cuenta
claves_ssh = manager.get_all_sshkeys()

maquina1 = digitalocean.Droplet(
  token=MI_TOKEN,
  name='maquina1',
  region='ams3',
  image='fedora-28-x64',
  size='s-1vcpu-1gb',
  ssh_keys=claves_ssh,
  backups=False
)
maquina1.create()
