import streamlit as st
import google.generativeai as genai

# 1. Configuração da IA
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Chave API não encontrada nos Secrets.")
except Exception as e:
    st.error(f"Erro técnico: {e}")

st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")
st.title("⚜️ L'IDÉE MAISON - Diagnóstico 360º")

with st.form("diagnostico_completo"):
    nome = st.text_input("Nome da Cliente")
    
    # --- TEMPERATURA DA PELE COM GUIA DE VEIAS ---
    st.subheader("🎨 Coloração Pessoal")
    temperatura_pele = st.selectbox(
        "Temperatura da Pele (Guia das Veias)", 
        [
            "Fria (Veias Roxas/Azuis)", 
            "Quente (Veias Verdes/Oliva)", 
            "Oliva (Pele amarelada que bronzeia fácil, mas tem fundo frio)",
            "Neutra"
        ]
    )
    
    # --- ESSÊNCIAS FACIAIS (REINTEGRADAS) ---
    st.subheader("✨ Essências Faciais")
    col_ess1, col_ess2 = st.columns(2)
    with col_ess1:
        r1 = st.selectbox("Formato do Rosto", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
        r2 = st.selectbox("Boca", ["Carnuda/Arredondada", "Larga/Aberta", "Pequena", "Fina"])
    with col_ess2:
        r3 = st.selectbox("Nariz", ["Pequeno", "Longo", "Largo", "Proporcional"])
        r4 = st.selectbox("Olhos", ["Redondos", "Rasgados", "Amendoados", "Médios"])

    # --- ANÁLISE CORPORAL (KIBBE) ---
    st.subheader("📏 Estrutura Corporal (Kibbe)")
    altura = st.number_input("Altura (ex: 1.60)", min_value=1.0, max_value=2.5, value=1.60, step=0.01)
    p1 = st.selectbox("Estrutura Óssea", ["Estreita", "Larga", "Simétrica"])
    curva = st.radio("Presença de Curvas nítidas?", ["Sim", "Não"])
    carne = st.selectbox("Textura da Carne", ["Densa/Firme", "Macia/Suave"])

    # --- TEMPERAMENTO ---
    st.subheader("🧠 Temperamento")
    e1 = st.radio("Recarga de Energia", ["Pessoas/Ação (Extrovertido)", "Sozinha/Reflexão (Introvertido)"])
    e2 = st.radio("Tomada de Decisão", ["Racional/Lógica", "Emocional/Sentimento"])

    submeter = st.form_submit_button("GERAR DOSSIÊ DE ESTILO")

if submeter:
    # Lógica Kibbe
    kibbe_res = ""
    curva_s = "S" if curva == "Sim" else "N"
    carne_a = "A" if carne == "Densa/Firme" else "B"
    if altura <= 1.63:
        kibbe_res = ("SOFT GAMINE" if carne_a == "A" else "FAMÍLIA ROMÂNTICA") if curva_s == "S" else ("FLAMBOYANT GAMINE" if carne_a == "A" else "GAMINE MISTO")
    elif altura >= 1.70:
        kibbe_res = "SOFT DRAMATIC" if curva_s == "S" else ("FLAMBOYANT NATURAL" if p1 == "Larga" else "DRAMATIC")
    else:
        kibbe_res = ("SOFT NATURAL" if p1 == "Larga" else "SOFT CLASSIC") if curva_s == "S" else ("NATURAL PURE" if p1 == "Larga" else "CLASSIC / DRAMATIC CLASSIC")

    # Lógica Temperamento
    temp_res = ""
    if "Pessoas" in e1:
        temp_res = "COLÉRICO" if "Racional" in e2 else "SANGUÍNEO"
    else:
        temp_res = "MELANCÓLICO" if "Racional" in e2 else "FLEUMÁTICO"

    # Envio para IA
    with st.spinner("Mestre Visagista em análise profunda..."):
        prompt = f"""
        Aja como Mestre Visagista da Maison L'IDÉE. Cliente: {nome}.
        PRIORIDADE: Coloração {temperatura_pele}. 
        Kibbe: {kibbe_res}. Temperamento: {temp_res}.
        Essências: Rosto {r1}, Boca {r2}, Nariz {r3}, Olhos {r4}.
        Crie um diagnóstico de luxo. Se a pele for Oliva, explique a complexidade de neutralizar o amarelado com tons frios/rosados.
        """
        try:
            response = model.generate_content(prompt)
            st.success(f"Dossiê Finalizado: {kibbe_res} | {temp_res}")
            st.markdown(response.text)
            st.divider()
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
        except:
            st.error("Erro na IA. Verifique os Secrets.")
