# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 04 - POLIMORFISMO E DUCK TYPING
#
# Aluno: Kelvin Araújo Ferreira
# =============================================================================


# -----------------------------------------------------------------------------
# CLASSE BASE
# -----------------------------------------------------------------------------

class CanalNotificacao:
    """Classe base que define o contrato para todos os canais de notificação."""

    def __init__(self, remetente):
        self.remetente = remetente

    def enviar(self, destinatario, mensagem):
        raise NotImplementedError(
            f"A classe '{type(self).__name__}' deve implementar o método 'enviar()'."
        )

    def formatar_log(self, destinatario, status):
        canal = type(self).__name__
        return f"[LOG] [{canal}] De: {self.remetente} → Para: {destinatario} | Status: {status}"


# -----------------------------------------------------------------------------
# SUBCLASSE 1: E-mail
# -----------------------------------------------------------------------------

class NotificacaoEmail(CanalNotificacao):
    """Envia notificações via e-mail."""

    def __init__(self, remetente, assunto_padrao="Notificação ITEAM"):
        super().__init__(remetente)
        self.assunto_padrao = assunto_padrao

    def enviar(self, destinatario, mensagem):
        print("📧 [E-MAIL]")
        print(f"   De:      {self.remetente}")
        print(f"   Para:    {destinatario}")
        print(f"   Assunto: {self.assunto_padrao}")
        print(f"   Corpo:   {mensagem}")
        print(self.formatar_log(destinatario, "ENVIADO"))


# -----------------------------------------------------------------------------
# SUBCLASSE 2: SMS
# -----------------------------------------------------------------------------

class NotificacaoSMS(CanalNotificacao):
    """Envia notificações via SMS com limite de caracteres."""

    def __init__(self, remetente, limite_chars=160):
        super().__init__(remetente)
        self.limite_chars = limite_chars

    def enviar(self, destinatario, mensagem):
        if len(mensagem) > self.limite_chars:
            print(f"   ⚠️  Mensagem truncada de {len(mensagem)} para {self.limite_chars} caracteres.")
            mensagem = mensagem[:self.limite_chars]

        print("📱 [SMS]")
        print(f"   De:         {self.remetente}")
        print(f"   Para:       {destinatario}")
        print(f"   Mensagem:   {mensagem}")
        print(f"   Caracteres: {len(mensagem)} / {self.limite_chars}")
        print(self.formatar_log(destinatario, "ENVIADO"))


# -----------------------------------------------------------------------------
# SUBCLASSE 3: Push
# -----------------------------------------------------------------------------

class NotificacaoPush(CanalNotificacao):
    """Envia notificações push para um aplicativo mobile."""

    def __init__(self, remetente, nome_app, icone="🔔"):
        super().__init__(remetente)
        self.nome_app = nome_app
        self.icone = icone

    def enviar(self, destinatario, mensagem):
        print(f"🔔 [PUSH - {self.nome_app}]")
        print(f"   Ícone:       {self.icone}")
        print(f"   Destino:     {destinatario}")
        print(f"   Notificação: {mensagem}")
        print(self.formatar_log(destinatario, "ENVIADO"))


# -----------------------------------------------------------------------------
# FUNÇÃO POLIMÓRFICA (Duck Typing em ação)
# -----------------------------------------------------------------------------

def disparar_notificacao(canal, destinatario, mensagem):
    """Aceita QUALQUER canal que possua o método 'enviar()'."""
    print("\n" + "=" * 50)
    canal.enviar(destinatario, mensagem)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE NOTIFICAÇÕES - ITEAM")
    print("=" * 50)

    email = NotificacaoEmail("sistema@iteam.com", "Atualização do Sistema")
    sms   = NotificacaoSMS("+55 92 99999-0000")
    push  = NotificacaoPush("servidor-01", "ITEAM App", "🎓")

    # Duck Typing: mesmo loop, mesmo método, comportamentos diferentes
    canais = [email, sms, push]
    for canal in canais:
        disparar_notificacao(canal, "aluno@email.com", "Sua aula começa em 30 minutos!")

    # Desafio: SMS com mensagem longa
    mensagem_longa = "A" * 200
    disparar_notificacao(sms, "+55 92 98888-1111", mensagem_longa)

    print("\nExercício concluído!")
