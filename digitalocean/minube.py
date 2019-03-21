import os
import digitalocean

MI_TOKEN = os.environ["MI_TOKEN"]
N_MAQUINAS = 5

manager = digitalocean.Manager(token=MI_TOKEN)
claves_ssh = manager.get_all_sshkeys()

for maquina in range(N_MAQUINAS):
    maquina_nueva = digitalocean.Droplet(
        token=MI_TOKEN,
        name="maquina" + str(maquina),
        region="ams3",
        image="fedora-28-x64",
        size="s-1vcpu-1gb",
        ssh_keys=claves_ssh,
        backups=False
    )
    maquina_nueva.create()

for maquina in manager.get_all_droplets():
    maquina.load()
    print(maquina.ip_address)
