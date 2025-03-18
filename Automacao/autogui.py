import pyautogui

def msg():
    print('1 - Bom dia!')
    print('2 - Boa tarde!')
    print('3 - Boa noite!')
    op = 0
    op = int(input('Digite a opção de Mensagem!'))
    match op:
        case 1:
            return "Bom Dia!"
        case 2:
            return "Boa Tarde"
        case 3:
            return "Boa Noite"

def menu():
    print('Mensagens WhatsApp')
    print('1 - Mensagem Prontas')
    print('2 - Digitar sua mensagem')
    op = int(input('Escolha sua opção:'))
    return op

op = menu()

if op == 1:
    print('Escolheu mensagem Prontas!')
    mensagem = msg()
elif op ==2:
    print('Escolheu digitar sua mensagem!')
    mensagem = str(input('Digite sua mensagem:'))

pyautogui.press('winleft')

pyautogui.sleep(2)

pyautogui.write('chromer')

pyautogui.sleep(2)

pyautogui.press('enter')

pyautogui.sleep(2)

pyautogui.moveTo(x=1254, y=50)

pyautogui.sleep(2)

pyautogui.click()

pyautogui.sleep(2)

pyautogui.write('whatsapp web')

pyautogui.sleep(2)

pyautogui.press('enter')

pyautogui.sleep(2)

pyautogui.moveTo(x=330, y=389)

pyautogui.sleep(2)

pyautogui.click()

pyautogui.sleep(10)

pyautogui.moveTo(x=205, y=243)

pyautogui.sleep(2)

pyautogui.click()

pyautogui.sleep(5)

pyautogui.write('chotta')

pyautogui.sleep(2)

pyautogui.press('enter')

pyautogui.sleep(2)

pyautogui.write(mensagem)

pyautogui.sleep(2)

pyautogui.press('enter')