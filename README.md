# 🤖 Automação de Cadastro de Produtos com Python (RPA)

Projeto de automação (RPA - Robotic Process Automation) desenvolvido em Python, capaz de ler uma base de dados de produtos em `.csv` e realizar o cadastro automático de cada item em um sistema web, simulando ações reais de mouse e teclado.

## 📋 Sobre o projeto

O objetivo do projeto é eliminar o trabalho manual e repetitivo de cadastrar produtos um a um em um sistema web. A automação:

1. Abre o navegador Chrome e acessa o sistema de cadastro automaticamente
2. Realiza o login informando usuário e senha
3. Lê uma planilha CSV com os dados dos produtos a serem cadastrados
4. Para cada produto da lista, preenche automaticamente os campos do formulário (código, marca, tipo, categoria, preço unitário, custo e observações)
5. Confirma o cadastro e repete o processo até percorrer todos os itens da base

No total, o script processa **296 produtos** de forma totalmente automática, sem intervenção manual.

## 🚀 Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — automação de mouse e teclado
- [Pandas](https://pandas.pydata.org/) — leitura e manipulação da base de dados (CSV)
- `subprocess` — abertura automática do navegador
- `time` — controle de tempo de espera entre ações

## 📁 Estrutura do projeto

```
automacao-cadastro-produtos/
├── main.py           # script principal: login + cadastro automático dos produtos
├── auxiliar.py        # script de apoio para identificar coordenadas (x, y) na tela
├── produtos.csv        # base de dados com os produtos a serem cadastrados
└── README.md
```

## ⚙️ Pré-requisitos

- Python 3.9 ou superior instalado
- Google Chrome instalado no caminho padrão (`C:\Program Files\Google\Chrome\Application\chrome.exe`)
- Acesso e credenciais válidas no sistema de cadastro utilizado

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/brenotrombini/automacao-cadastro-produtos.git
cd automacao-cadastro-produtos
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
```

No Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

3. Instale as dependências:
```bash
pip install pyautogui pandas
```

## ▶️ Como executar

1. Garanta que o arquivo `produtos.csv` esteja na mesma pasta do `main.py`, com as colunas: `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`
2. Ajuste as coordenadas de clique (`pyautogui.click(x=..., y=...)`) caso a resolução de tela ou o layout do sistema sejam diferentes — use o `auxiliar.py` para descobrir as posições corretas na sua tela
3. Execute o script principal:
```bash
python main.py
```
4. **Não mexa no mouse ou teclado enquanto o script estiver rodando**, já que a automação depende das coordenadas fixas da tela

## 🛠️ Como usar o `auxiliar.py`

Esse script serve para descobrir as coordenadas (x, y) de qualquer ponto da tela, facilitando o ajuste dos cliques do script principal:

```bash
python auxiliar.py
```

Ele dá 5 segundos para você posicionar o mouse sobre o ponto desejado (ex: um campo do formulário) e depois imprime a posição no terminal.

## ⚠️ Observações importantes

- Essa automação funciona por **coordenadas fixas de tela**, então é sensível a mudanças de resolução, zoom do navegador ou alterações no layout do site
- Recomenda-se rodar em uma máquina com resolução de tela fixa e o navegador sempre maximizado
- Os `time.sleep()` distribuídos pelo código servem para dar tempo da página carregar e evitar erros de digitação em campos ainda não carregados

## 🗺️ Possíveis melhorias futuras

- [ ] Migrar de automação por coordenadas fixas (PyAutoGUI) para automação via Selenium, mais robusta e independente de resolução de tela
- [ ] Adicionar tratamento de erros e logs de produtos que falharem no cadastro
- [ ] Adicionar barra de progresso no terminal
- [ ] Validar os dados do CSV antes de iniciar o cadastro (preços, campos obrigatórios, etc.)

## 👤 Breno Trombini

**Breno Trombini Tertuliano**
- GitHub: [@brenotrombini](https://github.com/brenotrombini)
- LinkedIn: [breno-trombini-tertuliano](https://www.linkedin.com/in/breno-trombini-tertuliano-b2ab50342)

## 📄 Licença

Este projeto está disponível para fins de estudo e portfólio.
