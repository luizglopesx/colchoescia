#!/usr/bin/env python3
"""Agenda os 3 posts de Preço e Acesso no Facebook — Colchões e Cia."""
import sys
sys.path.insert(0, r"d:\Projetos\colchoescia\.claude\skills\int-instagram\scripts")

from facebook_publisher import schedule_post, _get_account

acc = _get_account("colchoes_e_cia")

posts = [
    {
        "message": """Colchão bom não precisa ser caro. 💰

Qualidade de verdade com preço que cabe na sua realidade. Sem enrolação, sem promessa vazia — só colchão bom pra você dormir melhor.

Passa na loja ou chama no WhatsApp. A gente te mostra o preço na hora.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📱 WhatsApp: (17) 3324-5765

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/APtmf7d.png",
        "unix_ts": 1784127600,  # 15/07/2026 12:00 BRT
    },
    {
        "message": """Parcela que cabe no bolso. 💳

Colchão novo em até 12x sem juros e sem entrada no carnê. Do jeito que o povo gosta, sem letra miúda.

Passa na loja ou chama no WhatsApp. O Joaquim monta o parcelamento certo pra você.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📱 WhatsApp: (17) 3324-5765

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/9SfzsVf.png",
        "unix_ts": 1784300400,  # 17/07/2026 12:00 BRT
    },
    {
        "message": """Preço claro, sem pegadinha. 🔍

O que você vê na loja é o que você paga. Sem letra miúda, sem taxa escondida — do jeito que a gente sempre fez.

Passa na loja ou chama no WhatsApp. Preço na lata, sem enrolação.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📱 WhatsApp: (17) 3324-5765

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/oaDpRRK.png",
        "unix_ts": 1784559600,  # 20/07/2026 12:00 BRT
    },
]

for i, p in enumerate(posts, 1):
    print(f"\n--- Agendando Post {i} ---")
    result = schedule_post(acc, p["message"], p["unix_ts"], p["image_url"])
    status = "OK" if "post_id" in result else "ERRO"
    print(f"  [{status}] {result}")
