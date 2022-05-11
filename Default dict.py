# from collections import defaultdict
#
meu_texto = "Oi meu nome é Igor amo minha familia e amo minha esposa e amo minha filha"
meu_texto = meu_texto.lower()
#
# aparicoes = defaultdict(int)
#
# for palavras in meu_texto.split():
#     aparicoes[palavras] += 1
#
# print(aparicoes)

from collections import Counter

aparicoes = Counter(meu_texto.split())
print(aparicoes)