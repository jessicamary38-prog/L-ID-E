import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(
    page_title="Maison L'Idée - Jéssica Maria", 
    page_icon="⚜️", 
    layout="centered"
)

# Estilização CSS Maison
st.markdown("""
    <style>
    .main { background-color: #fcfaf7; }
    .stButton>button {
        background-color: #D4AF37; color: white; border-radius: 10px;
        font-weight: bold; width: 100%; height: 3em; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #B8860B; transform: translateY(2px); }
    h1, h2, h3 { color: #4a3728; font-family: 'serif'; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; line-height: 1.6; color: #5D4037; }
    .quote { border-left: 5px solid #D4AF37; padding-left: 20px; font-style: italic; color: #4a3728; margin: 20px 0; }
    .highlight-name { font-size: 1.5rem; font-weight: bold; color: #4a3728; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DEFINIÇÃO DAS PÁGINAS ---

def pagina_inicio():
    st.title("🏛️ Maison L’Idée")
    st.subheader("Onde a Alma Encontra sua Imagem")
    if os.path.exists("banner.png"): st.image("banner.png")
    st.markdown("""
    A Maison L’Idée (A Casa da Ideia) não é apenas um espaço de consultoria de imagem; é um refúgio dedicado à revelação da identidade. Acreditamos que a beleza não é algo que se cria do zero, mas algo que se descobre e se organiza.
    
    Nascemos da convicção de que cada ser humano é um projeto único, desenhado com uma geometria específica e uma essência inconfundível. Nosso papel é ser a ponte entre quem você é por dentro e o que o mundo vê por fora.
    
    ### 🌿 Nossa Filosofia: A Beleza em Ordem
    Para nós, a imagem é um testemunho silencioso. Quando há um abismo entre a sua alma e a sua aparência, o resultado é o cansaço emocional. Na Maison, trabalhamos para que haja paz no espelho. Unimos três pilares fundamentais para criar uma harmonia que gera repetição e conforto:
    
    * **O Temperamento:** A força da sua alma e o seu ritmo interno.
    * **A Geometria (Kibbe):** O respeito às linhas e formas do seu projeto original.
    * **A Essência (Kitchener):** O perfume e a mensagem que o seu rosto emana.
    
    ### 🕊️ Um Ecossistema de Cuidado
    A Maison L’Idée cresceu e hoje é um lar que abriga todas as fases da vida. Entendemos que cuidar da imagem é apenas o começo de uma jornada de autogoverno e amor ao próximo. Por isso, nossa casa se expandiu em novas frentes:
    
    * **Consultoria & Estilo:** Estratégias visuais que honram a sua história e o seu guarda-roupa.
    * **Biblioteca Digital:** Ebooks que alimentam a mente e o espírito.
    * **Maternar Leve (@maepedagoga):** Um espaço sagrado de educação e afeto para mães que desejam uma jornada com propósito.
    * **Alguém se Importa?:** O nosso braço de acolhimento e valorização da vida, lembrando a cada instante que você é um tesouro precioso do Criador.
    
    ### ⚜️ Nossa Missão
    Ajudar você a se vestir de si mesma. Sem fantasias, sem mudanças radicais que anulem sua essência, e com o respeito profundo à sua individualidade.
    
    Seja bem-vinda à Maison L’Idée. Aqui, sua vida tem um valor inestimável e sua beleza tem um lugar para florescer.
    """)

def pagina_jessica():
    st.title("⚜️ Jéssica Maria")
    st.subheader("A Curadora por trás da Maison")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        if os.path.exists("perfil.png"): st.image("perfil.png")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
        st.link_button("📌 PINTEREST", "https://www.pinterest.com/jessicamary38")
    with col2:
        st.markdown("""
        Integro corpo, face e essência através da neurociência e do comportamento humano. 
        Dessa investigação nasceu o meu método exclusivo: a **humanidade sistêmica**.
        
        Acredito que vestir-se de si mesma é um ato de autogoverno e honra ao seu projeto original. Meu papel é ser a ponte que traduz a sua essência em uma imagem coerente e cheia de paz.
        """)
        st.markdown('<p class="highlight-name">Prazer, Jéssica Maria.</p>', unsafe_allow_html=True)

def pagina_maternar():
    st.title("🕊️ Maternar Leve")
    st.markdown("""
    A maternidade é a nossa missão mais profunda. Na Maison L'Idée, acreditamos que o lar é o nosso primeiro santuário, e a forma como educamos nossos filhos é a nossa maior obra de arte. Por isso, convidamos a Raiane Camargo para trazer luz a este caminho através do @amae.pedagoga_.
    
    ### A Pedagogia do Afeto
    
    "Quando o Francisco chegou, minha casa se transformou na minha primeira sala de aula. 🏠✨
    
    Eu sou a Raiane, tenho 24 anos e, ao ver o mundo pelos olhos do meu filho, entendi que a pedagogia não está apenas nos livros, mas no dia a dia, nas brincadeiras e no afeto. Minha faculdade se tornou a ferramenta para criar momentos lúdicos, amorosos e cheios de propósito para ele.
    
    O Maternar Leve nasce desse desejo de viver a Maternidade Sagrada: entendendo que cada descoberta é um milagre e cada ensinamento é uma semente de eternidade. Decidi tirar esse conhecimento do papel para criar o @amae.pedagoga_ — um espaço onde vou te mostrar que é possível se conectar com seu filho através do ensinar, de forma simples e cheia de significado.
    
    A infância passa rápido demais para não aproveitarmos cada revelação."
    """)
    st.link_button("✨ SIGA @AMAE.PEDAGOGA_", "https://www.instagram.com/amae.pedagoga_")

def pagina_importa():
    st.title("❤️ Alguém se Importa")
    st.markdown("""
    Muitas vezes, a desistência não acontece de uma hora para outra. Ela é um caminho silencioso: começamos deixando de fazer algo por nós, paramos de cultivar nossos sonhos e projetos. Depois, o cansaço aumenta e desistimos de nos cuidar, de olhar no espelho e reconhecer a beleza que nos foi dada. Por último, quando a dor parece não ter fim, o inimigo da alma tenta nos convencer a desistir da própria vida.
    
    **Mas eu quero te dizer hoje: Deus não nos chamou para isso.**
    
    Ele não nos criou para o vazio ou para a derrota. O seu valor não está no que você faz, mas em quem você é para Ele. O próprio Criador deu a vida de Seu Filho por você, pagando o preço mais alto que já existiu para que você pudesse ter vida.
    """)
    
    st.markdown('<div class="quote">"Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna." (João 3:16)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Os planos de Deus para você não são de destruição. Mesmo que hoje você só veja nuvens escuras, a Palavra de Deus garante que o olhar d'Ele sobre você é de esperança:
    """)
    
    st.markdown('<div class="quote">"Porque sou eu que conheço os planos que tenho para vocês\', diz o Senhor, \'planos de fazê-los prosperar e não de causar dano, planos de dar a vocês esperança e um futuro.\'" (Jeremias 29:11)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Ele tem pensamentos de paz e não de mal a seu respeito. Sua vida é um tesouro precioso, e cada amanhecer é uma nova oportunidade de recomeçar sob o cuidado de Quem te ama sem medidas.
    
    ### ✨ Um convite para hoje:
    Não permita que o dia termine sem fazer algo por você. Comece pequeno, mas comece:
    * **Leia um livro:** Visite nossa biblioteca na aba Maison e escolha uma leitura que alimente sua mente.
    * **Leia a Bíblia:** Busque a voz do Pai nas Escrituras.
    * **Ouça uma música:** Coloque aquela canção que você gosta e que traz paz ao seu coração.
    * **Saia para passear:** Sinta o ar, veja o céu, mude o horizonte.
    * **Apenas reflita:** Tire um momento de silêncio para entender que você não é o que sente, mas o que Deus diz que você é.
    
    Nunca se esqueça: você tem um valor muito grande. O Autor da Vida ainda está escrevendo a sua história e Ele não terminou.
    
    **Você é importante.**
    
    Se a dor estiver difícil de carregar, não sofra em silêncio. O CVV oferece apoio gratuito e sigiloso 24 horas. Ligue 188.
    """)
    st.link_button("📩 CONVERSAR COM JÉSSICA", "https://wa.me/5515996398197?text=Olá Jéssica, li a aba Alguém se Importa.")
    st.link_button("📞 LIGAR PARA O CVV (188)", "tel:188")

def pagina_biblioteca():
    st.title("📚 Bem-vinda à Biblioteca Maison L’Idée")
    st.markdown("""
    Entre e sinta-se em casa. Este é o nosso canto de quietude e inspiração.
    
    Acreditamos que o conhecimento é uma das formas mais bonitas de cuidado. Por isso, preparamos a nossa Biblioteca Digital como um verdadeiro presente para você. Cada obra disponível aqui foi escrita e curada para ser mais do que uma simples leitura; são convites para a pausa e instrumentos para a reflexão.
    
    Nesta prateleira digital, você encontrará o fruto das nossas vivências e estudos, organizados para fortalecer a sua identidade e o seu caminhar. Cada página é um pedaço da nossa essência entregue a você. Que estas palavras sejam companheiras de jornada, trazendo clareza para os seus dias e beleza para a sua história.
    
    **Prepare uma xícara de café, escolha o seu título abaixo e desfrute deste momento de descoberta.** Nossa biblioteca está apenas começando, e é uma honra ter você aqui desde o primeiro capítulo.
    """)
    st.link_button("☕ ACESSAR BIBLIOTECA DIGITAL", "https://drive.google.com/drive/folders/1i9UQn39hkamqAefA3-bsErfadjObVhSF")

def pagina_analise_360():
    st.title("📏 Triagem Sistêmica 360º")
    st.info("A Etapa 1 é um presente da Maison. As demais compõem seu Dossiê Premium.")

    nome = st.text_input("Nome da Cliente:").strip()
    email = st.text_input("E-mail:")
    altura = st.number_input("Altura (ex: 1.60):", min_value=1.0, value=1.60, step=0.01)

    st.divider()

    st.markdown("### 🧠 ETAPA 1: TEMPERAMENTO (CORTESIA)")
    t1 = st.radio("1. Em lugares novos:", ["A) Sinto-me à vontade/Interajo", "B) Sou observadora/Analiso"])
    t2 = st.radio("2. Suas decisões são mais:", ["A) Racionais/Lógicas", "B) Emocionais/Sentimentais"])
    t3 = st.radio("3. Reação a imprevistos:", ["A) Rápida e Imediata", "B) Lenta e Criteriosa"])
    t4 = st.radio("4. Duração dos sentimentos:", ["A) Curta (esqueço rápido)", "B) Longa (guardo/intensifico)"])

    temp_veredito = ""
    if "A)" in t1 and "A)" in t2: temp_veredito = "COLÉRICO"
    elif "A)" in t1 and "B)" in t2: temp_veredito = "SANGUÍNEO"
    elif "B)" in t1 and "A)" in t2: temp_veredito = "MELANCÓLICO"
    elif "B)" in t1 and "B)" in t2: temp_veredito = "FLEUMÁTICO"

    if st.button("REVELAR MEU TEMPERAMENTO (CORTESIA)"):
        st.success(f"Seu temperamento predominante é: **{temp_veredito}**")

    st.divider()

    st.markdown("### 👗 ETAPA 2: GEOMETRIA CORPORAL (KIBBE)")
    k_osseo = st.radio("Estrutura Óssea:", ["A) Estreita/Pequena", "B) Larga/Estruturada", "C) Simétrica/Equilibrada"])
    k_curva = st.radio("Suas linhas naturais possuem curvas nítidas?", ["Sim", "Não"])
    k_carne = st.radio("Textura da Carne:", ["A) Densa/Firme", "B) Macia/Suave"])

    st.divider()

    st.markdown("### 🎨 ETAPA 3: ANÁLISE FACIAL (ESSÊNCIAS)")
    f1 = st.selectbox("Formato do Rosto:", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
    f2 = st.selectbox("Formato dos Olhos:", ["Grandes/Redondos", "Rasgados/Feline", "Amendoados", "Simétricos"])
    f3 = st.selectbox("Formato da Boca:", ["Carnuda", "Larga", "Pequena/Fina"])

    if st.button("SOLICITAR DOSSIÊ COMPLETO"):
        if not nome or not email:
            st.error("Por favor, preencha nome e e-mail.")
        else:
            relatorio = (
                f"*SOLICITAÇÃO DE DOSSIÊ COMPLETO*%0A"
                f"*CLIENTE:* {nome}%0A"
                f"*TEMPERAMENTO:* {temp_veredito}%0A"
                f"*KIBBE:* {k_osseo}, Curvas: {k_curva}, Carne: {k_carne}%0A"
                f"*ROSTO:* {f1}, {f2}, {f3}"
            )
            st.success("Tudo pronto! Clique no botão abaixo para enviar os dados.")
            st.link_button("👑 ENVIAR PARA JÉSSICA MARIA", f"https://wa.me/5515996398197?text={relatorio}")

def pagina_modelo():
    st.title("📔 Modelo de Consultoria")
    st.write("Conheça a estrutura do Dossiê que entregamos em nossa consultoria premium.")
    st.link_button("🔗 VER MODELO NO NOTION", "https://www.notion.so/Dossi-J-ssica-Maria-317f44f5bd8680c3b6a9e0ea0243822d")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "Maison": [
        st.Page(pagina_inicio, title="A Maison L'Idée", icon="🏛️"),
        st.Page(pagina_jessica, title="Quem Sou Eu", icon="⚜️"),
        st.Page(pagina_biblioteca, title="Biblioteca Maison", icon="📚"),
    ],
    "Consultoria": [
        st.Page(pagina_analise_360, title="Triagem 360º", icon="📏"),
        st.Page(pagina_modelo, title="Modelo Dossiê", icon="📔"),
    ],
    "Acolhimento": [
        st.Page(pagina_maternar, title="Maternar Leve", icon="🕊️"),
        st.Page(pagina_importa, title="Alguém se Importa", icon="❤️"),
    ]
})
pg.run()
