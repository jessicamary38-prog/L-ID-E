import streamlit as st
import google.generativeai as genai

# Configuração da Inteligência Artificial
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Erro na configuração da Chave API. Verifique os Secrets.")

st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")

st.title("⚜️ L'IDÉE MAISON - Diagnóstico de Visagismo")
st.write("Descubra a essência da sua imagem pessoal através do nosso mestre visagista.")

# --- QUESTIONÁRIO COMPLETO ---
with st.form("meu_formulario"):
    st.subheader("Características Físicas")
    formato_rosto = st.selectbox("Qual o formato do seu rosto?", ["Oval", "Redondo", "Quadrado", "Coração", "Diamante", "Retangular"])
    olhos = st.selectbox("Como são seus olhos?", ["Amendoados", "Arredondados", "Caídos", "Pequenos", "Proeminentes"])
    
    # Campo do nariz restaurado
    nariz = st.selectbox("Qual o formato do seu nariz?", ["Fino/Reto", "Largo", "Adunco", "Arrebitado", "Sinuoso"])
    
    st.subheader("Análise Psicológica")
    # Campo dos temperamentos restaurado
    temperamento = st.radio("Com qual temperamento você mais se identifica?", 
                             ["Sanguíneo (Extrovertido/Alegre)", 
                              "Melancólico (Analítico/Sério)", 
                              "Colérico (Líder/Determinado)", 
                              "Fleumático (Calmo/Paciente)"])
    
    objetivo = st.text_area("Qual mensagem você deseja passar com sua imagem? (Ex: Autoridade, Acessibilidade, Criatividade)")

    submeter = st.form_submit_button("GERAR DIAGNÓSTICO MESTRE")

# --- LÓGICA DE RESPOSTA DA IA ---
if submeter:
    with st.spinner("A Maison está analisando seu perfil..."):
        prompt = f"""
        Você é um mestre visagista de luxo da Maison L'IDÉE. 
        Analise estas características: 
        Rosto: {formato_rosto}, Olhos: {olhos}, Nariz: {nariz}, Temperamento: {temperamento}.
        Objetivo: {objetivo}.
        Dê um diagnóstico detalhado, elegante e sugira melhorias na imagem. 
        Seja sofisticado na linguagem.
        """
        try:
            response = model.generate_content(prompt)
            st.markdown("### ⚜️ Seu Diagnóstico Exclusivo")
            st.write(response.text)
            
            # --- ÁREA DE PAGAMENTO ---
            st.divider()
            st.info("Para um cronograma completo e consultoria personalizada, finalize sua reserva abaixo:")
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
            
        except Exception as e:
            st.error("Houve um erro ao processar seu diagnóstico. Verifique sua conexão ou a Chave API.")
