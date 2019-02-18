import os
import digitalocean

# Guardamos el valor de la variable de entorno MI_TOKEN para acceder a la API
MI_TOKEN = os.environ["MI_TOKEN"]

manager = digitalocean.Manager(token=MI_TOKEN)

for maquina in manager.get_all_droplets():
    maquina.destroy()
