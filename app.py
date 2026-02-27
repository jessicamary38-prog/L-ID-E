import streamlit as st
import google.generativeai as genai

# Configuração de Luxo L'IDÉE MAISON
st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️", layout="centered")

# Estilização Visual
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: #1a1a1a; text-align: center; }
    .stButton>button { background-color: #1a1a1a; color: white; border-radius: 0px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚜️ L'IDÉE MAISON")
st.markdown("<p style='text-align: center;'>L'Intelligence de l'Essence</p>", unsafe_allow_html=True)

# Conexão Segura com a IA
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Aguardando configuração da Chave de Segurança (API KEY)...")

# --- QUESTIONÁRIO INTEGRADO ---
with st.form("consultoria_360"):
    nome = st.text_input("Nome da Cliente:")
    altura = st.number_input("Altura (ex: 1.60)", min_value=1.0, max_value=2.5, step=0.01)
    
    col1, col2 = st.columns(2)
    with col1:
        ossatura = st.selectbox("Estrutura Óssea:", ["A) Estreita", "B) Larga", "C) Simétrica"])
        curva = st.radio("Presença de Curvas?", ["Sim", "Não"])
        pele = st.selectbox("Subtom de Pele:", ["Frio (Veias Azuis)", "Quente (Veias Verdes)", "Oliva (Veias Cinzas)"])
    
    with col2:
        carne = st.selectbox("Textura da Carne:", ["Densa/Firme", "Macia/Suave"])
        rosto = st.selectbox("Formato do Rosto:", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
        temp = st.selectbox("Temperamento:", ["Melancólico", "Sanguíneo", "Colérico", "Fleumático"])

    submit = st.form_submit_button("GERAR DIAGNÓSTICO MESTRE")

if submit:
    # Lógica do Kibbe simplificada para o Prompt
    diagnostico_base = f"Cliente {nome}, Altura {altura}, Rosto {rosto}, Pele {pele}, Temperamento {temp}."
    
    prompt = f"""
    Aja como a especialista da Maison L'IDÉE. Analise os dados: {diagnostico_base}.
    REGRAS MESTRE:
    1. Se Pele Quente + Melancólico: PROIBIR GRAFITE. Recomendar Marrom Café.
    2. Se Pele Oliva: Recomendar Ouro Envelhecido.
    3. Se Rosto Longo: Recomendar Franja Cortininha, proibir Pixie.
    4. Tom de voz: Luxuoso, francês, técnico.
    """
    
    response = model.generate_content(prompt)
    st.markdown("---")
    st.markdown(response.text)
    st.info("⚜️ Dossiê gerado pela inteligência L'IDÉE MAISON.")
