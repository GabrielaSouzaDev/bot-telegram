# 🤖 Bot de Monitoramento de Preços - Telegram

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Selenium-4.x-green?style=for-the-badge&logo=selenium&logoColor=white"/>
  <img src="https://img.shields.io/badge/Telegram-Bot%20API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/Amazon-Scraper-FF9900?style=for-the-badge&logo=amazon&logoColor=white"/>
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge"/>
</p>

> Bot Python que monitora preços de produtos em e-commerces (Amazon Brasil) via Selenium e envia uma notificação automática pelo Telegram quando o preço desejado é atingido.

---

## Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Demonstração](#-demonstração)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
  - [1. Obtendo o Token do Bot Telegram](#1-obtendo-o-token-do-bot-telegram)
  - [2. Obtendo o Chat ID](#2-obtendo-o-chat-id)
  - [3. Configurando os Produtos](#3-configurando-os-produtos)
- [Como Usar](#-como-usar)
- [Como Funciona](#-como-funciona)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Boas Práticas e Segurança](#-boas-práticas-e-segurança)
- [Possíveis Erros e Soluções](#-possíveis-erros-e-soluções)
- [Melhorias Futuras](#-melhorias-futuras)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## Sobre o Projeto

Este projeto automatiza o monitoramento de preços em sites de e-commerce, eliminando a necessidade de verificar manualmente se um produto atingiu o preço desejado. Utilizando **Selenium** para navegar e extrair dados das páginas e a **API do Telegram** para envio de notificações em tempo real, o bot percorre uma lista de produtos configurada pelo usuário e dispara um alerta assim que o preço estiver igual ou abaixo do valor-alvo definido.

Ideal para quem quer aproveitar promoções sem ficar verificando manualmente os sites.

---

## Funcionalidades

- ✅ Monitoramento de **múltiplos produtos** simultaneamente
- ✅ Extração de preço (inteiro + decimal) via **classes HTML** da Amazon
- ✅ Envio de **notificação pelo Telegram** com preço atual e link do produto
- ✅ Instalação automática do **ChromeDriver** via `webdriver-manager`
- ✅ Configuração simples por lista de dicionários Python
- ✅ Mensagem de status no console após cada verificação

---

## Demonstração

Quando o preço de um produto atinge o valor desejado, você recebe uma mensagem como esta no Telegram:

```
📢 O preço desejado foi alcançado!!
💰 O preço do produto é: R$ 449.90
🔗 https://www.amazon.com.br/...
```

---

##  Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| [Python](https://www.python.org/) | Linguagem principal |
| [Selenium](https://selenium-python.readthedocs.io/) | Automação do navegador e web scraping |
| [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) | Gerenciamento automático do ChromeDriver |
| [Requests](https://docs.python-requests.org/) | Integração com a API do Telegram |
| [Google Chrome](https://www.google.com/chrome/) | Navegador utilizado pelo Selenium |
| [Telegram Bot API](https://core.telegram.org/bots/api) | Envio das notificações |

---

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (versão atualizada)
- [pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes do Python)
- Uma conta no [Telegram](https://telegram.org/) e um bot criado via [@BotFather](https://t.me/BotFather)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as dependências

```bash
pip install ['nome da dependencia']
```

```
python3
selenium
webdriver-manager
requests
```

---

## Configuração

### 1. Obtendo o Token do Bot Telegram

1. Abra o Telegram e procure por **[@BotFather](https://t.me/BotFather)**
2. Envie o comando `/newbot`
3. Siga as instruções para nomear seu bot
4. Ao final, o BotFather fornecerá um **TOKEN** no formato:
   ```
   123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
   ```
5. Copie esse token — ele será usado no script

### 2. Obtendo o Chat ID

1. Inicie uma conversa com seu bot no Telegram (clique em `/start`)
2. Acesse a URL abaixo no navegador, substituindo `SEU_TOKEN`:
   ```
   https://api.telegram.org/botSEU_TOKEN/getUpdates
   ```
3. Procure pelo campo `"chat"` > `"id"` no JSON retornado
4. Esse número é o seu **CHAT_ID**

### 3. Configurando os Produtos

No arquivo `main.py`, edite a lista `produtos` com as URLs e valores desejados:

```python
produtos = [
    {
        "url": "https://www.amazon.com.br/seu-produto",
        "valor_desejado": 299.90
    },
    {
        "url": "https://www.amazon.com.br/outro-produto",
        "valor_desejado": 1500.00
    }
]
```

> ⚠️ **Atenção:** Não exponha seu `TOKEN` e `CHAT_ID` diretamente no código. Veja a seção de [Boas Práticas e Segurança](#-boas-práticas-e-segurança).

---

## Como Usar

Com tudo configurado, execute o script:

```bash
python botTelegram.py
```

O bot irá:
1. Abrir o Chrome automaticamente
2. Acessar cada URL da lista de produtos
3. Extrair o preço atual da página
4. Comparar com o `valor_desejado`
5. Enviar uma mensagem no Telegram caso o preço esteja dentro do limite
6. Fechar o navegador ao final

<!-- Para rodar o monitoramento de forma contínua, você pode agendar a execução do script usando:
- **Windows:** Agendador de Tarefas
- **Linux/macOS:** `cron` (ex: a cada hora)

```bash
# Exemplo de cron — executar a cada hora
0 * * * * /usr/bin/python3 /caminho/para/main.py
``` -->

---

## Como Funciona

```
┌──────────────┐     ┌──────────────────────┐     ┌─────────────────┐
│  Lista de    │────▶│  Selenium abre o     │────▶│  Extrai classes │
│  Produtos    │     │  Chrome e acessa URL │     │  HTML do preço  │
└──────────────┘     └──────────────────────┘     └────────┬────────┘
                                                           │
                                              ┌────────────▼────────────┐
                                              │ Converte para float e   │
                                              │ compara com valor-alvo  │
                                              └────────────┬────────────┘
                                                           │
                          ┌────────────────┐              │
                          │  Telegram envia│◀─────────────┘
                          │  notificação   │   (se preço ≤ desejado)
                          └────────────────┘
```

### Extração do preço

O script localiza os elementos HTML da Amazon usando as classes:

| Classe HTML | Conteúdo |
|---|---|
| `a-price-whole` | Parte inteira do preço (ex: `"1.299,"`) |
| `a-price-fraction` | Parte decimal do preço (ex: `"90"`) |

A parte inteira tem pontos e vírgulas removidos, depois é concatenada com a parte decimal para formar o preço final em `float`.

---

## Estrutura do Projeto

```
📦 nome-do-repositorio/
├── 📄 botTelegram.py     # Script principal do bot
├── 📄 .env               # Variáveis de ambiente (TOKEN e CHAT_ID) ⚠️ não versionar
├── 📄 .gitignore         # Arquivos ignorados pelo Git
└── 📄 README.md          # Documentação do projeto
```

---

## Boas Práticas e Segurança

> **Nunca suba seu TOKEN ou CHAT_ID para o GitHub!** Essas credenciais dão acesso total ao seu bot.

<!-- ### Usando variáveis de ambiente com `.env`

1. Instale a biblioteca `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```

2. Crie um arquivo `.env` na raiz do projeto:
   ```env
   TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
   CHAT_ID=987654321
   ```

3. Atualize o `main.py` para ler as variáveis:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()

   TOKEN = os.getenv("TOKEN")
   CHAT_ID = os.getenv("CHAT_ID")
   ```

4. Adicione o `.env` ao `.gitignore`:
   ```gitignore
   .env
   venv/
   __pycache__/
   *.pyc
   ``` -->

---

## Possíveis Erros e Soluções

| Erro | Causa Provável | Solução |
|---|---|---|
| `NoSuchElementException` | Classe HTML não encontrada na página | A Amazon pode ter mudado a estrutura; inspecione o HTML atualizado |
| `WebDriverException` | Chrome não encontrado ou versão incompatível | Atualize o Chrome e reinstale `webdriver-manager` |
| `ConnectionError` | Sem acesso à internet | Verifique sua conexão de rede |
| Preço retornado incorreto | Formatação regional diferente | Ajuste a lógica de remoção de caracteres no preço |
| Notificação não chegou | TOKEN ou CHAT_ID incorretos | Verifique as credenciais e se iniciou conversa com o bot |

> 💡 **Dica:** Se a página demorar a carregar, aumente o tempo do `time.sleep()` ou substitua por uma espera explícita com `WebDriverWait`.

---

## Melhorias Futuras

- [ ] Usar `WebDriverWait` no lugar de `time.sleep()` para esperas mais robustas
- [ ] Suporte a outros e-commerces (Mercado Livre, Magazine Luiza, etc.)
- [ ] Salvar histórico de preços em um arquivo `.csv` ou banco de dados
- [ ] Interface de configuração via linha de comando (CLI)
- [ ] Modo headless (Chrome sem abrir janela visível)
- [ ] Agendamento interno com `schedule` ou `APScheduler`
- [ ] Containerização com Docker

---

## Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um **fork** do repositório
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/minha-melhoria
   ```
3. Faça o commit das suas alterações:
   ```bash
   git commit -m "feat: descrição da melhoria"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/minha-melhoria
   ```
5. Abra um **Pull Request**

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Desenvolvido com 💙 usando Python, Selenium e Telegram Bot API
</p>