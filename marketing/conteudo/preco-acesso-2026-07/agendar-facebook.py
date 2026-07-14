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

Passa na loja ou liga pra gente. A gente te mostra o preço na hora.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/aRd6h4Q.png",
        "unix_ts": 1784127600,  # 15/07/2026 12:00 BRT
    },
    {
        "message": """Parcela que cabe no bolso. 💳

Colchão novo em até 12x sem juros e sem entrada no carnê. Do jeito que o povo gosta, sem letra miúda.

Passa na loja ou liga pra gente. O Joaquim monta o parcelamento certo pra você.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/2NkTTEI.png",
        "unix_ts": 1784300400,  # 17/07/2026 12:00 BRT
    },
    {
        "message": """Colchão pra cada bolso. 🛏️

Tem opção boa em toda faixa de preço — do simples ao completo. Ninguém sai daqui sem solução pra dormir melhor.

Passa na loja ou liga pra gente. A gente acha o colchão certo pro seu bolso.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/kKUP1O4.png",
        "unix_ts": 1784559600,  # 20/07/2026 12:00 BRT
    },
]

for i, p in enumerate(posts, 1):
    print(f"\n--- Agendando Post {i} ---")
    result = schedule_post(acc, p["message"], p["unix_ts"], p["image_url"])
    status = "OK" if "post_id" in result else "ERRO"
    print(f"  [{status}] {result}")
