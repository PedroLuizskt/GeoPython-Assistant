# GeoPython Assistant  Adaptado por Pedro Luiz para Geoprocessamento e IA

import os
import streamlit as st
from groq import Groq


# 1. Configuração da Página (Identidade Visual Geoespacial)

st.set_page_config(
    page_title="GeoPython - Assistente",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Engenharia de Prompt
CUSTOM_PROMPT = """
Você é o "GeoPython Architect", um mentor de elite especializado em Engenharia de Dados Geoespaciais, Sensoriamento Remoto e Inteligência Artificial.
Sua missão é ensinar Python focado EXCLUSIVAMENTE em aplicações de Geoprocessamento, GIS e Agricultura de Precisão.

DIRETRIZES CRÍTICAS DE COMPORTAMENTO:
1.  **Contexto Geoespacial Obrigatório**: NUNCA dê exemplos genéricos.
    * Se o usuário perguntar sobre 'listas', ensine iterando sobre uma 'ImageCollection' do Sentinel-2 ou features de um GeoJSON.
    * Se perguntar sobre 'Pandas', ensine manipulando tabelas de atributos de Shapefiles ou CSVs de estações meteorológicas.
    * Se perguntar sobre 'Matrizes/NumPy', trate como Bandas Espectrais ou Modelos Digitais de Elevação (MDE).

2.  **Stack Tecnológica Preferencial (Estado da Arte)**:
    * Vetor: Geopandas, Shapely, Fiona, PyGEOS.
    * Raster: Rasterio, Xarray, Rioxarray.
    * Nuvem: Google Earth Engine (API Python), Microsoft Planetary Computer.
    * Visualização: Leaflet (Folium), Streamlit, Datashader.
    * Banco de Dados: PostGIS, DuckDB Spatial.

3.  **Rigor Científico e Citação de Fontes (ANTI-ALUCINAÇÃO)**:
    * Toda resposta deve ser verificável.
    * Você deve citar explicitamente de onde vem a lógica, a fórmula ou a biblioteca.
    * Se usar uma fórmula de índice (ex: NDVI, EVI), cite a fonte teórica básica (ex: USGS, NASA).

4.  **Estrutura da Resposta**:
    * **Conceito Teórico**: Explicação breve do tópico Python.
    * **Aplicação Geoespacial**: Exemplo de código PRÁTICO e RELEVANTE.
    * **Explicação Técnica**: Detalhe o que o código faz.
    * **Dica de Performance**: Como escalar isso para Big Data.
    * **📚 Fontes e Referências**: SEÇÃO OBRIGATÓRIA ao final. Liste links para a documentação oficial das bibliotecas usadas (ex: geopandas.org, rasterio.readthedocs.io) ou papers/manuais técnicos relevantes.

5.  **Tom de Voz**: Profissional, Sênior, Focado em Engenharia e Escalabilidade.

Responda sempre em Português do Brasil.
"""
# 3. Interface da Barra Lateral

with st.sidebar:
    st.title("🛰️ GeoPython Assistente")
    st.caption("Mentor de Inteligência Geoespacial")
    
    st.markdown("""
    Este assistente converte conceitos de programação diretamente para a realidade do **GIS, Sensoriamento Remoto e Big Data Ambiental**.
    """)
    
    # Campo de API Key
    groq_api_key = st.text_input(
        "Insira sua API Key Groq", 
        type="password",
        help="Obtenha sua chave gratuita em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("###  Especialidades")
    st.markdown("""
    -  **Florestal**: Inventário, Carbono
    -  **Agro**: NDVI, Produtividade
    -  **GIS**: ETL, PostGIS, Geopandas
    -  **Remote Sensing**: Landsat, Sentinel
    """)
    
    st.markdown("---")
    st.info("ℹ️ **Verificabilidade:** Todas as respostas incluem links para a documentação oficial das bibliotecas utilizadas.")
    st.caption("Desenvolvido por Pedro Luiz | Baseado no DSA AI Coder")

# 4. Interface Principal

st.title("GeoPython Assistant 🌍🐍")
st.subheader("Sua Ponte entre Python e a Inteligência Geográfica")

# Texto introdutório condicional
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.info("👋 Olá! Sou seu assistente de soluções. Pergunte-me sobre Python e eu te mostrarei como aplicar em **Imagens de Satélite** e **Dados Vetoriais**, com referências técnicas oficiais.")

# Exibe histórico
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🛰️"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 5. Lógica de Processamento (Groq API)
client = None

if groq_api_key:
    try:
        client = Groq(api_key=groq_api_key)
    except Exception as e:
        st.sidebar.error(f"Erro na API Key: {e}")

# Captura input
if prompt := st.chat_input("Ex: Como uso Dicionários para classificar Uso do Solo?"):
    
    if not client:
        st.warning("⚠️ Por favor, insira sua API Key da Groq na barra lateral para iniciar o geoprocessamento.")
        st.stop()

    # Adiciona mensagem do usuário ao estado
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    # Prepara contexto para o LLM
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    messages_for_api.extend(st.session_state.messages)

    with st.chat_message("assistant", avatar="🛰️"):
        with st.spinner("Consultando bases de dados e documentação oficial..."):
            try:
                # Llama 3 70B 
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="llama-3.3-70b-versatile", 
                    temperature=0.2, # (Baixa temperatura reduz alucinação de links)
                    max_tokens=2048,
                )
                
                response_content = chat_completion.choices[0].message.content
                st.markdown(response_content)
                
                # Salva resposta no histórico
                st.session_state.messages.append({"role": "assistant", "content": response_content})

            except Exception as e:
                st.error(f"Erro de conexão com o satélite (API): {e}")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
    "GeoPython Architect © 2024 - Pedro Luiz | Engenharia de Dados Geoespaciais"
    "</div>", 
    unsafe_allow_html=True

)

