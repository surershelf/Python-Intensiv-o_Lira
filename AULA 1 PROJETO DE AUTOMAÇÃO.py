import pyautogui
import pyperclip
import time
import pandas
time.sleep(5)
pyautogui.FAILSAFE=True
pyautogui.PAUSE=1

pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=396, y=296, clicks=2)
pyautogui.click(x=425, y=379)
pyautogui.click(x=1476, y=187)
pyautogui.click(x=1256, y=591)

tabela= pandas.read_excel(r'C:\Users\Usuário\Downloads\Vendas - Dez.xlsx')
print(tabela)
faturamento= tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

pyautogui.hotkey('ctrl','t')
pyautogui.click(x=535, y=48)
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=126, y=197)
pyautogui.write('mazzolucas0@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Faturamento do mês')
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
pyperclip.copy(f'''
Prezados, bom dia 

O valor de faturamento foi de R${faturamento:,.2f}
O valor da quantidade foi de R${quantidade:,.2f}

Att. Surershelf
''')
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
pyautogui.hotkey('ctrl','enter',cliks=2)




