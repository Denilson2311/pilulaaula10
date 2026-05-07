def acao_semaforo(cor: str):
    cor = cor.lower()
    if cor.lower()== 'vermelho':
        return 'Pare'
    elif cor == 'amarelo':
        return 'Atenção'
    elif cor == 'verde':
        return 'Siga'
    return 'Cor invalida'