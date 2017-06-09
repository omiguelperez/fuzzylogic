import json
import pickle


class RuleSystem(object):
    """This class contains the Rule System capability."""

    def __init__(self, rules=[]):
        """Set RuleSystem initial config."""
        super(RuleSystem, self).__init__()
        self.rules = rules

    def add_rule(self, rule):
        """Add new rule to rules system."""
        self.rules.append(rule)

    def format_rule(self, rule):
        """Format and generate a rule."""
        basic_format = 'SI {} es {}, {} es {}, ... ENTONCES {} es '

    def generate(self):
        """Genera el sistema de reglas base del problema."""
        inputs = json.loads(open('resources/inputs.json').read())['inputs']
        outputs = json.loads(open('resources/outputs.json').read())['outputs']
        message_format = 'SI {} es {}, {} es {}, {} es {}, {} es {} ENTONCES {} es '

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
                        print(rule)
                        self.rules.append(rule)
        print('\n%s reglas en el sistema.' % len(self.rules))

    def save_rules():
        """Save generated rules system on disk."""
        response = input('? S/N: ').upper()
        if response == 'S':
            pickle.dump(rules, open('rules.db', 'wb'))


if __name__ == '__main__':
    rule_system = RuleSystem()
    rule_system.generate()