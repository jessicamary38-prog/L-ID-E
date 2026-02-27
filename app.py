import streamlit as st
import google.generativeai as genai

# 1. Configuração de Segurança e IA
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Erro: Chave API não encontrada nos Secrets do Streamlit.")
except Exception as e:
    st.error(f"Erro ao configurar IA: {e}")

# 2. Configuração da Página
st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️")
st.title("⚜️ L'IDÉE MAISON - Diagnóstico de Visagismo")
st.write("Descubra a essência da sua imagem pessoal através do nosso mestre visagista.")

# 3. Formulário Completo (Unindo todas as informações)
with st.form("meu_formulario"):
    st.subheader("Características Físicas")
    formato_rosto = st.selectbox("Qual o formato do seu rosto?", ["Oval", "Redondo", "Quadrado", "Coração", "Diamante", "Retangular"])
    olhos = st.selectbox("Como são seus olhos?", ["Amendoados", "Arredondados", "Caídos", "Pequenos", "Proeminentes"])
    nariz = st.selectbox("Qual o formato do seu nariz?", ["Fino/Reto", "Largo", "Adunco", "Arrebitado", "Sinuoso"])
    
    st.subheader("Análise de Temperamento e Estilo")
    temperamento = st.radio("Com qual temperamento você mais se identifica?", 
                             ["Sanguíneo (Extrovertido e Comunicativo)", 
                              "Melancólico (Analítico e Detalhista)", 
                              "Colérico (Determinado e Líder)", 
                              "Fleumático (Calmo e Diplomático)"])
    
    objetivo = st.text_area("Qual mensagem você deseja passar com sua imagem? (Ex: Autoridade, Elegância, Acessibilidade)")
    
    submeter = st.form_submit_button("GERAR DIAGNÓSTICO MESTRE")

# 4. Lógica de Resposta e Pagamento
if submeter:
    with st.spinner("O Mestre Visagista está analisando seu perfil..."):
        prompt = f"""
        Aja como um renomado mestre visagista de luxo da Maison L'IDÉE. 
        Analise estas características: 
        Rosto: {formato_rosto}, Olhos: {olhos}, Nariz: {nariz}, Temperamento: {temperamento}.
        Objetivo de Imagem: {objetivo}.
        Forneça um diagnóstico sofisticado, detalhado e sugestões de personalização de imagem.
        """
        try:
            response = model.generate_content(prompt)
            st.markdown("---")
            st.markdown("### ⚜️ Seu Diagnóstico Exclusivo")
            st.write(response.text)
            
            # Área de Finalização
            st.divider()
            st.info("Para um cronograma completo e consultoria personalizada, finalize sua reserva abaixo:")
            st.link_button("ADQUIRIR CONSULTORIA COMPLETA", "https://mpago.la/2FcahRg")
            
        except Exception as e:
            st.error("Não foi possível gerar o diagnóstico. Verifique se a sua GOOGLE_API_KEY está correta nos Secrets.")
