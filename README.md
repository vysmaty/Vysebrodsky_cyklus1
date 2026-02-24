# Chronicon 1350: Malířská Dílna

Vítejte v "Chronicon 1350", interaktivní vzdělávací hře postavené na platformě Streamlit. Přeneste se do roku 1350 a vžijte se do role učedníka v malířské dílně, kde vás čeká série úkolů a hádanek prověřujících vaše znalosti z dějin umění, architektury a teologie.

Aplikace kombinuje historický narativ s unikátním "techno-gotickým" vizuálním stylem.

## 📜 Koncept

Jako badatel a učedník procházíte šesti kapitolami, které symbolizují cestu za poznáním středověkého díla. Každá kapitola představuje zkoušku:

1.  **Vnitřní ztišení:** Duchovní příprava na cestu.
2.  **Stavitelské tajemství:** Test znalostí gotické architektury.
3.  **Tajemství barev:** Zkouška malířského vhledu a pozorovacích schopností.
4.  **Skrytá písma:** Analýza a pochopení biblických odkazů v umění.
5.  **Práce v cechu:** Plnění specializovaného úkolu.
6.  **Vrchol díla:** Symbolické dokončení mistrovského díla.

Během hry sbíráte body váženosti (XP) a vaše úspěchy se zapisují do osobního deníku. Na konci jste vyhodnoceni a obdržíte titul – Učeň, Tovaryš, nebo Mistr.

## ✨ Funkce

-   **Příběhová hratelnost:** Interaktivní vyprávění vás provede dílnou Mistra Vyšebrodského cyklu.
-   **Vzdělávací obsah:** Hra zábavnou formou představuje prvky gotického umění.
-   **Systém postupu:** Sledujte svůj pokrok pomocí bodů zkušeností (XP) a zápisků v deníku.
-   **Unikátní UI:** Futuristický design s vlastními fonty, barvami a stylizovanými komponentami, které připomínají svitky.
-   **Atmosférický doprovod:** Podkresová hudba pro hlubší ponoření do hry.

## 🛠️ Technický přehled

-   **Jazyk:** Python
-   **Framework:** Streamlit

## 🚀 Instalace a spuštění

Pro spuštění aplikace na vašem lokálním stroji postupujte podle následujících kroků:

**1. Klonování repozitáře:**
```bash
git clone <URL_VAŠEHO_REPOZITÁŘE>
cd <NÁZEV_SLOŽKY>
```

**2. Vytvoření a aktivace virtuálního prostředí:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Instalace závislostí:**
Aplikace vyžaduje balíček `streamlit`. Nainstalujte jej pomocí přiloženého souboru:
```bash
pip install -r requirements.txt
```

**4. Příprava souborů:**
Ujistěte se, že v hlavní složce projektu máte následující soubory, které jsou nezbytné pro správný chod aplikace:
- `intro.mp3` (hudba pro úvod)
- `image_c6a996.jpg` (obrázek pro 3. kapitolu)
- `image.png` (obrázek pro 4. kapitolu)
- `scroll_header_large.png` (obrázek svitku)
- `scroll_header_small.png` (obrázek svitku)
- `scroll_normal.png` (obrázek svitku)
- `scroll_button_like.png` (obrázek svitku)

**5. Spuštění aplikace:**
```bash
streamlit run app.py
```
Po spuštění příkazu se aplikace otevře ve vašem webovém prohlížeči.
