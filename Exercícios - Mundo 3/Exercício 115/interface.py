def menu(lista=list()):
    import textos
    from cores import cor
    textos.título('MENU PRINCIPAL')
    for i in range(0, len(lista)):
        print(f'{cor(i+1,"Ama", imprimir=False)} - {cor(lista[i],"Azu", imprimir=False)}')
    textos.linhas()
    return textos.selInt(1, len(lista), cor('Sua Opção: ', 'verde', imprimir=False))