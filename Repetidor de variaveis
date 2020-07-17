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
