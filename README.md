# Aula---7---Sistemas-Distribuidos


Passo 1 — estrutura do processo

class Processo:
    def __init__(self, nome, indice, total):
        self.nome = nome
        self.indice = indice
        self.vetor = [0] * total

    def mostrar(self, evento):
        print(
            self.nome,
            evento,
            "->",
            self.vetor
        )

    def evento_local(self, descricao):
        self.vetor[self.indice] += 1
        self.mostrar(descricao)
__________________________________________________________________________________________________________

Passo 2 — método de envio


def enviar(self, mensagem):
        self.vetor[self.indice] += 1

        self.mostrar(
            "ENVIA: " + mensagem
        )

        return self.vetor.copy()
________________________________________________________________________________________________________

Passo 3 — método de recebimento

def receber(
        self,
        mensagem,
        vetor_recebido
    ):
        for i in range(len(self.vetor)):
            self.vetor[i] = max(
                self.vetor[i],
                vetor_recebido[i]
            )

        self.vetor[self.indice] += 1

        self.mostrar(
            "RECEBE: " + mensagem
        )
__________________________________________________________________________________________________

Passo 4 — crie os três processos

A = Processo("A", 0, 3)
B = Processo("B", 1, 3)
C = Processo("C", 2, 3)

A.evento_local("criou pedido")
B.evento_local("consultou estoque")
C.evento_local("iniciou faturamento")
_________________________________________________________________________________________________

Passo 5 — envie A → B


vetor_A = A.enviar(
    "pedido criado"
)

B.receber(
    "pedido criado",
    vetor_A
)
________________________________________________________________________________________________

Passo 6 — continue B → C


B.evento_local(
    "reservou estoque"
)

vetor_B = B.enviar(
    "estoque reservado"
)

C.receber(
    "estoque reservado",
    vetor_B
)

_____________________________________________________________________________________________

Passo 7 — execute

python vetor.py

# No Windows, se necessário:
py vetor.py

# Observe cada linha impressa.
# Exemplo de evolução:

A criou pedido -> [1, 0, 0]
B consultou estoque -> [0, 1, 0]
C iniciou faturamento -> [0, 0, 1]

_________________________________________________________________________________________

Perguntas para análise


1 - Qual posição do vetor pertence ao Processo A? E ao B? E ao C?
R: A pertence à posição 0, B à posição 1 e C à posição 2.

2 - O que aconteceu com o vetor de B quando ele recebeu uma mensagem de A?
R: B combinou seu vetor com o de A, atualizando os valores e incrementando seu próprio contador. O resultado foi [2, 2, 0].

3 - Por que C passa a conhecer eventos de A mesmo sem receber uma mensagem diretamente de A?
R: Porque B repassou a C as informações dos eventos de A contidas em seu vetor.

4 - Que informação foi propagada por B?
R :B propagou informações sobre os eventos que conhecia, incluindo os de A e os seus próprios.

5 - O vetor representa horário real? Explique.
R: Não. O vetor representa um relógio lógico que registra a ordem dos eventos, não o horário real.











