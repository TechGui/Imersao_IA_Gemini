import requests;
import random;

#Acessar para pegar as palavras e dicas para jogar.
url = 'https://raw.githubusercontent.com/arturferreiradev/imersao-ia-gemini/main/live-python/words.json';

resposta = requests.get(url);
data = resposta.json();
valor_secreto = random.choice(data);
palavra_secreta = valor_secreto['palavra'];
dica = valor_secreto['dica'];

chute = input(f'A palavra secreta tem {len(palavra_secreta)} letras -> {dica}\n');

if(chute == palavra_secreta):
    print('Acertou');
else:
    print(f'Errou.. a palavra secreta era {palavra_secreta}');