import streamlit as st
import google.generativeai as genai

# 1. Configuração da IA (Modelo alterado para GEMINI-PRO para evitar Erro 404)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # O modelo 'gemini-pro' é o que resolverá o erro do log
        model = genai.GenerativeModel('gemini-pro')
    else:
        st.error("Chave API não encontrada nos Secrets.")
except Exception as e:
    st.error(f"Erro na conexão: {e}")

st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")
st.title("⚜️ L'IDÉE MAISON - Diagnóstico 360º")

with st.form("diagnostico_completo"):
    nome = st.text_input("Nome da Cliente")
    
    st.subheader("🎨 Coloração Pessoal (Prioridade)")
    temperatura_pele = st.selectbox(
        "Temperatura da Pele (Guia das Veias)", 
        ["Fria (Veias Roxas/Azuis)", "Quente (Veias Verdes)", "Oliva (Fundo frio/Tom amarelado)", "Neutra"]
    )
    
    st.subheader("✨ Essências Faciais")
    col1, col2 = st.columns(2)
    with col1:
        r1 = st.selectbox("Formato do Rosto", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
        r2 = st.selectbox("Boca", ["Carnuda/Arredondada", "Larga/Aberta", "Pequena", "Fina"])
    with col2:
        r3 = st.selectbox("Nariz", ["Pequeno", "Longo", "Largo", "Proporcional"])
        r4 = st.selectbox("Olhos", ["Redondos", "Rasgados", "Amendoados", "Médios"])

    st.subheader("📏 Estrutura Corporal (Kibbe)")
    altura = st.number_input("Altura (ex: 1.60)", min_value=1.0, max_value=2.5, value=1.60, step=0.01)
    p1 = st.selectbox("Estrutura Óssea", ["Estreita", "Larga", "Simétrica"])
    curva = st.radio("Presença de Curvas?", ["Sim", "Não"])
    carne = st.selectbox("Textura da Carne", ["Densa/Firme", "Macia/Suave"])

    st.subheader("🧠 Temperamento")
    e1 = st.radio("Recarga de Energia", ["Pessoas/Ação (Extrovertido)", "Sozinha/Reflexão (Introvertido)"])
    e2 = st.radio("Tomada de Decisão", ["Racional/Lógica", "Emocional/Sentimento"])

    submeter = st.form_submit_button("GERAR DOSSIÊ DE ESTILO")

if submeter:
    with st.spinner("O Mestre Visagista está redigindo seu diagnóstico..."):
        prompt = f"""
        Você é o Mestre Visagista da Maison L'IDÉE. Analise {nome}.
        Prioridade: Pele {temperatura_pele}. 
        Considere Kibbe, Essências (Rosto {r1}, Boca {r2}, Nariz {r3}, Olhos {r4}) e Temperamento.
        Crie um dossiê de luxo.
        """
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.divider()
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
        except Exception as e:
            st.error(f"Erro técnico: {e}. Verifique se a chave nos Secrets está ativa.")
