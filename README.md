# Jogo de Adivinhação (CLI)

Joguinho de terminal onde você tenta adivinhar um número de 1 a 100.
Escolha a dificuldade (easy = 10 tentativas, hard = 5) e receba dicas “muito alto/baixo” até acertar ou acabar as chances.

✨ Recursos

Número secreto aleatório (randint(1, 100)).

Dois níveis de dificuldade: easy (10) e hard (5).

Dicas a cada tentativa: muito alto / muito baixo.

Mensagens claras de vitória ou fim das tentativas.


🚀 Como executar

Pré-requisito: Python 3.9+

python adivinhacao.py

🕹️ Exemplo de sessão
./Bem-vindo(a)! Vamos jogar? Adivinhe um número de 1 a 100
Escolha a sua dificuldade: 'easy' ou 'hard': hard
Você tem 5 tentativas restantes
Faça um chute: 50
Muito alto!
Você tem 4 tentativas restantes
Faça um chute: 32
Muito baixo!
...
Parabéns! Você acertou, o número era 37

🔎 Como funciona (resumo)

dificuldade() retorna o número de tentativas com base na escolha do usuário.

aposta() controla o loop de palpites, imprime dicas e encerra ao acertar ou acabar as chances.

resposta_correta é gerado com randint(1, 100).
