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
        self.remetente = None

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
        self.assunto_padrao = None

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
        pass


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
        self.limite_chars = None

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

        # TODO: Imprima a simulação no formato:
        #
        # 📱 [SMS]
        #    De:         [remetente]
        #    Para:       [destinatario]
        #    Mensagem:   [mensagem (truncada ou completa)]
        #    Caracteres: [len(mensagem)] / [limite_chars]
        #
        # TODO: Imprima o log de envio
        pass


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
        self.nome_app = None
        self.icone = None

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
        pass


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
    pass


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

    # TODO: Use a função disparar_notificacao() para enviar mensagens por cada canal

    # TODO (DESAFIO DUCK TYPING): Crie uma lista com os diferentes canais e
    # percorra-a chamando disparar_notificacao() para cada um com a mesma mensagem.
    # Observe como cada canal responde de forma diferente!
    #
    # canais = [email, sms, push]
    # for canal in canais:
    #     disparar_notificacao(canal, "aluno@email.com", "Sua aula começa em 30 minutos!")

    # TODO (DESAFIO EXTRA): Teste enviar um SMS com uma mensagem muito longa
    # (mais de 160 caracteres) e observe o truncamento.

    print("\nExercício concluído!")
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
        """
        # Este padrão simula um método abstrato
        raise NotImplementedError(
            f"A classe '{type(self).__name__}' deve implementar o método 'enviar()'."
        )

    def formatar_log(self, destinatario, status):
        """
        Formata uma linha de log para o envio realizado.
        """
        canal = type(self).__name__
        return f"[LOG] [{canal}] De: {self.remetente} → Para: {destinatario} | Status: {status}"


# -----------------------------------------------------------------------------
# SUBCLASSE 1: Notificação por E-mail
# -----------------------------------------------------------------------------

class NotificacaoEmail(CanalNotificacao):
    """
    Envia notificações via e-mail.
    """

    def __init__(self, remetente, assunto_padrao="Notificação ITEAM"):
        """
        Inicializa o canal de e-mail.
        """
        # TODO: Chame super().__init__() com o remetente e atribua o assunto_padrao
        super().__init__(remetente)
        self.assunto_padrao = assunto_padrao

    def enviar(self, destinatario, mensagem):
        """
        Simula o envio de um e-mail.
        """
        # TODO: Imprima a simulação do envio no formato solicitado
        print("📧 [E-MAIL]")
        print(f"    De:      {self.remetente}")
        print(f"    Para:    {destinatario}")
        print(f"    Assunto: {self.assunto_padrao}")
        print(f"    Corpo:   {mensagem}")
        
        # TODO: Use self.formatar_log() e imprima o log com status "ENVIADO"
        log = self.formatar_log(destinatario, "ENVIADO")
        print(log)


# -----------------------------------------------------------------------------
# SUBCLASSE 2: Notificação por SMS
# -----------------------------------------------------------------------------

class NotificacaoSMS(CanalNotificacao):
    """
    Envia notificações via SMS, com limite de caracteres.
    """

    def __init__(self, remetente, limite_chars=160):
        """
        Inicializa o canal de SMS.
        """
        # TODO: Chame super().__init__() e atribua limite_chars
        super().__init__(remetente)
        self.limite_chars = limite_chars

    def enviar(self, destinatario, mensagem):
        """
        Simula o envio de SMS com validação e truncamento de texto.
        """
        # TODO: Verifique se len(mensagem) > self.limite_chars.
        tamanho_original = len(mensagem)
        if tamanho_original > self.limite_chars:
            print(f"⚠️ [AVISO] Mensagem muito longa ({tamanho_original} caracteres). Reduzindo para o limite de {self.limite_chars}h.")
            mensagem = mensagem[:self.limite_chars]

        # TODO: Imprima a simulação no formato solicitado
        print("📱 [SMS]")
        print(f"    De:         {self.remetente}")
        print(f"    Para:       {destinatario}")
        print(f"    Mensagem:   {mensagem}")
        print(f"    Caracteres: {len(mensagem)} / {self.limite_chars}")
        
        # TODO: Imprima o log de envio
        log = self.formatar_log(destinatario, "ENVIADO")
        print(log)


# -----------------------------------------------------------------------------
# SUBCLASSE 3: Notificação Push (App)
# -----------------------------------------------------------------------------

class NotificacaoPush(CanalNotificacao):
    """
    Envia notificações push para um aplicativo mobile.
    """

    def __init__(self, remetente, nome_app, icone="🔔"):
        """
        Inicializa o canal push.
        """
        # TODO: Chame super().__init__() e atribua nome_app e icone
        super().__init__(remetente)
        self.nome_app = nome_app
        self.icone = icone

    def enviar(self, destinatario, mensagem):
        """
        Simula o envio de uma notificação push.
        """
        # TODO: Imprima a simulação no formato solicitado
        print(f"{self.icone} [PUSH - {self.nome_app}]")
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
    """
    # TODO: Imprima um separador visual e chame canal.enviar(destinatario, mensagem)
    print("\n" + "=" * 55)
    canal.enviar(destinatario, message=mensagem) if hasattr(canal, 'enviar') else canal.enviar(destinatario, mensagem)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE NOTIFICAÇÕES - ITEAM")
    print("=" * 50)

    # 1. Instanciando cada um dos canais disponíveis
    email = NotificacaoEmail("sistema@iteam.com", "Atualização do Sistema")
    sms   = NotificacaoSMS("+55 92 99999-0000")
    push  = NotificacaoPush("servidor-01", "ITEAM App", "🎓")

    # 2. DESAFIO DUCK TYPING: Enviando a mesma mensagem em lote percorrendo a lista
    print("\n--- Desafio: Disparos Dinâmicos (Lote) ---")
    canais = [email, sms, push]
    
    for c in canais:
        disparar_notificacao(c, "aluno_dev_fullstack@email.com", "Sua aula começa em 30 minutos!")

    # 3. DESAFIO EXTRA: Testando estouro do limite de caracteres do SMS
    print("\n" + "=" * 55)
    print("--- Testando Limite de Caracteres (SMS) ---")
    mensagem_gigante = (
        "Olá, esta é uma mensagem extremamente longa criada intencionalmente para "
        "testar a regra de negócio aplicada ao sistema de mensagens rápidas via celular SMS. "
        "Ela deve obrigatoriamente estourar o teto padrão estabelecido de cento e sessenta caracteres."
    )
    disparar_notificacao(sms, "+55 11 98888-7777", mensagem_gigante)

    print("\nExercício concluído!")
