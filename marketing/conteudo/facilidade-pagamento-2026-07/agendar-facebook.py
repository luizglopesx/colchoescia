#!/usr/bin/env python3
"""Agenda os 3 posts de Facilidade de Pagamento no Facebook — Colchões e Cia."""
import sys
sys.path.insert(0, r"d:\Projetos\colchoescia\.claude\skills\int-instagram\scripts")

from facebook_publisher import schedule_post, _get_account

acc = _get_account("colchoes_e_cia")

posts = [
    {
        "message": """Não espera pra dormir bem. 🛌

Comprou hoje, já pode trocar de colchão — em até 12x sem juros, no seu ritmo.

Passa na loja ou liga pra gente. A gente monta o parcelamento certo pra você.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/xgKFs3k.png",
        "unix_ts": 1785337200,  # 29/07/2026 12:00 BRT
    },
    {
        "message": """Compra fácil, sem enrolação. 📋

Parcelamento simples, direto com quem atende você — sem complicação pra fechar.

Passa na loja ou liga pra gente. A gente resolve rápido, sem rodeio.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/7O6KbHJ.png",
        "unix_ts": 1785510000,  # 31/07/2026 12:00 BRT
    },
    {
        "message": """Do jeito que cabe no seu mês. 💳

Parcelamento sem juros, simples do começo ao fim.

Passa na loja ou liga pra gente. A gente encontra o parcelamento certo pro seu bolso.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/WkmkmEU.png",
        "unix_ts": 1785769200,  # 03/08/2026 12:00 BRT
    },
]

for i, p in enumerate(posts, 1):
    print(f"\n--- Agendando Post {i} ---")
    result = schedule_post(acc, p["message"], p["unix_ts"], p["image_url"])
    status = "OK" if "post_id" in result else "ERRO"
    print(f"  [{status}] {result}")
