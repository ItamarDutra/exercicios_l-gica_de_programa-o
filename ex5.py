#def vencedor():
    # matriz_vencedora = random.choice(cartelas)
    # for col in range(5):
    #     for lin in range(5):
    #         print(f'[{matriz_vencedora[lin][col]:>2}]', end = " ")
    # print()

    #  def mostrar_cartela():
    ##print([lin and print() for lin in matriz])

    # # aleat = random.randint(1,75)
        # if aleat not in nums_sort:
        #     nums_sort.append(aleat)
        #     for m in cartelas:
        #         for lin in range(5):
        #             if m[lin] in nums_sort:
 
import random

cartelas = []


def gerar_cartela(sigla):
    global cartelas
    cartelas.clear()
    qtd_cartelas = int(input("Qual a quantidade de cartelas a serem geradas? "))
    for i in range(qtd_cartelas):
        matriz = [[0,0,0,0,0] for i in range(5)]
        x= 1
        y= 15
        sorteados = []
        for col in range(5):
            for lin in range(5):
                while True:
                    aleat = random.randint(x,y)
                    if aleat not in sorteados:
                            sorteados.append(aleat)
                            matriz[lin][col] = aleat
                            break
            x +=15
            y +=15

        matriz[2][2] = sigla
        cartelas.append(matriz.copy())





def bingo_todo():
    cabou = False
    nums_sort = []
    while cabou == False:
        
        aleat = random.randint(1,75) 
        if aleat not in nums_sort:
            nums_sort.append(aleat)
            for matriz in cartelas:
                campeao = True
                for linha in matriz:
                    for num in linha:
                        if type(num)==int and num not in nums_sort:
                            campeao = False
                            break
                
                if campeao == True:
                    print("Vencedor encontrado!")
                    print(f"quantidade de números sorteados: {len(nums_sort)}")
                    print("Cartela Vencedora")
                    for lin in matriz:
                        for num in lin:
                            print(f'[{num:>02}]', end= " ")
                        print()
                    cabou = True
                    break
        
        
       
                        
               
            
def bingo_lcd():    
    cabou = False
    nums_sort = []
    while cabou == False:


        aleat = random.randint(1,75) 
        if aleat not in nums_sort:
            nums_sort.append(aleat)
            for matriz in cartelas:
                for lin in range(5):
                    for col in range(5):
                        campeao = True
                        if type(matriz[lin][col])==int and matriz[lin][col] not in nums_sort:
                            campeao = False
                            break
            

                    if campeao == True:
                        print("Vencedor encontrado!")
                        print(f"quantidade de números sorteados: {len(nums_sort)}")
                        print("Cartela Vencedora")
                        for lin in matriz:
                            for num in lin:
                                print(f'[{num:>02}]', end= " ")
                            print()
                        cabou = True
                        break



regras_resp = "1"
resp = True
while resp != "4":
    resp = input('''
1) Gerar Cartelas 
2) Definir Regras 
3) Começar Bingo! 
4) Encerrar Programa
>>> ''')
    if resp == "1":
        gerar_cartela("NT")
        print(" Cartelas Gerada! ")
    elif resp == "2":
        regras_resp = input('''
1 - Linha, Coluna, Diagonal (padrão)
2 - Cartela Cheia
''')
        print("Regras definidas!")
    elif resp == "3":
        if regras_resp == "2":
            bingo_todo()
        else:
            bingo_lcd()

    elif resp == "4":
        print(" Ok, encerrando... ") 
    else:
        print(" Opção errada. Tente novamente. ")
        continue