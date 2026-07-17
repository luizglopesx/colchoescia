#!/usr/bin/env python3
"""Agenda os 3 posts de Espuma ou Mola no Facebook — Colchões e Cia."""
import sys
sys.path.insert(0, r"d:\Projetos\colchoescia\.claude\skills\int-instagram\scripts")

from facebook_publisher import schedule_post, _get_account

acc = _get_account("colchoes_e_cia")

posts = [
    {
        "message": """Espuma ou molas? A dúvida que todo mundo tem antes de comprar. 🤔

Cada colchão tem um jeito diferente de sustentar o corpo. Não existe um melhor pra todo mundo — existe o melhor pro seu jeito de dormir.

Nos próximos posts a gente mostra a diferença entre os dois. E se quiser sentir na pele, é só vir na loja e testar.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/uVkiaBc.png",
        "unix_ts": 1784732400,  # 22/07/2026 12:00 BRT
    },
    {
        "message": """Espuma com firmeza de verdade. 🛌

O colchão de espuma é mais denso e mantém a base firme a noite toda, sem afundar com o tempo. Ótimo pra quem gosta de dormir numa superfície mais dura e sente falta de sustentação.

Vem na loja sentir a diferença. A gente te ajuda a escolher o modelo certo.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/pNdJkVB.png",
        "unix_ts": 1784905200,  # 24/07/2026 12:00 BRT
    },
    {
        "message": """Molas com maciez que acolhe. 🌬️

O colchão de molas vem com camadas de conforto por cima, deixando a superfície mais macia sem perder a ventilação. Ótimo pra quem gosta de uma cama mais aconchegante e sente calor durante o sono.

Espuma ou molas, a gente tem os dois. Vem na loja testar e decidir com o corpo, não só o preço.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📞 (17) 3325-6039

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/UyfEzmY.png",
        "unix_ts": 1785164400,  # 27/07/2026 12:00 BRT
    },
]

for i, p in enumerate(posts, 1):
    print(f"\n--- Agendando Post {i} ---")
    result = schedule_post(acc, p["message"], p["unix_ts"], p["image_url"])
    status = "OK" if "post_id" in result else "ERRO"
    print(f"  [{status}] {result}")
