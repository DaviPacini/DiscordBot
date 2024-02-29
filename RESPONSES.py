from random import choice, randint
from datetime import datetime


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    atual = datetime.now()
    t = atual.strftime("%H:%M:%S")

    if lowered == '':
        return 'Bota isso aqui não padrin...'
    elif '$comandos' in lowered:
        return '$duvidas, $hora, $xingar, $dado'
    elif '$hora' in lowered:
        return t
    elif '$xingar' in lowered:
        return choice(['Sua mãe aquela imensa',
                       'Chupa meu pau',
                       'Dps eu amasso vc no fifa e tu n sabe pq',
                       'Sua mina eu vou pegar, e lalaialaia'])
    elif '$dado' in lowered:
        return f'Deu: {randint(1, 6)}'
    else:
        return choice(['Desculpa, não entendi',
                       'Do que você está falando?'
                       'Como é irmão?'])