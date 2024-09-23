from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    print('TEST ORDENADOR DECIDE JUGADA')
    res = ordenador_decide_jugada()
    print('EL ORDENADOR HA ELEGIDO:', res)

def test_usuario_decide_jugada():
    print('TEST USUARIO DECIDE JUGADA')
    res = usuario_decide_jugada()
    print('EL USUARIO HA ELEGIDO:', res)

def test_determina_ganador(usuario, ordenador):
    print('TEST DETERMINA GANADOR')
    res = determina_ganador(usuario, ordenador)
    print('EL GANADOR ES:', res)

def test_juego():
    print('TEST JUEGO')
    juego()

def test_juego_a_n_rondas(n):
    print('TEST JUEGO A N RONDAS')
    juego_a_n_rondas(n)

if __name__ == '__main__':

    print('------------------------------------')
    test_ordenador_decide_jugada()
    print('------------------------------------')
    test_usuario_decide_jugada()
    print('------------------------------------')
    test_determina_ganador('PIEDRA', 'TIJERAS')
    print('------------------------------------')
    test_determina_ganador('PIEDRA', 'PAPEL')
    print('------------------------------------')
    test_determina_ganador('PIEDRA', 'PIEDRA')
    print('------------------------------------')
    test_determina_ganador('TIJERAS', 'PIEDRA')
    print('------------------------------------')
    test_determina_ganador('TIJERAS', 'PAPEL')
    print('------------------------------------')
    test_determina_ganador('TIJERAS', 'TIJERAS')
    print('------------------------------------')
    test_determina_ganador('PAPEL', 'PIEDRA')
    print('------------------------------------')
    test_determina_ganador('PAPEL', 'TIJERAS')
    print('------------------------------------')
    test_determina_ganador('PAPEL', 'PAPEL')
    print('------------------------------------')
    test_juego_a_n_rondas(3)
    print('------------------------------------')
    

