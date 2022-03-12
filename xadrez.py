def MatrixChallenge(strArr):
    coordenadas = extrairCoordenadas(strArr)
    coordRainha = coordenadas[0]
    coordRei = coordenadas[1]
    tabuleiro = criarTabuleiro(8, 8, None)
    tabuleiro = setPosicao(tabuleiro, coordRainha, 'rainha')
    tabuleiro = setPosicao(tabuleiro, coordRei, 'rei')
    tabuleiro = simularMovimentosRainha(tabuleiro, coordRainha)
    tabuleiro, posicoesSeguras = simularMovimentosRei(tabuleiro, coordRei)
    tabuleiro, emXeque = simularXequeRainha(tabuleiro, coordRainha, coordRei)
    if emXeque:
        return posicoesSeguras
    return -1

def simularXequeRainha(tabuleiro, coordRainha, coordRei):
    for x in range(-8, 8):
        try:
            if (coordRei[0] == (coordRainha[0] + x) and coordRei[1] == coordRainha[1]) or\
               (coordRei[0] == coordRainha[0] and coordRei[1] == (coordRainha[1] + x)) or\
               (coordRei[0] == (coordRainha[0] + x) and coordRei[1] == (coordRainha[1] + x)) or\
               (coordRei[0] == (coordRainha[0] + x) and coordRei[1] == (coordRainha[1] + x)) or\
               (coordRei[0] == (coordRainha[0] - x) and coordRei[1] == (coordRainha[1] + x)):
                return tabuleiro, True
        except IndexError:
            pass
    return tabuleiro, False

def simularMovimentosRainha(tabuleiro, coordRainha):
    for x in range(-8, 8):
        try:
            tabuleiro[coordRainha[0] + x][coordRainha[1]] = 'rainha'
            tabuleiro[coordRainha[0]][coordRainha[1] + x] = 'rainha'
            tabuleiro[coordRainha[0] + x][coordRainha[1] + x] = 'rainha'
            tabuleiro[coordRainha[0] + x][coordRainha[1] + x] = 'rainha'
            tabuleiro[coordRainha[0] - x][coordRainha[1] + x] = 'rainha'
        except IndexError:
            pass
    return tabuleiro

def simularMovimentosRei(tabuleiro, coordRei):
    posicoesSeguras = 0
    for x in range(-1, 2):
        coordX = coordRei[0] + x
        for y in range(-1, 2):
            coordY = coordRei[1] + y
            if coordX >= 0 and coordY >=0:
                try:
                    if tabuleiro[coordX][coordY] is None:
                        tabuleiro[coordX][coordY] = 'rei'
                        posicoesSeguras += 1
                except IndexError:
                    pass
    return tabuleiro, posicoesSeguras

def emXequeLinha(coordRainha, coordRei):
    "Verifica se em xeque em linha reta"
    if coordRainha[0] == coordRei[0] or coordRainha[1] == coordRei[1]:
        return True
    return False

def setPosicao(tabuleiro: list, coord: list, peca: str):
    tabuleiro[coord[0]][coord[1]] = peca
    return tabuleiro

def extrairCoordenadas(strArr) -> list:
    """Recebe strArr, retorna uma lista com as coordenadas
    de rainha e rei.
    Args:
        strArr (type): strArr
    Returns:
        list: lista de coordenadas
    """
    xRainha = int(strArr[0].split(",")[0][1:]) -1
    yRainha = int(strArr[0].split(",")[1][:-1]) -1
    xRei = int(strArr[1].split(",")[0][1:]) -1
    yRei = int(strArr[1].split(",")[1][:-1]) -1
    return [[xRainha, yRainha], [xRei, yRei]]

def criarTabuleiro(x: int, y: int, valor) -> list:
    """Cria uma matriz com um numero de colunas(x) e linhas(y)
    Args:
        x (int): numero de colunas
        y (int): numero de linhas
        valor (type): description

    Returns:
        list: retorna a matriz
    """
    matriz = []
    for i in range(x):
        linhas = []
        for ii in range(y):
            linhas.append(valor)
        matriz.append(linhas)
    return matriz

print(MatrixChallenge(["(4,4)", "(6,6)"]))
