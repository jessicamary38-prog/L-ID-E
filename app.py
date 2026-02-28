import streamlit as st

# Configuração visual do Clube
st.set_page_config(page_title="Clube Maison L'Idée", page_icon="⚜️")
st.title("⚜️ Clube Maison L'Idée")

st.markdown("""
### Bem-vinda ao nosso Clube!
Este é o seu primeiro passo para uma imagem estratégica. 
Identifique seu biotipo corporal (Kibbe) abaixo e agende sua consultoria completa.
""")

with st.form("teste_estilo_clube"):
    nome = st.text_input("Qual o seu nome?")
    
    st.subheader("📏 Análise de Estrutura Corporal")
    altura = st.selectbox("Sua altura:", ["Até 1.60m", "1.61m a 1.69m", "Acima de 1.70m"])
    ombros = st.selectbox("Seus ombros são:", ["Quadrados/Angulares", "Largos", "Equilibrados", "Suaves/Arredondados"])
    silhueta = st.radio("Sua silhueta geral é:", ["Mais reta", "Proporcional", "Curvilínea"])
    
    submeter = st.form_submit_button("REVELAR MEU BIOTIPO")

if submeter:
    # Lógica interna de identificação automática (sem erros de IA)
    resultado = ""
    if altura == "Acima de 1.70m":
        resultado = "Família Dramática ou Natural (Linhas Longas)"
    elif silhueta == "Curvilínea":
        resultado = "Família Romântica (Linhas Suaves)"
    else:
        resultado = "Família Clássica ou Gamine (Equilíbrio e Mistura)"

    st.success(f"⚜️ {nome}, sua estrutura base identificada é: {resultado}")
    
    st.divider()
    
    st.markdown("""
    ### ✨ Próximos Passos no Clube
    **Para uma análise completa com dossiê, entre em contato conosco pelo WhatsApp.**
    """)
    
    st.info("""
    Como membro do Clube, você terá acesso a:
    * **Identificação de Essências Faciais** (Análise detalhada via fotos)
    * **Diagnóstico de Coloração Pessoal** (Incluindo Pele Oliva)
    * **Montagem de Looks e Visita ao Closet**
    * **Bioestética: Treinos específicos para o seu biotipo Kibbe**
    """)
    
    # Configuração do seu WhatsApp direto
    meu_numero = "5515996398197" 
    msg = f"Olá! Sou {nome}, fiz o teste no Clube Maison L'Idée e quero agendar minha análise completa e saber sobre os treinos!"
    link_wa = f"https://wa.me/{meu_numero}?text={msg}"
    
    st.link_button("💬 FALAR COM A MAISON PELO WHATSAPP", link_wa)
