
class Mensagem:

    # Serve de base para as outras classes através das heranças.

    def enviar_mensagem(self):

        # Apenas define uma função para ser usada para as outras classes. 

        pass

# Herança   vvvvvvvv
class Email(Mensagem):

    def __init__(self, destinatario, assunto, corpo):

        # O email (objeto) é composto por um destinatário, um assunto, e um corpo.

        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo

    def enviar_mensagem(self):

        # Polimorfismo - apesar de usar a mesma função, 
        # devolve uma resposta diferente.

        return f"{self.destinatario}; Assunto:{self.assunto} - {self.corpo}"

# Herança vvvvvvvv
class SMS(Mensagem):

    def __init__(self, numero, mensagem):

        # O SMS (objeto) é composto por um número (de telefone) e uma mensagem. 

        self.numero = numero
        self.mensagem = mensagem

    def enviar_mensagem(self):

        # Polimorfismo - apesar de usar a mesma função, 
        # devolve uma resposta diferente.

        return f"{self.numero} - {self.mensagem}"

# Herança             vvvvvvvv
class NotificacaoPush(Mensagem):

    def __init__(self, dispositivo_id, mensagem):

        # A notificação (objeto) é composta por um ID e uma mensagem.

        self.dispositivo_id = dispositivo_id
        self.mensagem = mensagem

    def enviar_mensagem(self):

        # Polimorfismo - apesar de usar a mesma função, 
        # devolve uma resposta diferente.

        return f"{self.dispositivo_id} - {self.mensagem}"

# Herança          vvvvvvvv
def realizar_envio(mensagem):
    
    # Define uma função que, quando chamada, 
    # dá print ao enviar_mensagem, que pedende da classe.

    # No caso da NotificacaoPush, o enviar_mensagem está definido como: 
    # 'return f"{self.dispositivo_id} - {self.mensagem}" '. Ou seja, polimorfismo!

    print(mensagem.enviar_mensagem())

# "Data" :
email = Email(destinatario="joao.silva@email.com", assunto="Reunião", corpo="Reunião marcada para as 10h.")
sms = SMS(numero="912345678", mensagem="A sua Encomenda Chegou!")
notificacao = NotificacaoPush(dispositivo_id="abc123", mensagem="Tem uma Nova Mensagem.")

# Prints :
realizar_envio(email)
realizar_envio(sms)
realizar_envio(notificacao)
