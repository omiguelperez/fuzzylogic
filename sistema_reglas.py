import json
import pickle

inputs = json.loads(open('resources/inputs.json').read())['inputs']
outputs = json.loads(open('resources/outputs.json').read())['outputs']

message_format = 'SI {} es {}, {} es {}, {} es {}, {} es {} ENTONCES {} es '
rules = []


def generate_rules_system():
    """Genera el sistema de reglas base del problema."""
    print('\n SISTEMA DE REGLAS BASE (LISTO PARA LLENAR)\n')
    for velocidad in inputs[3]['universo']['etiquetas']:
        for estado in inputs[2]['universo']['etiquetas']:
            for trafico in inputs[1]['universo']['etiquetas']:
                for tipo_via in inputs[0]['universo']['etiquetas']:
                    rule = message_format.format(
                        inputs[3]['nombre'], velocidad['nombre'],
                        inputs[0]['nombre'], tipo_via['nombre'],
                        inputs[1]['nombre'], trafico['nombre'],
                        inputs[2]['nombre'], estado['nombre'],
                        outputs[0]['nombre']
                    )
                    input_rule = input('{}: '.format(rule))
                    rules.append('{} {}'.format(rule, input_rule))
    print('\n%s reglas en el sistema.' % len(rules))


def save_rules():
    """Guardar el sistema de reglas obtenido en el problema."""
    response = input('Desea guardar el sistema de reglas? S/N: ')
    if response == 'S':
        pickle.dump(rules, open('rules.db', 'wb'))


"""Iniciar programa principal si es main."""
if __name__ == '__main__':
    generate_rules_system()
    save_rules()
