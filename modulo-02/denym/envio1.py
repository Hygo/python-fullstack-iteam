# ── VERSÃO 1 (ingênua) ── funciona, mas já tem cheiro ruim
def enviar_notificacao_v1(canal: str, mensagem: str) -> None:
    """Sistema de notificações – versão original com if/elif."""

    if canal == "email":
        print(f"[EMAIL] Enviando: {mensagem}")

    elif canal == "sms":
        print(f"[SMS] Enviando: {mensagem}")

    elif canal == "push":
        print(f"[PUSH] Enviando: {mensagem}")

    # ← Seis meses depois o time pede Slack, WhatsApp e Telegram...
    elif canal == "slack":
        # TODO: Brian vai revisar isso depois
        print(f"[SLACK] Enviando: {mensagem}")

    elif canal == "whatsapp":
        if len(mensagem) > 160:
            print(f"[WHATSAPP] Mensagem longa — truncando para 160 chars")
            mensagem = mensagem[:160]
        print(f"[WHATSAPP] Enviando: {mensagem}")

    elif canal == "telegram":
        print(f"[TELEGRAM] Enviando: {mensagem}")

    elif canal == "discord":
        # ATENÇÃO: discord exige formato diferente em prod
        print(f"[DISCORD] Enviando: {mensagem}")

    elif canal == "teams":
        print(f"[TEAMS] Enviando: {mensagem}")

    # ← Um ano depois: mais 6 canais, lógica condicional aninhada,
    #   comentários desatualizados, ninguém quer tocar nisso.
    else:
        print(f"[ERRO] Canal desconhecido: {canal}")


# Teste da versão problemática
enviar_notificacao_v1("teams", "Reunião às 14h")