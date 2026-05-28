# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 04 - POLIMORFISMO E DUCK TYPING
#
# Tema: Sistema de Notificações
#
# Objetivo:
#   Criar um sistema de notificações onde diferentes canais de envio
#   (E-mail, SMS, Push) respondem ao mesmo método 'enviar()' de formas
#   distintas, demonstrando polimorfismo e o conceito de Duck Typing do Python.
#
# Duck Typing:
#   "Se anda como pato e faz qua-qua como pato, então é um pato."
#   → O Python não exige que os objetos sejam da mesma classe, apenas que
#     possuam o método esperado (neste caso, 'enviar()').
#
# Estrutura das classes:
#
#   CanalNotificacao (classe base abstrata - não instancie diretamente)
#       │
#       ├── NotificacaoEmail
#       ├── NotificacaoSMS
#       └── NotificacaoPush
#
# Conceitos trabalhados:
#   - Polimorfismo: mesma interface, comportamentos diferentes
#   - Duck Typing: função polimórfica que aceita qualquer objeto com 'enviar()'
#   - Sobrescrita de métodos
#   - Funções que recebem objetos como argumento (callbacks)
#
# Referência: Seções 5.3.3 e 5.7 da Apostila ITEAM
# =============================================================================


# -----------------------------------------------------------------------------
# CLASSE BASE (Interface/Contrato)
# -----------------------------------------------------------------------------

class CanalNotificacao:
    """
    Classe base que define o contrato para todos os canais de notificação.
    Não deve ser instanciada diretamente.
    """

    def __init__(self, remetente):
        """
        Args:
            remetente (str): Nome ou identificador do remetente.
        """
        # TODO: Atribua o remetente ao atributo de instância
        self.remetente = remetente

    def enviar(self, destinatario, mensagem):
        """
        Método que DEVE ser sobrescrito pelas subclasses.
        Lança um erro se chamado diretamente na classe base.

        Args:
            destinatario (str): Destinatário da notificação.
            mensagem (str): Conteúdo da notificação.
        """
        # Este padrão (levantar NotImplementedError) simula um método abstrato,
        # forçando as subclasses a implementar o comportamento.
        raise NotImplementedError(
            f"A classe '{type(self).__name__}' deve implementar o método 'enviar()'."
        )

    def formatar_log(self, destinatario, status):
        """
        Formata uma linha de log para o envio realizado.
        Método compartilhado por todas as subclasses (não precisa sobrescrever).

        Args:
            destinatario (str): Destinatário da mensagem.
            status (str): Status do envio (ex: "ENVIADO", "FALHOU").

        Returns:
            str: Linha de log formatada.
        """
        canal = type(self).__name__
        return f"[LOG] [{canal}] De: {self.remetente} → Para: {destinatario} | Status: {status}"


# -----------------------------------------------------------------------------
# SUBCLASSE 1: Notificação por E-mail
# -----------------------------------------------------------------------------

class NotificacaoEmail(CanalNotificacao):
    """
    Envia notificações via e-mail.

    Atributos extras:
        assunto_padrao (str): Assunto padrão para os e-mails enviados.
    """

    def __init__(self, remetente, assunto_padrao="Notificação ITEAM"):
        """
        Args:
            remetente (str): E-mail do remetente.
            assunto_padrao (str): Assunto padrão dos e-mails.
        """
        # TODO: Chame super().__init__() com o remetente
        # TODO: Atribua o assunto_padrao
        super().__init__(remetente)
        self.assunto_padrao = assunto_padrao

    def enviar(self, destinatario, mensagem):
        """
        Simula o envio de um e-mail, exibindo todas as informações formatadas.

        Args:
            destinatario (str): E-mail do destinatário.
            mensagem (str): Corpo do e-mail.
        """
        # TODO: Imprima a simulação do envio no formato:
        #
        # 📧 [E-MAIL]
        #    De:      [remetente]
        #    Para:    [destinatario]
        #    Assunto: [assunto_padrao]
        #    Corpo:   [mensagem]
        #
        # TODO: Após imprimir, use self.formatar_log() e imprima o log com status "ENVIADO"
        print(f"""
        📧 [E-MAIL]
           De:      {self.remetente}
           Para:    {destinatario}
           Assunto: {self.assunto_padrao}
           Corpo:   {mensagem}""")
        
        print(self.formatar_log(destinatario, "ENVIADO"))


# -----------------------------------------------------------------------------
# SUBCLASSE 2: Notificação por SMS
# -----------------------------------------------------------------------------

