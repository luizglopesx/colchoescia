#!/usr/bin/env python3
"""Agenda os 3 posts do Anúncio Geral no Facebook — Colchões e Cia."""
import sys
sys.path.insert(0, r"d:\Projetos\colchoescia\.claude\skills\int-instagram\scripts")

from facebook_publisher import schedule_post, _get_account

acc = _get_account("colchoes_e_cia")

posts = [
    {
        "message": """Dormir bem não é luxo. É coisa de quem sabe onde comprar. 🛏️

A gente existe pra isso: colchão bom, preço justo, sem conversa fiada. Entrega e montagem grátis, parcelamento sem juros e aquele atendimento de vizinho que você já conhece.

Vem dar uma olhada. Sem compromisso.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📱 WhatsApp: (17) 3324-5765

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/OipuBpU.png",
        "unix_ts": 1783350000,  # 06/07/2026 12:00 BRT
    },
    {
        "message": """Preço de vizinho. Qualidade de verdade. 💰

Colchão novo com parcelamento que cabe no seu bolso: em até 12x sem juros e sem entrada no carnê. Do jeito que o povo gosta.

Passa na loja ou chama no WhatsApp. O Joaquim separa o melhor colchão pra você.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📱 WhatsApp: (17) 3324-5765

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/TnycqK4.png",
        "unix_ts": 1783522800,  # 08/07/2026 12:00 BRT
    },
    {
        "message": """Seu sono merece o melhor. E o melhor sempre coube aqui. 😴

Colchão novo, entrega rápida em Barretos, montagem grátis na hora. Sem estresse, sem enrolação.

Dormir bem não precisa ser complicado. Dá um pulo na loja ou manda um oi no WhatsApp.

📍 Rua 20 Esq. Av. 13 — Centro — Barretos
📱 WhatsApp: (17) 3324-5765

Pensou Colchão, Colchões e Cia!""",
        "image_url": "https://i.imgur.com/pOqntMg.png",
        "unix_ts": 1783695600,  # 10/07/2026 12:00 BRT
    },
]

for i, p in enumerate(posts, 1):
    print(f"\n--- Agendando Post {i} ---")
    result = schedule_post(acc, p["message"], p["unix_ts"], p["image_url"])
    status = "OK" if "post_id" in result else "ERRO"
    print(f"  [{status}] {result}")
