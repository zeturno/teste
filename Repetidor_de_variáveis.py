def repetidor(valor_ou_str,msg_de_erro,definicao):
    while:
         try:
            #valores a serem adicionados.
             valor = definicao(input(valor_ou_str))
             break
        except:
            print(msg_de_erro)
            return valor