class NotificacaoSMS(CanalNotificacao):
    """
    Envia notificações via SMS, com limite de caracteres.

    Atributos extras:
        limite_chars (int): Limite de caracteres por mensagem (padrão: 160).
    """

    def __init__(self, remetente, limite_chars=160):
        """
        Args:
            remetente (str): Número de telefone do remetente.
            limite_chars (int): Limite de caracteres (padrão 160).
        """
        # TODO: Chame super().__init__() e atribua limite_chars
        super().__init__(remetente)
        self.limite_chars = limite_chars

    def enviar(self, destinatario, mensagem):
        """
        Simula o envio de SMS. Se a mensagem ultrapassar o limite,
        ela deve ser truncada e o usuário deve ser avisado.

        Args:
            destinatario (str): Número do destinatário.
            mensagem (str): Texto do SMS.
        """
        # TODO: Verifique se len(mensagem) > self.limite_chars.
        # Se sim: truncate a mensagem (mensagem[:limite_chars]) e avise o usuário.
        if len(mensagem) > self.limite_chars:
            mensagem = mensagem[:self.limite_chars]
            print("Sua mensagem será truncada, pois utrapassa o limite de 160 caracteres.")

        # TODO: Imprima a simulação no formato:
        #
        # 📱 [SMS]
        #    De:         [remetente]
        #    Para:       [destinatario]
        #    Mensagem:   [mensagem (truncada ou completa)]
        #    Caracteres: [len(mensagem)] / [limite_chars]
        #
        # TODO: Imprima o log de envio
        print(f"""
        📱 [SMS]
            De:         {self.remetente}
            Para:       {destinatario}
            Mensagem:   {mensagem}
            Caracteres: {len(mensagem)} / {self.limite_chars}
""")
        print(self.formatar_log(destinatario, "ENVIADO"))


# -----------------------------------------------------------------------------
# SUBCLASSE 3: Notificação Push (App)
# -----------------------------------------------------------------------------

class NotificacaoPush(CanalNotificacao):
    """
    Envia notificações push para um aplicativo mobile.

    Atributos extras:
        nome_app (str): Nome do aplicativo que dispara a notificação.
        icone (str): Emoji ou identificador do ícone da notificação.
    """

    def __init__(self, remetente, nome_app, icone="🔔"):
        """
        Args:
            remetente (str): ID do sistema remetente.
            nome_app (str): Nome do aplicativo.
            icone (str): Ícone da notificação.
        """
        # TODO: Chame super().__init__() e atribua nome_app e icone
        super().__init__(remetente)
        self.nome_app = nome_app
        self.icone = icone

    def enviar(self, destinatario, mensagem):
        """
        Simula o envio de uma notificação push.

        Args:
            destinatario (str): ID do dispositivo ou usuário.
            mensagem (str): Texto curto da notificação.
        """
        # TODO: Imprima a simulação no formato:
        #
        # 🔔 [PUSH - nome_app]
        #    Ícone:       [icone]
        #    Destino:     [destinatario]
        #    Notificação: [mensagem]
        #
        # TODO: Imprima o log de envio
        print(f"""
        🔔 [PUSH - {self.nome_app}]
            Ícone:       {self.icone}
            Destino:     {destinatario}
            Notificação: {mensagem}
        """)
        print(self.formatar_log(destinatario, "ENVIADO"))


# -----------------------------------------------------------------------------
# FUNÇÃO POLIMÓRFICA (Duck Typing em ação)
# -----------------------------------------------------------------------------

def disparar_notificacao(canal, destinatario, mensagem):
    """
    Função polimórfica que aceita QUALQUER canal de notificação.
    Não importa se é E-mail, SMS ou Push — desde que tenha o método 'enviar()'.

    Args:
        canal: Qualquer objeto que possua o método 'enviar()'.
        destinatario (str): Destinatário da notificação.
        mensagem (str): Conteúdo da notificação.
    """
    # TODO: Imprima um separador visual e chame canal.enviar(destinatario, mensagem)
    print("\n" + "=" * 50)
    # Chame o método enviar() do canal recebido
    canal.enviar(destinatario, mensagem)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE NOTIFICAÇÕES - ITEAM")
    print("=" * 50)

    # TODO: Crie uma instância de cada canal:
    # email = NotificacaoEmail("sistema@iteam.com", "Atualização do Sistema")
    # sms   = NotificacaoSMS("+55 92 99999-0000")
    # push  = NotificacaoPush("servidor-01", "ITEAM App", "🎓")
    email = NotificacaoEmail("sistema@iteam.com", "Atualização do Sistema")
    sms   = NotificacaoSMS("+55 92 99999-0000")
    push  = NotificacaoPush("servidor-01", "ITEAM App", "🎓")

    # TODO: Use a função disparar_notificacao() para enviar mensagens por cada canal
    disparar_notificacao(email, "Aluno1 ITEAM", "Mensagem 1")
    disparar_notificacao(sms, "Aluno1 ITEAM", "Mensagem 2")
    disparar_notificacao(push, "Aluno1 ITEAM", "Mensagem 3")

    # TODO (DESAFIO DUCK TYPING): Crie uma lista com os diferentes canais e
    # percorra-a chamando disparar_notificacao() para cada um com a mesma mensagem.
    # Observe como cada canal responde de forma diferente!
    #
    canais = [email, sms, push]
    for canal in canais:
        disparar_notificacao(canal, "aluno@email.com", "Sua aula começa em 30 minutos!")

    # TODO (DESAFIO EXTRA): Teste enviar um SMS com uma mensagem muito longa
    # (mais de 160 caracteres) e observe o truncamento.
    disparar_notificacao(sms, "Aluno1 ITEAM", "Essa é uma mensagem muito longa."*30)

    print("\nExercício concluído!")
