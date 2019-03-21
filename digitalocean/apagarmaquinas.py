import os
import digitalocean

MI_TOKEN = os.environ["MI_TOKEN"]

manager = digitalocean.Manager(token=MI_TOKEN)

for maquina in manager.get_all_droplets():
    maquina.destroy()
