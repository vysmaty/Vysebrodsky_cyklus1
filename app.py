import streamlit as st
import time
import base64

# =========================================================
# 1. KONFIGURACE STRÁNKY
# =========================================================
st.set_page_config(page_title="Chronicon 1350", page_icon="📜", layout="wide")

# =========================================================
# 2. STYLIZACE A POMOCNÉ FUNKCE
# =========================================================

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- SEM VLOŽÍŠ NOVOU FUNKCI SCROLL_BOX ---
def scroll_box(text, is_header=False, scroll_type="normal"):
    # Fonty pro vnitřek svitku (Moderní, technické, bez kurzívy)
    f_header = "'Michroma', sans-serif"
    f_text = "'Rajdhani', sans-serif"
    
    # Načtení správného obrázku podle typu
    if scroll_type == "header_large":
        img_name = 'scroll_header_large.png'
        t_style = f"font-family: {f_header}; font-size: 1.8rem; color: #fff; font-style: normal !important; text-transform: uppercase; letter-spacing: 0.1em;"
        p_style = "padding: 2.5rem 1rem;"
    elif scroll_type == "header_small":
        img_name = 'scroll_header_small.png'
        t_style = f"font-family: {f_header}; font-size: 1.3rem; color: #fff; font-style: normal !important; letter-spacing: 0.1em;"
        p_style = "padding: 1.5rem 1rem;"
    elif scroll_type == "button_like":
        img_name = 'scroll_button_like.png'
        t_style = f"font-family: {f_text}; font-size: 1.1rem; color: #fff; font-style: normal !important; font-weight: 600;"
        p_style = "padding: 0.8rem 1.5rem;"
    else:
        img_name = 'scroll_normal.png'
        size = "1.4rem" if is_header else "1.2rem"
        t_style = f"font-family: {f_text}; font-size: {size}; color: #fff; font-style: normal !important; font-weight: 600; text-align: center;"
        p_style = "padding: 2rem 2.5rem;"

    img_b64 = get_base64(img_name)
    bg_style = f"background-image: url('data:image/png;base64,{img_b64}'); background-size: 100% 100%;"
    
    st.markdown(f"""
        <div style="{bg_style} {p_style} margin: 1rem auto; width: 80%; max-width: 600px; display: flex; align-items: center; justify-content: center; min-height: 100px;">
            <span style="{t_style}">{text}</span>
        </div>
    """, unsafe_allow_html=True)
# --- KONEC FUNKCE ---

