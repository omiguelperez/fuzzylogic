import json

inputs = json.loads(open('resources/inputs.json').read())['inputs']
outputs = json.loads(open('resources/outputs.json').read())['outputs']


def get_quality(quality_value, output):
    """Este metodo en teoria debe generar una etiqueda linguistica de salida."""
    tags = output['universo']['etiquetas']
    for tag in tags:
        if quality_value >= tag['minimo'] and quality_value < tag['maximo'] and tag['maximo'] != 100:
            return tag['nombre']
    return tags[len(tags) - 1]['nombre']


message_format = 'SI {} es {}, {} es {} e {} es {} ENTONCES {} es '
rules = []


def generate_rules_system():
    """Genera el sistema de reglas base del problema."""
    print('\n SISTEMA DE REGLAS BASE (LISTO PARA LLENAR)\n')
    for humedad in inputs[0]['universo']['etiquetas']:
        for grano_partido in inputs[1]['universo']['etiquetas']:
            for impureza in inputs[2]['universo']['etiquetas']:
                rule = message_format.format(
                    inputs[0]['nombre'], humedad['nombre'],
                    inputs[1]['nombre'], grano_partido['nombre'],
                    inputs[2]['nombre'], impureza['nombre'],
                    outputs[0]['nombre']
                )
                rules.append(rule)
                print(rule)
    print('\n%s reglas en el sistema.' % len(rules))


"""Iniciar programa principal si es main."""
if __name__ == '__main__':
    generate_rules_system()
