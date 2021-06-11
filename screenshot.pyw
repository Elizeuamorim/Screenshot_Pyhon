import pyautogui
import os
import string
import random
#geração de um nome aleatório com 6 caracter.
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))
#Condição que fica rodando sempre
while True:
    capturar = pyautogui.screenshot
    #tirando um print da tela
    capturar.save('print.png')
    #salvando o print com o nome print.png na mesma pasta que o sistema está rodando
    os.rename('print.png', random_generator())
    #alterando o nome do arquivo para o nome gerado automaticamente
    time.sleep(10)
    #esperar 10 segundos para tirar o print novamente