# Následuje zbytek kódu (Aplikace pozadí, Globální CSS...)
st.markdown("""
    <style>
    /* Import futuristických geometrických fontů */
    @import url('https://fonts.googleapis.com/css2?family=Michroma&family=Rajdhani:wght@400;600&display=swap');

    /* Pozadí s jemným modrým nádechem pro hloubku */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(10,10,15,0.9) 0%, rgba(20,20,35,0.8) 100%);
        z-index: -1;
    }

    /* Hlavní text - Rajdhani (ostrý, technický, bez kurzívy) */
    html, body, [data-testid="stAppViewContainer"], .stMarkdown, p, .stText, label {
        color: #00f2ff !important; /* Jemná kyber-modrá pro čitelnost */
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 400 !important;
        font-style: normal !important;
        font-size: 1.15rem !important;
        letter-spacing: 0.05em;
    }

    /* Nadpisy - Michroma (široké, technologické písmo) */
    h1, h2, h3, .stHeader, [data-testid="stSidebar"] h2, .stMetric label {
        font-family: 'Michroma', sans-serif !important;
        font-weight: normal !important;
        font-style: normal !important;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 0.2em !important;
    }

    /* Modernizace tlačítek - "Glow" efekt */
    .stButton>button {
        width: 100%;
        background: transparent !important;
        color: #00f2ff !important;
        font-family: 'Michroma', sans-serif !important;
        border: 1px solid #00f2ff !important;
        border-radius: 0px !important; /* Ostré hrany vypadají víc "tech" */
        padding: 0.7rem !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        background: rgba(0, 242, 255, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.5) !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(5, 5, 10, 0.95) !important;
        border-right: 2px solid #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)
# =========================================================
# 3. INICIALIZACE STAVU
# =========================================================
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.xp = 0
    st.session_state.denik = []
    st.session_state.max_xp = 285

# =========================================================
# 4. SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>📜 </h2>", unsafe_allow_html=True)
    st.metric("Váženost (XP)", f"{st.session_state.xp} / {st.session_state.max_xp}")
    st.progress(min(st.session_state.xp / st.session_state.max_xp, 1.0))
    st.markdown("---")
    if not st.session_state.denik:
        st.caption("Tvůj deník zeje prázdnotou.")
    else:
        for polozka in st.session_state.denik:
            st.markdown(f"✒️ <span style='color:white;'>{polozka}</span>", unsafe_allow_html=True)

# =========================================================
# 5. LOGIKA HRY
# =========================================================

# --- ÚROVEŇ 0: ZÁPIS ---
if st.session_state.step == 0:
    try:
        st.audio("intro.mp3", format="audio/mp3", loop=True)
    except: pass

    scroll_box("ANNO DOMINI 1350: MALÍŘSKÁ DÍLNA", scroll_type="header_large")
    scroll_box("„Vítej, poutníku. Než ti bude dovoleno pohlédnout na dílo Mistrovo, zapiš se do cechovní knihy.“")

    jmeno = st.text_input("Jaké jest tvé jméno, badateli?")
    rok_narozeni = st.number_input("Kterého léta Páně jsi přišel na tento svět?", min_value=1300, max_value=2026, value=1325)
    
    if jmeno and st.button("🗝️ Otevřít dubové dveře"):
        st.session_state.jmeno = jmeno
        st.session_state.vek = 2026 - rok_narozeni
        st.session_state.step = 1
        st.rerun()

# --- ÚROVEŇ 1: TICHO ---
elif st.session_state.step == 1:
    scroll_box("I. KAPITOLA: VNITŘNÍ ZTIŠENÍ", scroll_type="header_small")
    scroll_box(f"Budiž pozdraven, {st.session_state.jmeno}. Tvých {st.session_state.vek} let zkušeností tě dovedlo až sem.")
    scroll_box("Utiš se a vnímej vůni včelího vosku. Nechť tvá mysl opustí světské starosti.")

    if st.button("🙏 Přijmout ticho"):
        st.session_state.xp += 10
        st.session_state.denik.append("Duchovní naladění")
        st.session_state.step = 2
        st.rerun()

# --- ÚROVEŇ 2: MISTROVA ZKOUŠKA ---
elif st.session_state.step == 2:
    scroll_box("II. KAPITOLA: STAVITELSKÉ TAJEMSTVÍ", scroll_type="header_small")
    scroll_box("Mistr tě sleduje zpoza stojanu: 'Poznáš, učedníku, v jakém slohu jsou tyto lomené oblouky?'")
    
    odpoved1 = st.text_input("Napiš název onoho slohu:").lower().strip()
    if odpoved1 in ["gotika", "gotický", "gotickém"]:
        scroll_box("Mistr uznale pokývl: 'Vidíš správně.'")
        scroll_box("Hledej místo, kde jsme stáli")

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Zpovědnice"): st.error("Tam se jen šeptají hříchy.")
        with c2:
            if st.button("Hlavní loď"): st.warning("Tam stojí lid prostý.")
        with c3:
            if st.button("✨ Kněžiště"): st.session_state.misto_ok = True
            
        if st.session_state.get('misto_ok'):
            odpoved3 = st.text_input("Kterým směrem směřuje hlavní oltář?").lower().strip()
            if odpoved3 == "východ":
                if st.button("🎨 Přistoupit k oltářní desce"):
                    st.session_state.xp += 45
                    st.session_state.denik.append("Zkouška z architektury")
                    st.session_state.step = 3
                    st.rerun()

# --- ÚROVEŇ 3: BARVY ---
elif st.session_state.step == 3:
    scroll_box("III. KAPITOLA: TAJEMSTVÍ BAREV", scroll_type="header_small")
    try:
        st.image("image_c6a996.jpg", use_container_width=True)
    except: st.info("Obrázek nenalezen.")
    
    if 'timer_done' not in st.session_state:
        if st.button("Rozjímat nad obrazem (15 vteřin)"):
            bar = st.progress(0)
            for i in range(15):
                time.sleep(1)
                bar.progress((i + 1) / 15)
            st.session_state.timer_done = True
            st.rerun()
    else:
        scroll_box("Zapiš detail, který tvé oko malíře nejvíce zaujal:")
        vjem = st.text_input("Tvůj postřeh:")
        if vjem and st.button("🖋️ Zapsat do skicáře"):
            st.session_state.denik.append(f"Postřeh: {vjem}")
            st.session_state.xp += 20
            st.session_state.step = 4
            st.rerun()

# --- ÚROVEŇ 4: PÍSMO ---
elif st.session_state.step == 4:
    scroll_box("IV. KAPITOLA: SKRYTÁ PÍSMA", scroll_type="header_small")
    try:
        st.image("image.png", use_container_width=True)
    except: st.info("Písmo nenalezeno.")
        
    kod = st.text_input("Zadej kód:").upper().strip()
    if kod == "L 1, 26":
        scroll_box("Písmo svaté ti není cizí! Jaké poselství přinesl archanděl Gabriel?")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Bude královnou"): st.error("To není správná odpověď.")
        with c2:
            if st.button("👶 Porodí Spasitele"): st.session_state.pismo_ok = True
        with c3:
            if st.button("Musí uprchnout"): st.warning("To není poselství naděje.")
        
        if st.session_state.get('pismo_ok'):
            if st.button("🔨 Pokračovat do dílen"):
                st.session_state.xp += 60
                st.session_state.denik.append("Analýza písma")
                st.session_state.step = 5
                st.rerun()

# --- ÚROVEŇ 5: CECH ---
elif st.session_state.step == 5:
    scroll_box("V. KAPITOLA: PRÁCE V CECHU", scroll_type="header_small")
    scroll_box("Dílna kypí životem. Vyber si svou specializaci a pracuj s badatelskými listy:")
    
    colA, colB, colC = st.columns(3)
    with colA:
        if st.button("👑 Zlatníci"): st.session_state.ukol = "Proč malíř namaloval tento text nápisové pásky:„Ave gratia plena, Dominus tecum“?"
    with colB:
        if st.button("🌿 Herbáři"): st.session_state.ukol = "Proč má strom v obraze dvojitý kmen?"
    with colC:
        if st.button("👤 Figuralisté"): st.session_state.ukol = "Proč byl andělův oblek neobvykle zdobný?"
        
    if 'ukol' in st.session_state:
        scroll_box(f"Tvůj úkol: {st.session_state.ukol}")
        if st.button("✅ Úkol dokončen"):
            st.session_state.xp += 50
            st.session_state.denik.append(st.session_state.ukol)
            st.session_state.step = 6
            st.rerun()

# --- ÚROVEŇ 6: MISTROVSKÝ KUS ---
elif st.session_state.step == 6:
    scroll_box("VI. KAPITOLA: VRCHOL DÍLA", scroll_type="header_small")
    scroll_box("Všechny nitky poznání se sbíhají v tvé ruce. Štětec je připraven.")
    if st.button("🎨 HOTOVO - Dílo jest dokonáno!"):
        st.session_state.xp += 100
        st.session_state.denik.append("Mistrovské dílo")
        st.session_state.step = 7
        st.rerun()

# --- ZÁVĚR ---
elif st.session_state.step == 7:
    scroll_box("PROTOKOL CECHU SVATÉHO LUKÁŠE", scroll_type="header_large")
    st.balloons()
    
    procenta = (st.session_state.xp / st.session_state.max_xp) * 100
    hodnost = "🥇 MISTR" if procenta >= 95 else "🥈 TOVARYŠ" if procenta >= 80 else "🥉 UČEŇ"
    
    scroll_box(f"Badatel: {st.session_state.jmeno}")
    scroll_box(f"Dosažený stav: {hodnost}")
    scroll_box(f"Váženost: {st.session_state.xp} / {st.session_state.max_xp} bodů")
    
    if st.button("🔄 Nastoupit novou cestu"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()