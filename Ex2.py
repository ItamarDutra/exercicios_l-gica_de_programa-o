print("=======Olá! Seja bem vindo a nossa loja=======")
print("Eu me chamo Itamar e irei anotar o seu pedido")
pedido = False
tam_correto = False
sabor1 = "AC"
sabor2 = "CP"

while pedido == False:
    sabor_resp = input("por gentileza, escolha entre AC(Açai) ou CP(Cupuaçu). [AC/CP]: ").upper() 
    if sabor_resp in [sabor1, sabor2]:
        
        while tam_correto == False:
            if sabor_resp == sabor1:
             print("tamanhos disponiveis: [P/M/G] \n P : R$ 11,00 \n M : R$ 16,00 \n G : R$ 20,00")
            else: 
                print("tamanhos disponiveis: [P/M/G] \n P : R$ 9,00 \n M : R$ 14,00 \n G : R$ 18,00")

            print("*se quiser voltar digite 1* ")
            t_resp = input("escolha: ").upper()
            if t_resp in ["P","M","G"]:
                pedido = True
                tam_correto = True
            elif t_resp == "1":
                break
            else: 
                print("Tamanho invalido, sua MULA! Tente novamente.")            
    else:
        print("Sabor invalido ANIMAL! Tente novamente.")

print(f"pedido em preparo : {sabor_resp} tamanho {t_resp}")