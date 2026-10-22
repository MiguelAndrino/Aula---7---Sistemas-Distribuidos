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

    def enviar(self, mensagem):
        self.vetor[self.indice] += 1

        self.mostrar(
            "ENVIA: " + mensagem
        )

        return self.vetor.copy()

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

A = Processo("A", 0, 3)
B = Processo("B", 1, 3)
C = Processo("C", 2, 3)

A.evento_local("criou pedido")
B.evento_local("consultou estoque")
C.evento_local("iniciou faturamento")

vetor_A = A.enviar(
    "pedido criado"
)

B.receber(
    "pedido criado",
    vetor_A
)

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
