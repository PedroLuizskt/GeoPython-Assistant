# 🛰️ GeoPython Assistant: O Mentor de IA para Inteligência Geoespacial

> **Transformando conceitos de programação em soluções de Geoprocessamento e Sensoriamento Remoto.**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Groq API](https://img.shields.io/badge/Groq-AI_Inference-orange?style=for-the-badge)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sobre o Projeto

O **GeoPython Assistant** não é apenas um chatbot; é uma ferramenta de **Engenharia de Prompt** aplicada à educação técnica.

Muitos profissionais de Geociências (Engenheiros Florestais, Agrônomos, Geógrafos) enfrentam uma barreira ao aprender Python: **a desconexão entre os tutoriais genéricos e a realidade dos dados espaciais.** Aprender a manipular listas de compras não ajuda a manipular uma coleção de imagens de satélite.

Este projeto resolve isso criando uma "persona" de Arquiteto de Soluções que traduz qualquer dúvida de programação diretamente para o ecossistema geoespacial (GIS).

### O Diferencial: Contextualização Forçada
Através de um System Prompt rigoroso, o assistente é instruído a:
1.  **Ignorar exemplos genéricos:** Listas viram `FeatureCollections`, Matrizes viram `Rasters`.
2.  **Anti-Alucinação:** Priorizar bibliotecas oficiais e citar documentação.
3.  **Foco em Big Data:** Sugerir otimizações de performance para processamento em escala.

---

## Stack Tecnológica

A arquitetura foi pensada para leveza e velocidade de inferência (Low Latency):

* **Frontend & UI:** [Streamlit](https://streamlit.io/) - Para criação rápida de dashboards de dados.
* **LLM Inference:** [Groq API](https://groq.com/) - Utilizando LPUs (Language Processing Units) para respostas quase instantâneas.
* **Modelo de IA:** **Llama-3-70b-Versatile** - Escolhido pelo equilíbrio entre capacidade de raciocínio lógico e geração de código complexo.
* **Linguagem:** Python 3.10+

---

## Como Utilizar

### Opção 1: Acesso Online (Recomendado)
Acesse a aplicação hospedada na nuvem do Streamlit:
👉 **[Clique aqui para acessar o GeoPython Assistant](https://geopython-assistant-skt.streamlit.app/)**

*Nota: Você precisará de uma API Key gratuita da Groq.*

### Opção 2: Execução Local

Se você deseja rodar o projeto na sua máquina ou contribuir com o código:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/GeoPython-Assistant.git](https://github.com/SEU-USUARIO/GeoPython-Assistant.git)
    cd GeoPython-Assistant
    ```

2.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate   # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

---

## Exemplo de Engenharia de Prompt

O "cérebro" do assistente opera sob regras estritas. Um trecho do *System Prompt* utilizado:

> *"Você é o 'GeoPython Architect'. Sua missão é ensinar Python focado EXCLUSIVAMENTE em aplicações de Geoprocessamento. Se o usuário perguntar sobre 'Dicionários', ensine criando um mapeamento de classificação de uso do solo (ex: {'floresta': 1, 'agua': 2})."*

---

## Autor

Desenvolvido por **Pedro Luiz**.

* **Engenheiro Florestal**
* **Especialista em Ciência de Dados Geoespaciais**

Conecte-se comigo:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedro-luiz-rodrigues-vaz-de-melo)

---
