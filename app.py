import streamlit as st
import google.generativeai as genai

# 1. Configuração da IA
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Erro na Chave API. Verifique os Secrets.")

st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")
st.title("⚜️ L'IDÉE MAISON - Diagnóstico 360º")

# --- FORMULÁRIO COM SUA LÓGICA ---
with st.form("diagnostico_completo"):
    nome = st.text_input("Nome da Cliente")
    altura = st.number_input("Altura (ex: 1.60)", min_value=1.0, max_value=2.5, value=1.60, step=0.01)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Análise Corporal")
        p1 = st.selectbox("Estrutura Óssea", ["Estreita", "Larga", "Simétrica"])
        curva = st.radio("Presença de Curvas nítidas?", ["Sim", "Não"])
        carne = st.selectbox("Textura da Carne", ["Densa/Firme", "Macia/Suave"])
        
    with col2:
        st.subheader("Essências Faciais")
        r1 = st.selectbox("Formato do Rosto", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
        r2 = st.selectbox("Boca", ["Carnuda/Arredondada", "Larga/Aberta", "Pequena", "Fina"])
        r3 = st.selectbox("Nariz", ["Pequeno", "Longo", "Largo", "Proporcional"])
        r4 = st.selectbox("Olhos", ["Redondos", "Rasgados", "Amendoados", "Médios"])

    st.subheader("Temperamento")
    e1 = st.radio("Recarga de Energia", ["Pessoas/Ação (Extrovertido)", "Sozinha/Reflexão (Introvertido)"])
    e2 = st.radio("Tomada de Decisão", ["Racional/Lógica", "Emocional/Sentimento"])

    submeter = st.form_submit_button("GERAR DOSSIÊ DE ESTILO")

if submeter:
    # --- PROCESSAMENTO DA SUA LÓGICA (KIBBE) ---
    kibbe_res = ""
    curva_s = "S" if curva == "Sim" else "N"
    carne_a = "A" if carne == "Densa/Firme" else "B"
    
    if altura <= 1.63:
        kibbe_res = ("SOFT GAMINE" if carne_a == "A" else "FAMÍLIA ROMÂNTICA") if curva_s == "S" else ("FLAMBOYANT GAMINE" if carne_a == "A" else "GAMINE MISTO")
    elif altura >= 1.70:
        kibbe_res = "SOFT DRAMATIC" if curva_s == "S" else ("FLAMBOYANT NATURAL" if p1 == "Larga" else "DRAMATIC")
    else:
        kibbe_res = ("SOFT NATURAL" if p1 == "Larga" else "SOFT CLASSIC") if curva_s == "S" else ("NATURAL PURE" if p1 == "Larga" else "CLASSIC / DRAMATIC CLASSIC")

    # --- PROCESSAMENTO TEMPERAMENTO ---
    temp_res = ""
    if "Pessoas" in e1:
        temp_res = "COLÉRICO" if "Racional" in e2 else "SANGUÍNEO"
    else:
        temp_res = "MELANCÓLICO" if "Racional" in e2 else "FLEUMÁTICO"

    # --- ENVIO PARA A IA ---
    with st.spinner("Mestre Visagista processando cálculos..."):
        prompt = f"""
        Aja como Mestre Visagista da Maison L'IDÉE. 
        Cliente: {nome}. 
        Resultado Kibbe: {kibbe_res}. 
        Temperamento: {temp_res}. 
        Características Faciais: Rosto {r1}, Boca {r2}, Nariz {r3}, Olhos {r4}.
        Crie um diagnóstico de luxo explicando como o temperamento e o corpo se unem.
        """
        try:
            response = model.generate_content(prompt)
            st.success(f"Dossiê Pronto: {kibbe_res} | {temp_res}")
            st.markdown(response.text)
            st.divider()
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
        except:
            st.error("Erro ao gerar diagnóstico. Verifique os Secrets.")
