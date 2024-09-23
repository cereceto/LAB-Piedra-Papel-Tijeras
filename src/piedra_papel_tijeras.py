import random 

def ordenador_decide_jugada():
    return random.choice(["PIEDRA", "PAPEL", "TIJERAS"])

def usuario_decide_jugada():
    res = ''
    while res not in ["PIEDRA", "PAPEL", "TIJERAS"]:
        res = input("ELIGE PIEDRA, PAPEL O TIJERAS: ")
        if res not in ["PIEDRA", "PAPEL", "TIJERAS"]:
            print("ERROR")
    return res

def determina_ganador(usuario, ordenador):
    if usuario == ordenador:
        return "EMPATE"
    elif usuario == "PIEDRA" and ordenador == "TIJERAS":
        return "USUARIO GANA"
    elif usuario == "PAPEL" and ordenador == "PIEDRA":
        return "USUARIO GANA"
    elif usuario == "TIJERAS" and ordenador == "PAPEL":
        return "USUARIO GANA"
    else:
        return "ORDENADOR GANA"
    
def juego():
    usuario = usuario_decide_jugada()
    ordenador = ordenador_decide_jugada()
    print('EL USUARIO HA ELEGIDO:', usuario)
    print('EL ORDENADOR HA ELEGIDO:', ordenador)
    print('EL GANADOR ES:', determina_ganador(usuario, ordenador))
    return determina_ganador(usuario, ordenador)

def juego_a_n_rondas(n):
    rondas = 1
    user_win = 0
    cpu_win = 0 
    print('LA PARTIDA SE JUGARA HASTA QUE ALGUIEN GANE', n, 'VECES')
    while user_win < n and cpu_win < n:
        print('RONDA: ', rondas)
        partida = juego()
        if partida == 'USUARIO GANA':
            user_win = user_win + 1
            rondas = rondas + 1
        if partida == 'ORDENADOR GANA':
            cpu_win = cpu_win + 1
            rondas = rondas + 1
        if partida == 'EMPATE':
            rondas = rondas + 1
    if user_win == n:
        print("EL USUARIO GANA LA PARTIDA EN ", rondas, "RONDAS")
    if cpu_win == n:
        print("EL ORDENADOR GANA LA PARTIDA EN ", rondas, "RONDAS")