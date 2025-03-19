def calculo_recisao(salario, meses_trabalhados, aviso_previo=True):
    """"
    Calculo simples de recisão de contrato de trabalho

    Parâmetros usados:
        salario (float): Salário mensal do funcionario
        meses_trabalhados (int): Quantos meses o funcionário trabalhou 
        aviso_previo (bool): Se o aviso prévio foi dado ou não
    
    Retorna:
        Um detalhamento do calculo da recisão  
    """

    saldo_salario = (salario / 30) * meses_trabalhados
    aviso = salario if aviso_previo else 0
    fgts = salario*0.08 * meses_trabalhados
    multa_fgts = fgts * 0.4
    total = saldo_salario + aviso + fgts

    return {
        "Saldo de Salário: ": round(saldo_salario),
        "Aviso Prévio: ": round(aviso),
        "FGTS: ": round(fgts),
        "Multa FGTS: ": round(multa_fgts),
        "Total: ": round(total)
    }