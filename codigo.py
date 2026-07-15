# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import subprocess
import pandas as pd
       

pyautogui.PAUSE = 0.3
# abrir o Chrome direto, sem depender do menu de busca do Windows
caminho_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.Popen([caminho_chrome, "--start-maximized",
                   "https://dlp.hashtagtreinamentos.com/python/intensivao/login"])
time.sleep(5)  # espera o Chrome abrir e a página carregar

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=574, y=376)
time.sleep(0.5)
pyautogui.write("brenotrobini22@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(3)


# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=744, y=261)
    time.sleep(0.3)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")  # cadastra o produto
    time.sleep(1)
    pyautogui.scroll(5000)
    time.sleep(1)
