import streamlit as st

# 1. Configuração visual do Clube Maison L'Idée
st.set_page_config(page_title="Clube Maison L'Idée", page_icon="⚜️")
st.title("⚜️ Clube Maison L'Idée")

# 2. Navegação por Abas
aba1, aba2 = st.tabs(["Análise de Biotipo", "Área da Cliente (Notion)"])

with aba1:
    st.markdown("### Descubra sua Estrutura Base")
    st.write("Identifique seu biotipo corporal e traços de temperamento abaixo.")
    
    with st.form("teste_estilo_clube"):
        nome = st.text_input("Qual o seu nome?")
        
        st.subheader("📏 Estrutura Corporal")
        altura = st.selectbox("Sua altura:", ["Até 1.60m", "1.61m a 1.69m", "Acima de 1.70m"])
        # Mantendo a pergunta técnica de ombros que você já tinha
        ombros = st.selectbox("Seus ombros são:", ["Quadrados/Angulares", "Largos", "Equilibrados", "Suaves/Arredondados"])
        
        st.subheader("🧠 Temperamento e Presença")
        # Refinamento da extroversão em ambientes novos
        extroversao = st.radio(
            "Como você se comporta em lugares totalmente desconhecidos?",
            [
                "Sou observadora, prefiro ver o ambiente antes de interagir (Introvertida)", 
                "Sinto-me à vontade e interajo com facilidade desde o início (Extrovertida)"
            ]
        )
        
        submeter = st.form_submit_button("REVELAR MEU BIOTIPO")

    if submeter:
        # Lógica interna baseada no seu conhecimento (Sem IA para evitar erros 404/v1beta)
        resultado = ""
        if altura == "Acima de 1.70m":
            resultado = "Família Dramática ou Natural (Linhas Yang)"
        elif "interajo com facilidade" in extroversao:
            resultado = "Família Gamine ou Natural (Energia Ativa)"
        else:
            resultado = "Família Clássica ou Romântica (Energia Suave/Yin)"

        st.success(f"⚜️ {nome}, sua estrutura base identificada é: {resultado}")
        
        st.divider()
        st.markdown("**Para uma análise completa de Temperamento, Dossiê 360º e Treinos, entre em contato!**")
        
        # 3. Configuração do WhatsApp (Seu número configurado)
        meu_numero = "5515996398197" 
        msg = f"Olá! Sou {nome}, fiz o teste no Clube e quero minha análise completa de biotipo e treinos!"
        link_wa = f"https://wa.me/{meu_numero}?text={msg}"
        st.link_button("💬 FALAR COM A MAISON NO WHATSAPP", link_wa)

with aba2:
    st.markdown("### 📔 Sua Área Exclusiva")
    st.write("Acesse seu Dossiê Personalizado, orientações de estilo e seu plano de Bioestética.")
    
    # Integração com seu link real do Notion
    st.link_button("🔗 ACESSAR MEU DOSSIÊ NO NOTION", "https://nine-broccoli-4e7.notion.site/Boas-Vindas-317f44f5bd8681898138f6bb2118c02f")
    
    st.info("""
    **O que você encontra no seu Dossiê:**
    * 🎨 Diagnóstico de Temperamento e Coloração (Pele Oliva).
    * ✨ Análise detalhada de Essências Faciais.
    * 👗 Curadoria de Looks para seu ID Kibbe.
    * 🏋️‍♂️ Protocolo de Treino para seu biotipo (Bioestética).
    """)
