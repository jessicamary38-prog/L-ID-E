        st.divider()
    
    # Frase para conversão de consultoria completa
    st.markdown("""
    ### ✨ Próximos Passos
    **Para uma análise completa com dossiê, entre em contato conosco pelo WhatsApp.**
    """)
    
    st.info("""
    No atendimento privado, realizaremos:
    * **Identificação de Essências Faciais** (Análise de fotos)
    * **Diagnóstico de Coloração Pessoal** (Incluindo Pele Oliva)
    * **Montagem de Looks e Visita ao Guarda-roupa**
    """)
    
    # --- CONFIGURAÇÃO DO SEU WHATSAPP ---
    # Seu número já configurado corretamente abaixo
    meu_numero = "5515996398197" 
    
    msg = "Olá! Fiz o teste no site e gostaria de agendar minha análise completa com dossiê."
    # O link abaixo foi corrigido para o formato padrão do WhatsApp
    link_wa = f"https://wa.me/{meu_numero}?text={msg}"
    
    st.link_button("💬 ENTRAR EM CONTATO PELO WHATSAPP", link_wa)
