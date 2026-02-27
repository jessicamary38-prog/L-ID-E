import streamlit as st
import google.generativeai as genai

# 1. Configuração da IA (Corrigida para evitar o erro 404)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Alteramos para 'gemini-pro' para garantir compatibilidade
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
        [
            "Fria (Veias Roxas/Azuis)", 
            "Quente (Veias Verdes)", 
            "Oliva (Fundo frio com tom amarelado)",
            "Neutra"
        ]
    )
    
    st.subheader("✨ Essências Faciais")
    col_ess1, col_ess2 = st.columns(2)
    with col_ess1:
        r1 = st.selectbox("Formato do Rosto", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
        r2 = st.selectbox("Boca", ["Carnuda/Arredondada", "Larga/Aberta", "Pequena", "Fina"])
    with col_ess2:
        r3 = st.selectbox("Nariz", ["Pequeno", "Longo", "Largo", "Proporcional"])
        r4 = st.selectbox("Olhos", ["Redondos", "Rasgados", "Amendoados", "Médios"])

    st.subheader("📏 Estrutura Corporal (Kibbe)")
    altura = st.number_input("Altura (ex: 1.60)", min_value=1.0, max_value=2.5, value=1.60, step=0.01)
    p1 = st.selectbox("Estrutura Óssea", ["Estreita", "Larga", "Simétrica"])
    curva = st.radio("Presença de Curvas nítidas?", ["Sim", "Não"])
    carne = st.selectbox("Textura da Carne", ["Densa/Firme", "Macia/Suave"])

    st.subheader("🧠 Temperamento")
    e1 = st.radio("Recarga de Energia", ["Pessoas/Ação (Extrovertido)", "Sozinha/Reflexão (Introvertido)"])
    e2 = st.radio("Tomada de Decisão", ["Racional/Lógica", "Emocional/Sentimento"])

    submeter = st.form_submit_button("GERAR DOSSIÊ DE ESTILO")

if submeter:
    # Lógica de processamento interna...
    with st.spinner("Mestre Visagista processando análise 360º..."):
        prompt = f"""
        Aja como Mestre Visagista da Maison L'IDÉE. Cliente: {nome}.
        PRIORIDADE: Coloração {temperatura_pele}. 
        Kibbe, Essências ({r1}, {r2}, {r3}, {r4}) e Temperamento.
        Crie um diagnóstico de luxo. Se Oliva, destaque o fundo frio.
        """
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.divider()
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
        except:
            st.error("Erro ao gerar. Verifique se a chave API nos Secrets está correta.")
