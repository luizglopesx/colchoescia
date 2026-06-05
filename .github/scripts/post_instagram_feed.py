#!/usr/bin/env python3
"""Publica post no feed do Instagram — Campanha Namorados (Colchões & Cia 2026)."""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta

ACCESS_TOKEN = os.environ["IG_TOKEN"]
ACCOUNT_ID   = os.environ["IG_ACCOUNT_ID"]
BASE_URL     = "https://graph.facebook.com/v25.0"

POSTS = {
    "03/06": {
        "image": "https://i.imgur.com/Yj10XsT.png",
        "caption": (
            "😴 Dormir bem é presente de quem ama de verdade.\n\n"
            "Nossa Cama Box Casal com Molas Ensacadas é conforto de verdade, pelo preço que cabe no seu bolso:\n\n"
            "✅ Molas ensacadas — sem barulho, sem balançar\n"
            "✅ Casal — espaço pra dois\n"
            "✅ 12x de R$ 132,50 SEM JUROS\n"
            "✅ Entrega e montagem grátis!\n\n"
            "📲 Chama agora: (17) 3325-6039\n"
            "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
            "#ColchõesCia #CamaBoxCasal #MolasEnsacadas #Barretos #DiaDoNamorados"
        ),
    },
    "11/06": {
        "image": "https://i.imgur.com/JuAnmTL.png",
        "caption": (
            "⏰ Ainda dá tempo!\n\n"
            "O Dia dos Namorados tá chegando e a melhor oferta de Barretos ainda tá aqui:\n\n"
            "🛏 Cama Box Casal — Molas Ensacadas\n"
            "💳 12x de R$ 132,50 sem juros\n"
            "🚚 Entrega e montagem GRÁTIS\n\n"
            "👉 Chama no WhatsApp agora: (17) 3324-5765\n"
            "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n\n"
            "Não deixa o presente do namorado(a) pra depois! 💙\n\n"
            "#ColchõesCia #Barretos #OfertaDeNamorados"
        ),
    },
    "12/06": {
        "image": "https://i.imgur.com/cPNiHJH.png",
        "caption": (
            "💙 Feliz Dia dos Namorados!\n\n"
            "A Colchões & Cia deseja que vocês tenham muitas noites de descanso e amor juntos. 🛏\n\n"
            "Obrigado pela confiança! Barretos, a gente ama vocês! 💙\n\n"
            "📍 Rua 20 Esq. Av. 13 - Centro - Barretos\n"
            "📞 (17) 3325-6039\n\n"
            "#FelizDiaDoNamorados #ColchõesCia #Barretos"
        ),
    },
}


def api_post(path: str, data: dict) -> dict:
    url = f"{BASE_URL}/{path}"
    payload = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}: {body[:500]}")
        sys.exit(1)


def publish(image_url: str, caption: str) -> str:
    container = api_post(f"{ACCOUNT_ID}/media", {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN,
    })
    creation_id = container.get("id")
    if not creation_id:
        print(f"Erro ao criar container: {container}")
        sys.exit(1)
    print(f"Container criado: {creation_id}")

    result = api_post(f"{ACCOUNT_ID}/media_publish", {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN,
    })
    return result.get("id", "")


def main():
    brt = timezone(timedelta(hours=-3))
    today = datetime.now(brt).strftime("%d/%m")

    if len(sys.argv) > 1:
        today = sys.argv[1]

    post = POSTS.get(today)
    if not post:
        print(f"Nenhum post agendado para hoje ({today}). Nada a fazer.")
        sys.exit(0)

    print(f"Publicando feed de {today}...")
    post_id = publish(post["image"], post["caption"])
    print(f"✅ Feed publicado! ID: {post_id}")


if __name__ == "__main__":
    main()
