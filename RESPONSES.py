from random import choice, randint
from datetime import datetime


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    atual = datetime.now()
    t = atual.strftime("%H:%M:%S")

    if lowered == '':
        return 'Bota isso aqui não padrin...'
    elif '$comandos' in lowered:
        return '**$duvidas**, **$hora**, **$xingar**, **$dado**, **$insta**, **$wpp**, **$vava**, **$cs**, **$lol**, **$fifa**, **$rl**'
    elif '$hora' in lowered:
        return t
    elif '$xingar' in lowered:
        return choice(['Sua mãe aquela imensa',
                       'Chupa meu pau',
                       'Dps eu amasso vc no fifa e tu n sabe pq',
                       'Sua mina eu vou pegar, e lalaialaia',
                       'Quer me fuder, me beija',
                       'Masoquista é? pedindo pra te xingar, estranho',
                       'Vai te fuder, primata',
                       'cê quer dar cê fala ta?'])
    elif '$dado' in lowered:
        return f'Deu: {randint(1, 6)}'
    elif '$insta' in lowered:
        return f'Ja seguiu nosso insta? https://www.instagram.com/atletica.cybernetica/'
    elif '$wpp' in lowered:
        return f'Nosso WhatsApp: https://chat.whatsapp.com/DVcRtuKbUJTDZRGcsCpmDa'
    elif '$é o brazzino' in lowered:
        return ' Jogo da galera...\n' \
               'Vem jogar Brazino que é o jogo da galera\n' \
               'Vem jogar Brazino que é direto na sua tela\n'
    elif '$vava' in lowered:
        return 'No momento a Line de VAVA se encontra indisponível!'
    elif '$cs' in lowered:
        return 'No momento a Line de CS se encontra indisponível!'
    elif '$lol' in lowered:
        return 'No momento a Line de LOL se encontra indisponível!'
    elif '$fifa' in lowered:
        return 'No momento a Line de FIFA se encontra indisponível!'
    elif '$rl' in lowered:
        return 'No momento a Line de ROCKET LEAGUE se encontra indisponível!'
    elif '$duvidas' in lowered:
        return '**1- Como participo da equipe Cyber? ** Divulgamos sempre nos grupos de "$wpp" ou no "$insta" quando os forms para se candidatar estao abertos, então fiquem de olho\n' \
               '**2- Como funcionam os treinos? ** Cada Coordenador tem a autonomia para decidir como os treinos ocorrerão, então por via das dúvidas, consulte o coordenador do seu jogo'

    else:
        return choice(['Desculpa, não entendi',
                       'Do que você está falando?',
                       'Como é irmão?'])