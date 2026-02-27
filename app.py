import streamlit as st
import google.generativeai as genai

# Configuração de Luxo L'IDÉE MAISON
st.set_page_config(page_title="L'IDÉE MAISON", page_icon="⚜️", layout="centered")

# Estilização Visual (Agora com botão de pagamento destacado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: #1a1a1a; text-align: center; }
    .stButton>button { background-color: #1a1a1a; color: white; border-radius: 0px; width: 100%; height: 50px; font-weight: bold; }
    .pay-button { 
        display: inline-block; padding: 15px 25px; background-color: #00A1E4; color: white !important; 
        text-decoration: none; border-radius: 5px; font-weight: bold; text-align: center; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚜️ L'IDÉE MAISON")
st.markdown("<p style='text-align: center; font-style: italic;'>L'Intelligence de l'Essence - Diagnóstico 360º</p>", unsafe_allow_html=True)

# Conexão com a IA
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.warning("Sistema em fase de ativação. Verifique as chaves de segurança.")

# --- FORMULÁRIO ---
with st.form("consultoria_lidee"):
    nome = st.text_input("Nome da Cliente:")
    altura = st.number_input("Altura (ex: 1.65)", min_value=1.0, max_value=2.5, step=0.01)
    
    col1, col2 = st.columns(2)
    with col1:
        ossatura = st.selectbox("Estrutura Óssea:", ["Estreita", "Larga", "Simétrica"])
        curva = st.radio("Presença de Curvas?", ["Sim", "Não"])
        pele = st.selectbox("Subtom de Pele:", ["Frio (Veias Azuis)", "Quente (Veias Verdes)", "Oliva (Veias Cinzas)"])
    
    with col2:
        carne = st.selectbox("Textura da Carne:", ["Densa/Firme", "Macia/Suave"])
        rosto = st.selectbox("Formato do Rosto:", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
        temp = st.selectbox("Temperamento:", ["Melancólico", "Sanguíneo", "Colérico", "Fleumático"])

    submit = st.form_submit_button("GERAR DIAGNÓSTICO MESTRE")

if submit:
    if not nome:
        st.error("Por favor, insira o nome da cliente.")
    else:
        # Prompt Estruturado
        prompt = f"""
        Aja como a especialista da Maison L'IDÉE. Analise: Nome {nome}, Altura {altura}, Rosto {rosto}, Pele {pele}, Temperamento {temp}.
        REGRAS: 
        1. Se Pele Quente + Melancólico: PROIBIR GRAFITE. Recomendar Marrom Café.
        2. Se Pele Oliva: Recomendar Ouro Envelhecido.
        3. Tom de voz: Luxuoso, sofisticado e técnico.
        Finalize dizendo que este é um diagnóstico preliminar.
        """
        
        with st.spinner('A Maison está analisando sua essência...'):
            response = model.generate_content(prompt)
            st.markdown("---")
            st.subheader(f"Dossiê de {nome}")
            st.markdown(response.text)
        
        st.markdown("---")
        # ÁREA DE PAGAMENTO
        st.subheader("⚜️ Eleve sua Imagem ao Próximo Nível")
        st.write("Deseja receber seu **Dossiê Completo L'IDÉE** (20+ páginas) com cartela de cores, sugestões de cortes e acessórios específicos para sua essência?")
        
        st.markdown(f'''
            <a href="https://mpago.la/2FcahRg" target="_blank" class="pay-button">
                ADQUIRIR DOSSIÊ COMPLETO - R$ (Valor do seu Link)
            </a>
        ''', unsafe_allow_html=True)
        st.caption("Ao clicar, você será redirecionada para o Mercado Pago com total segurança.")
