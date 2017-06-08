inputs = [
    ['Humedad', [
        'Muy baja',
        'Baja',
        'Media',
        'Alta',
        'Muy Alta'
    ]],
    ['Grano partido', [
        'Poco partido',
        'Medio',
        'Muy partido'
    ]],
    ['Impureza', [
        'Muy baja',
        'Baja',
        'Media',
        'Alta',
        'Muy alta'
    ]]
]

outputs = [
    ['Calidad', [
        'Baja',
        'Media',
        'Alta'
    ]]
]

message_format = 'SI {} es {}, {} es {} e {} es {} ENTONCES {} es '
messages = []

for humedad in inputs[0][1]:
    for grano_partido in inputs[1][1]:
        for impureza in inputs[2][1]:
            message = message_format.format(
                inputs[0][0], humedad, inputs[1][0],
                grano_partido, inputs[2][0], impureza,
                outputs[0][0]
            )
            messages.append(message)

print('%s mensajes' % len(messages))
