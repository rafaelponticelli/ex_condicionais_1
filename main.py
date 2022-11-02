#funçoes formulas de calculo



def formula ():
    salario = float(input("Digite o Salário Atual :"))
  
    if  (salario <= 1280.00 ): #20%   
        reajuste =  (20 * salario) / 100
        percentual = "20%"
        novo_Salario = salario + reajuste
        
        print("Salario atual :",salario,
        "\nPercetual de aumento :",percentual,
        "\nVocê ganhou de aumento :",reajuste, 
        "\nSeu novo salario é de :",novo_Salario) 
    elif(salario > 1280.00  and salario  <= 1700.00): #15%
        reajuste =  (15 * salario) / 100
        percentual = "15%"
        novo_Salario = salario + reajuste

        print("Salario atual :",salario,
        "\nPercetual de aumento :",percentual,
        "\nVocê ganhou de aumento :",reajuste, 
        "\nSeu novo salario é de :",novo_Salario) 

    elif(salario > 1700.00 and salario <= 2500.00): #10%
        reajuste =  (10 * salario) / 100
        percentual = "10%"
        novo_Salario = salario + reajuste
        
        print("Salario atual :",salario,
        "\nPercetual de aumento :",percentual,
        "\nVocê ganhou de aumento :",reajuste, 
        "\nSeu novo salario é de :",novo_Salario) 

    elif(salario > 2500 ): #5%
        reajuste =  (5 * salario) / 100
        percentual = "5%"
        novo_Salario = salario + reajuste

        print("Salario atual :",salario,
        "\nPercetual de aumento :",percentual,
        "\nVocê ganhou de aumento :",reajuste, 
        "\nSeu novo salario é de :",novo_Salario) 