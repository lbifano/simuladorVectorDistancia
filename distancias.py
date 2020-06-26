import json
import math
from pprint import pprint

with open('datos.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

nodos = {}
for nodoa in obj['nodos']:
    for nodob in obj['nodos']:
        if nodoa['nombre'] != nodob['nombre']:
            distancia=round(math.sqrt(math.pow(nodob['posicion-x']-nodoa['posicion-x'],2)+math.pow(nodob['posicion-y']-nodoa['posicion-y'],2)),2)
            if distancia < nodoa['rango-maximo'] and distancia < nodob['rango-maximo']:
                nodoa['vecinos'][nodob['nombre']]=distancia    
    nodos[nodoa['nombre']]=nodoa

def propagar(destino,ps,nodos,distancia):
    for vecino in nodos[ps]['vecinos']:
        if vecino != destino:
            if destino in nodos[vecino]['rutas']:
                if nodos[vecino]['rutas'][destino]['distancia'] > distancia:
                    nodos[vecino]['rutas'][destino]['distancia']=distancia
                    nodos[vecino]['rutas'][destino]['proximo_salto']=ps
            else:
                ruta = {}
                ruta['proximo_salto']=ps
                ruta['distancia']=distancia
                nodos[vecino]['rutas'][destino]=ruta                
                propagar(destino,vecino,nodos,distancia+1)

for i in nodos:    
    propagar(i,i,nodos,1)
pprint(nodos)