import os
import digitalocean

# Guardamos el valor de la variable de entorno MI_TOKEN para acceder a la API
MI_TOKEN = os.environ["MI_TOKEN"]

manager = digitalocean.Manager(token=MI_TOKEN)

print("### CENTRO DE DATOS ####")
for region in manager.get_all_regions():
    print("id: '%s',\tpais: %s" % (region.slug, region.name))
print("### IMAGENES ###")
for image in manager.get_all_images():
    print("id: '%s',\tnombre: %s" % (image.slug, image.name))
print("### TIPOS DE VM ###")
for size in manager.get_all_sizes():
    print("id: '%s',\tvCPUS:\t%d,\tRAM:\t%dMB,\tSSD: %dGB" % (size.slug, size.vcpus, size.memory, size.disk))