    BANCO LISTA

 class Bancolista:
     def __init__(self):
         self.contas = []

     def cadastrar(self , conta):
         self.contas.append(conta)

     def procurar_conta(self , numero):
        achou = false
        for conta in self.contas:
            if conta.get_numero() == numero:
                achou = true
                return conta
            if achou is false
                return none