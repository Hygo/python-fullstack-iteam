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

    def __init__(self, remetente, assunto_padrao="Notificação"):
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
        print("📧 [E-MAIL]")
        print(f"    De:      {self.remetente}")
        print(f"    Para:    {destinatario}")
        print(f"    Assunto: {self.assunto_padrao}")
        print(f"    Corpo:   {mensagem}")
        
        # TODO: Após imprimir, use self.formatar_log() e imprima o log com status "ENVIADO"
        log = self.formatar_log(destinatario, "ENVIADO")
        print(log)


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
        caracteres_originais = len(mensagem)
        if caracteres_originais > self.limite_chars:
            print(f"[Aviso] Mensagem para {destinatario} excedeu {self.limite_chars} caracteres e foi truncada!")
            mensagem = mensagem[:self.limite_chars]

        # TODO: Imprima a simulação no formato:
        print("📱 [SMS]")
        print(f"    De:         {self.remetente}")
        print(f"    Para:       {destinatario}")
        print(f"    Mensagem:   {mensagem}")
        print(f"    Caracteres: {caracteres_originais} / {self.limite_chars}")
        
        # TODO: Imprima o log de envio
        log = self.formatar_log(destinatario, "ENVIADO")
        print(log)


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
        print(f"🔔 [PUSH - {self.nome_app}]")
        print(f"    Ícone:       {self.icone}")
        print(f"    Destino:     {destinatario}")
        print(f"    Notificação: {mensagem}")
        
        # TODO: Imprima o log de envio
        log = self.formatar_log(destinatario, "ENVIADO")
        print(log)


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
    print("\n" + "-" * 50)
    # Chame o método enviar() do canal recebido
    canal.enviar(destinatario, mensagem)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE NOTIFICAÇÕES")
    print("=" * 50)

    email = NotificacaoEmail("sistema@iteam.com", "Atualização do Sistema")
    sms   = NotificacaoSMS("+55 92 99999-0000")
    push  = NotificacaoPush("servidor-01", "ITEAM App", "🎓")

    disparar_notificacao(email, "aluno1@email.com", "Bem-vindo ao curso Full Stack!")
    disparar_notificacao(sms, "+55 95 98888-1111", "Seu código de acesso é 4582.")
    disparar_notificacao(push, "user_id_992", "Nova nota publicada no portal.")


    print("\n" + "=" * 50)
    print("--- EXECUÇÃO DO DESAFIO (DUCK TYPING) ---")
    canais = [email, sms, push]
    for canal in canais:
        disparar_notificacao(canal, "aluno@email.com", "Sua aula começa em 30 minutos!")

    print("\n" + "=" * 50)
    print("--- TESTE DE SMS COM TEXTO LONGO ---")
    mensagem_longa = "Olá! Esta é uma mensagem extremamente longa para testar o sistema de truncamento automático do canal de SMS, contendo mais caracteres do que o limite permitido de cento e sessenta que foi estabelecido no construtor do objeto."
    disparar_notificacao(sms, "+55 95 98888-1111", mensagem_longa)

    print("\nExercício concluído!")