def repetidor(valor_ou_str,msg_de_erro,definicao):
    try:
        #valores a serem adicionados.
        valor = definicao(input(valor_ou_str))
    except:
        t=False
        print(msg_de_erro)
        while t==False:
            #repetição para caso o usuário insira algo além do que foi definido(int,float ou str)
            try:
                valor = definicao(input(valor_ou_str))
                break
            except:
                print(msg_de_erro)
                t=False
    return valor
F=True
while F==True:
	print("_-_"*20)
	opção_de_iniciar = repetidor("O que deseja fazer?\n[1]calcular valor de uma porcetagem.\n[2]calcular a porcetagem de um valor.\n","esta opção não é válida, tente novamente.",float)

	if opção_de_iniciar == 1:
		valor_total = repetidor("insira o valor total:","indisponível ",float)
		valor_da_porcetagem = repetidor("insira a porcentagem a ser calculada","indisponível ",float)
		
		    
		multiplicação = valor_total * valor_da_porcetagem
		
		somar=str(input("""deseja calcular o acrescimo da porcetagem sobe o valor total? \n[s] \n[n]\n"""))
		
		if somar=="s":
		    print(multiplicação/100+valor_total)
		elif somar=="n":
		    print(multiplicação/100)
		while somar!="s" and somar!="n":
		    print("opção inválida, tente novamente ")
		    somar=str(input("""deseja calcular o acrescimo da porcetagem sobe o valor total? \n[s] \n[n]\n"""))
	
	elif opção_de_iniciar == 2:
		try:
			valor_total = repetidor("insira o valor total:","opção inválida, tente novamente. ",float)
			valor_que_deseja_saber_da_porcetagem = repetidor("insira o valor a ser calculado a porcetagem:","opção inválida, tente novamente.", float)
			resultado = (valor_que_deseja_saber_da_porcetagem * 100)/valor_total
			print (f"a porcetagem de  {valor_que_deseja_saber_da_porcetagem} em  {valor_total} é {resultado}%")
		except:
			t=False
			print("opção inválida, tente novamente.")
			while t==False:
					try:
						valor_total = repetidor("insira o valor total:","opção inválida, tente novamente. ",float)
						valor_que_deseja_saber_da_porcetagem = repetidor("insira o valor a ser calculado a porcetagem:","opção inválida, tente novamente.", float)
						resultado = (valor_que_deseja_saber_da_porcetagem * 100)/valor_total
						print (f"a porcetagem de  {valor_que_deseja_saber_da_porcetagem} em  {valor_total} é {resultado}%")
						break
						
					except:
						print("opção inválida, tente novamente. ")
						t=False
						print("teste")				
	continuar_ou_finalizar = repetidor("\nDeseja utilizar o programa novamente?\n[s]Sim.\n[n]Não.\n", "opção inválida, tente novamente.",str)
	if continuar_ou_finalizar == "s":
		F == True
	elif continuar_ou_finalizar == "n":
		print("Obrigado por usar o programa ^^")
		break
