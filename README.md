# EngenheiroIA — Assistente Virtual de Engenharia Civil

## Sobre o projeto

O **EngenheiroIA** é um assistente virtual desenvolvido com Inteligência Artificial, com o objetivo de auxiliar estudantes e iniciantes a compreender conceitos fundamentais da Engenharia Civil.

O projeto utiliza a API do Google Gemini para responder perguntas em linguagem natural, consultando uma base de conhecimento própria sobre diferentes áreas da Engenharia Civil.

## Objetivo

Desenvolver um assistente virtual capaz de explicar conceitos técnicos de Engenharia Civil de maneira simples, didática e acessível.

## Tecnologias utilizadas

- Python
- Google Gemini API
- Biblioteca Google GenAI
- Google Colab
- GitHub

## Áreas de conhecimento

A base de conhecimento foi organizada em cinco temas principais:

- **Estruturas:** vigas, pilares, lajes e fundações.
- **Geotecnia:** solos, sondagem, terraplanagem e fundações.
- **Hidráulica:** instalações hidráulicas, esgoto e águas pluviais.
- **Materiais de construção:** cimento, concreto, aço, areia e outros materiais.
- **Construção civil:** planejamento, execução de obras e etapas construtivas.

## Desenvolvimento — 6 etapas

**1. Definição do projeto**

Escolha do tema Engenharia Civil e definição do objetivo do assistente virtual.

**2. Organização da base de conhecimento**

Criação de arquivos com informações sobre diferentes áreas da Engenharia Civil.

**3. Engenharia de prompts**

Desenvolvimento de instruções para orientar o comportamento do EngenheiroIA, definindo linguagem, objetivos e limites das respostas.

**4. Integração com Inteligência Artificial**

Utilização da API do Google Gemini e implementação do código em Python para receber perguntas e gerar respostas.

**5. Testes e validação**

Realização de testes com perguntas sobre vigas, fundações e materiais de construção, verificando a capacidade de resposta e a utilização da base de conhecimento.

**6. Documentação e publicação**

Organização dos arquivos, documentação do projeto e publicação do código no GitHub para apresentação e compartilhamento.

## Como executar

Instale a biblioteca necessária:

```bash
pip install -r requirements.txt
```

Configure sua chave de API do Google Gemini na variável de ambiente:

```text
GEMINI_API_KEY
```

Execute o arquivo principal `assistente.py` utilizando Python.

O assistente iniciará uma conversa no terminal, permitindo digitar perguntas sobre Engenharia Civil. Para encerrar, digite `sair`.

## Exemplo de utilização

**Pergunta:**

O que é uma fundação na Engenharia Civil?

**Resposta esperada:**

O EngenheiroIA explica que a fundação é o elemento responsável por transmitir as cargas da construção para o solo, apresentando exemplos e explicações em linguagem simples.

## Limitações

O EngenheiroIA possui finalidade educativa e foi desenvolvido para apoiar estudantes e iniciantes. Suas respostas não substituem projetos, cálculos, orientações ou avaliações realizados por profissionais habilitados.

## Autor

Desenvolvido por **Guilherme Urban** como projeto prático de aprendizagem da plataforma DIO.

## Repositório

[GitHub — EngenheiroIA](https://github.com/guilhermeUrban74/EngenheiroIA)
