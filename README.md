# 🛒 MERCAPO: Comparador de Preços em Tempo Real

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Web%20Scraping-Playwright-green?style=for-the-badge&logo=playwright)](https://playwright.dev/)
[![Rich](https://img.shields.io/badge/CLI%20UI-Rich-yellow?style=for-the-badge&logo=python)](https://github.com/Textualize/rich)

## 🎯 Sobre o Projeto

O **MercaPo** é uma aplicação de linha de comando (CLI) desenvolvida em Python que realiza web scraping em tempo real para comparar os preços de uma lista de produtos entre diferentes supermercados. O objetivo principal é identificar a opção de compra mais econômica para o consumidor.

Este projeto demonstra competências em:
*   **Web Scraping Assíncrono/Síncrono:** Utilização do Playwright para automação de navegador e extração de dados.
*   **Engenharia de Dados:** Limpeza, transformação e estruturação de dados brutos (preços) para análise.
*   **Desenvolvimento CLI:** Criação de uma interface de usuário rica e interativa utilizando a biblioteca Rich.
*   **Modularização:** Organização do código em módulos (`services`, `routers`, `utils`) seguindo o princípio de Separação de Responsabilidades.

## 🚀 Funcionalidades

1.  **Criação de Tabela de Preços:** Coleta os preços dos produtos definidos em tempo real.
2.  **Comparação Econômica:** Apresenta o menor preço por produto e calcula o valor total da cesta de compras mais econômica.
3.  **Listagem Detalhada:** Exibe a lista completa de produtos e preços para cada mercado.

## 💻 Demonstração Visual

### Menu Principal
<img width="1108" height="461" alt="image" src="https://github.com/user-attachments/assets/ac87f56a-7da0-4765-9400-04cbea640d77" />


### Comparação de Preços
<img width="672" height="306" alt="image" src="https://github.com/user-attachments/assets/7e9f6db1-2312-4ceb-ba62-5d968518f1b6" />
<img width="786" height="485" alt="image" src="https://github.com/user-attachments/assets/1e42842e-4615-4189-9796-ca1eea2984a1" />

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.x | Linguagem principal de desenvolvimento. |
| **Web Scraping** | Playwright | Utilizado para simular a navegação do usuário e extrair dados dinâmicos dos sites. |
| **Interface CLI** | Rich | Responsável pela formatação e estilização da saída no terminal (tabelas, cores, painéis). |
| **Estrutura** | Modularização | Código organizado em `app/services` (lógica de negócio), `app/routers` (acesso a dados) e `app/utils` (funções auxiliares). |

## ⚙️ Como Executar o Projeto

Para rodar o MercadoPreço em sua máquina, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado.

### 1. Clonar o Repositório

```bash
git clone https://github.com/leomarqueti/MERCAPO.git
cd mercadopreco
```

### 2. Instalar Dependências


```bash
# Instala as bibliotecas Python
pip install -r requirements.txt

# Instala os drivers de navegador necessários para o Playwright
playwright install
```

### 3. Executar a Aplicação

```bash
python main.py
```

## 💡 Próximos Passos

Para evoluir este projeto para um nível de produção e demonstrar maturidade de engenharia de software, as seguintes melhorias estão planejadas:

*   **Configuração Externa:** Mover a lista de produtos, URLs e seletores CSS para um arquivo de configuração (YAML/JSON) para maior flexibilidade.
*   **Testes Unitários:** Implementar testes com `pytest` para a lógica de negócio em `gerencia_preco.py`.
*   **Type Hinting:** Adicionar anotações de tipo em todo o código para melhorar a manutenibilidade e o suporte a ferramentas de análise estática.
*   **Refatoração de Arquitetura:** Revisar a nomenclatura dos módulos e o gerenciamento de estado (evitando variáveis globais).

---

## 👨‍💻 Autor

**Leonardo Marqueti de Lima Sato**


