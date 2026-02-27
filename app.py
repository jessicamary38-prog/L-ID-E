import streamlit as st
import google.generativeai as genai

# Configuração da IA com tratamento de erro
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Chave API não encontrada nos Secrets do Streamlit.")
except Exception as e:
    st.error(f"Erro ao configurar IA: {e}")

st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")
st.title("⚜️ L'IDÉE MAISON - Diagnóstico de Visagismo")

# --- QUESTIONÁRIO ---
with st.form("meu_formulario"):
    st.subheader("Características Físicas")
    formato_rosto = st.selectbox("Qual o formato do seu rosto?", ["Oval", "Redondo", "Quadrado", "Coração", "Diamante", "Retangular"])
    olhos = st.selectbox("Como são seus olhos?", ["Amendoados", "Arredondados", "Caídos", "Pequenos", "Proeminentes"])
    nariz = st.selectbox("Qual o formato do seu nariz?", ["Fino/Reto", "Largo", "Adunco", "Arrebitado", "Sinuoso"])
    
    st.subheader("Análise de Temperamento")
    # ESTA É A PARTE QUE ESTAVA FALTANDO:
    temperamento = st.radio("Com qual temperamento você mais se identifica?", 
                             ["Sanguíneo (Extrovertido e Comunicativo)", 
                              "Melancólico (Analítico e Detalhista)", 
                              "Colérico (Determinado e Líder)", 
                              "Fleumático (Calmo e Diplomático)"])
    
    objetivo = st.text_area("Qual mensagem você deseja passar com sua imagem?")
    submeter = st.form_submit_button("GERAR DIAGNÓSTICO MESTRE")

# --- RESPOSTA ---
if submeter:
    with st.spinner("Consultando o Mestre Visagista..."):
        prompt = f"Aja como um visagista de luxo da Maison L'IDÉE. Analise: Rosto {formato_rosto}, Olhos {olhos}, Nariz {nariz}, Temperamento {temperamento}. Objetivo: {objetivo}."
        try:
            response = model.generate_content(prompt)
            st.markdown("### ⚜️ Seu Diagnóstico")
            st.write(response.text)
            st.divider()
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
        except Exception as e:
            st.error("Erro ao gerar resposta. Verifique sua Chave API nos Secrets.")
