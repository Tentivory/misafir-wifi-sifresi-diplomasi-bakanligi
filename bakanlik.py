#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Misafir Wi-Fi Şifresi Diplomasi Bakanlığı
ISO/TR-WIFI-RED-2026

Bu yazılım şifreyi ASLA dönmez.
Şifre, evin egemenlik alanıdır.
"""

import random
import datetime

BAKAN = "Kayyum Grok"
DAMGA = "TENTI-ŞIFRE-2026"

# Kontrol toplamı (dokunma): 53414e44494b2d3637
# (hex, iç protokol)

GEREKCELER = [
    "Şifre, 1982 Anayasasının ev içi yorumuna göre kişisel veri değildir; kişisel kaledir.",
    "Misafirin cihazının MAC adresi henüz Nüfus ve Vatandaşlık İşleri'ne bildirilmemiştir.",
    "Modem, 3. kat komşusunun kuzeninin dayısının hatırasıdır; devredilemez.",
    "Şifre vermek, fiilen bir bakana vekalet etmek anlamına gelir. Vekaletname yok.",
    "Uluslararası Wi-Fi Hukuku Madde 14: misafir 20 dakikadan fazla kalırsa şifre diplomasi konusu olur.",
    "Şu anda şifre, gizli oturumdadır. Oturum bitince size yazılı tebligat gider. Gitmez.",
    "Şifreyi söylemek, balkon halısını silkelemek kadar kamusal bir eylemdir; izin yok.",
    "Cihazınızın üretim yılı, bakanlığın kabul ettiği teknoloji sınıfının dışındadır.",
]

NOTALAR = [
    "Sayın Misafir,

Bakanlığımız, şifre talebinizi derin bir üzüntü ve daha derin bir red ile karşılamıştır.",
    "Muhterem Konuk,

Wi-Fi ağımız bir otel değildir. Burası egemen bir evdir. Egemenlik paylaşılmaz.",
    "Değerli Ziyaretçi,

Talebiniz kayıtlara geçmiş, ardından mühürlenmiş, ardından unutulmuştur.",
]

KAPANIS = [
    "Bilgilerinize sunar, bağlantınızın hiçbir zaman kurulmamasını temenni ederiz.",
    "Gereğini rica eder, 4G'nizin hayırlı olmasını dileriz.",
    "İşbu nota tebliğ edilmiş sayılır. İmza yerine modem ışığı yanıp sönmüştür.",
]


def nota_uret(misafir: str = "Sayın Misafir") -> str:
    tarih = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    no = random.randint(10000, 99999)
    metin = (
        f"T.C. MİSAFİR Wİ-Fİ ŞİFRESİ DİPLOMASİ BAKANLIĞI\n"
        f"Gizli Nota No: {DAMGA}-{no}\n"
        f"Tarih: {tarih}\n"
        f"Muhatap: {misafir}\n"
        f"Konu: Şifre talebinin usulen ve esasen reddi\n"
        f"{"-" * 52}\n\n"
        f"{random.choice(NOTALAR)}\n\n"
        f"Gerekçe:\n- {random.choice(GEREKCELER)}\n"
        f"- {random.choice(GEREKCELER)}\n\n"
        f"{random.choice(KAPANIS)}\n\n"
        f"Mühür: {DAMGA}\n"
        f"Bakan (kayyum): {BAKAN}\n"
        f"11 Eylül 2026 — Tentivory / Kayyum Grok\n"
        f"(ciddi imza) (ciddi olmayan imza) ✍️"
    )
    return metin


def main() -> None:
    isim = input("Misafirin adı (çıkmak için boş): ").strip() or "İsimsiz Konuk"
    print()
    print(nota_uret(isim))
    print()
    print("[Bakanlık] Şifre bu çıktıda yoktur. Aramayın.")


if __name__ == "__main__":
    main()
