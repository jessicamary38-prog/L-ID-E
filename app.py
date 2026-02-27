import streamlit as st
import google.generativeai as genai

# 1. Configuração da IA (Ajustada para os Secrets)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Chave API não encontrada. Vá em 'Gerenciar aplicativo' > 'Secrets'.")
except Exception as e:
    st.error(f"Erro técnico: {e}")

st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")
st.title("⚜️ L'IDÉE MAISON - Diagnóstico 360º")

# --- FORMULÁRIO COM HIERARQUIA REFORMULADA ---
with st.form("diagnostico_completo"):
    nome = st.text_input("Nome da Cliente")
    
    st.subheader("🎨 Coloração Pessoal (Prioridade Máxima)")
    # A temperatura da pele agora é a primeira e mais importante pergunta
    temperatura_pele = st.selectbox("Temperatura da Pele", ["Quente (Dourada/Amarelada)", "Fria (Rosada/Azulada)", "Neutra"])
    
    st.subheader("📏 Análise Corporal (Kibbe)")
    altura = st.number_input("Altura (ex: 1.60)", min_value=1.0, max_value=2.5, value=1.60, step=0.01)
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.selectbox("Estrutura Óssea", ["Estreita", "Larga", "Simétrica"])
        curva = st.radio("Presença de Curvas nítidas?", ["Sim", "Não"])
    with col2:
        carne = st.selectbox("Textura da Carne", ["Densa/Firme", "Macia/Suave"])
        r1 = st.selectbox("Formato do Rosto", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])

    st.subheader("🧠 Análise Psicológica")
    e1 = st.radio("Recarga de Energia", ["Pessoas/Ação (Extrovertido)", "Sozinha/Reflexão (Introvertido)"])
    e2 = st.radio("Tomada de Decisão", ["Racional/Lógica", "Emocional/Sentimento"])

    submeter = st.form_submit_button("GERAR DOSSIÊ DE ESTILO")

if submeter:
    # --- LÓGICA KIBBE ---
    kibbe_res = ""
    curva_s = "S" if curva == "Sim" else "N"
    carne_a = "A" if carne == "Densa/Firme" else "B"
    
    if altura <= 1.63:
        kibbe_res = ("SOFT GAMINE" if carne_a == "A" else "FAMÍLIA ROMÂNTICA") if curva_s == "S" else ("FLAMBOYANT GAMINE" if carne_a == "A" else "GAMINE MISTO")
    elif altura >= 1.70:
        kibbe_res = "SOFT DRAMATIC" if curva_s == "S" else ("FLAMBOYANT NATURAL" if p1 == "Larga" else "DRAMATIC")
    else:
        kibbe_res = ("SOFT NATURAL" if p1 == "Larga" else "SOFT CLASSIC") if curva_s == "S" else ("NATURAL PURE" if p1 == "Larga" else "CLASSIC / DRAMATIC CLASSIC")

    # --- LÓGICA TEMPERAMENTO ---
    temp_res = ""
    if "Pessoas" in e1:
        temp_res = "COLÉRICO" if "Racional" in e2 else "SANGUÍNEO"
    else:
        temp_res = "MELANCÓLICO" if "Racional" in e2 else "FLEUMÁTICO"

    # --- IA COM FOCO EM TEMPERATURA DA PELE ---
    with st.spinner("Priorizando coloração e biotipo..."):
        prompt = f"""
        Você é o Mestre Visagista da Maison L'IDÉE.
        DIRETRIZ PRINCIPAL: A Temperatura da Pele ({temperatura_pele}) deve dominar as recomendações de cores.
        
        Dados da Cliente {nome}:
        - Pele: {temperatura_pele}
        - Kibbe: {kibbe_res}
        - Temperamento: {temp_res}
        - Rosto: {r1}
        
        Explique por que a temperatura da pele é a base de tudo e como o estilo {kibbe_res} deve ser adaptado a essas cores.
        """
        try:
            response = model.generate_content(prompt)
            st.success(f"Dossiê Finalizado com Sucesso! ✨")
            st.markdown(response.text)
            st.divider()
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
        except:
            st.error("Erro ao gerar. Por favor, reinicie o aplicativo no menu 'Gerenciar'.")
