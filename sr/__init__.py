salario  = 1000
imposto  = 27.
while imposto > 0.:
    imposto  = input('imposto ou (0) para sair')
    if not imposto:
        imposto  = 27.
    else:
        imposto = float(imposto)
    print('Valor real : {0}'.format(salario -(salario * (imposto *0.1))))
    print("string de test1".replace("test1", "'teste2'"))
        
