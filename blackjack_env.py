import random

ACOES = ["hit", "stick"]

def comprar_carta():
    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(baralho)

def valor_mao(mao):
    total = sum(mao)
    ases = mao.count(1)

    while ases > 0 and total + 10 <= 21:
        total += 10
        ases -= 1

    return total

def tem_as_utilizavel(mao):
    total = sum(mao)
    return 1 in mao and total + 10 <= 21

def estado_jogo(mao_jogador, carta_dealer):
    return (
        valor_mao(mao_jogador),
        carta_dealer,
        int(tem_as_utilizavel(mao_jogador))
    )

def iniciar_partida():
    mao_jogador = [comprar_carta(), comprar_carta()]
    mao_dealer = [comprar_carta(), comprar_carta()]
    return mao_jogador, mao_dealer

def resolver_resultado_final(mao_jogador, mao_dealer):
    while valor_mao(mao_dealer) < 17:
        mao_dealer.append(comprar_carta())

    total_jogador = valor_mao(mao_jogador)
    total_dealer = valor_mao(mao_dealer)

    if total_dealer > 21 or total_jogador > total_dealer:
        return 1, "vitoria", mao_dealer
    elif total_jogador < total_dealer:
        return -1, "derrota", mao_dealer
    else:
        return 0, "empate", mao_dealer

def step_blackjack(mao_jogador, mao_dealer, acao):
    if acao == "hit":
        mao_jogador.append(comprar_carta())

        if valor_mao(mao_jogador) > 21:
            return None, -1, True, "derrota", mao_jogador, mao_dealer

        proximo_estado = estado_jogo(mao_jogador, mao_dealer[0])
        return proximo_estado, 0, False, "em_andamento", mao_jogador, mao_dealer

    elif acao == "stick":
        recompensa, resultado, mao_dealer = resolver_resultado_final(mao_jogador, mao_dealer)
        return None, recompensa, True, resultado, mao_jogador, mao_dealer

    else:
        raise ValueError("Ação inválida. Use 'hit' ou 'stick'.")

def partida_blackjack(policy=None, verbose=False, id_episodio=None):
    mao_jogador, mao_dealer = iniciar_partida()
    carta_visivel_dealer = mao_dealer[0]

    historico = []
    done = False
    resultado_final = "em_andamento"
    recompensa_final = 0

    while not done:
        estado_atual = estado_jogo(mao_jogador, carta_visivel_dealer)

        if policy is None:
            acao_escolhida = random.choice(ACOES)
        else:
            acao_escolhida = policy(estado_atual)

        historico.append({
            "estado": estado_atual,
            "acao": acao_escolhida
        })

        _, recompensa_final, done, resultado_final, mao_jogador, mao_dealer = step_blackjack(
            mao_jogador, mao_dealer, acao_escolhida
        )

        if verbose:
            print(f"Estado: {estado_atual} | Ação: {acao_escolhida}")

    return {
        "id_episodio": id_episodio,
        "resultado": resultado_final,
        "recompensa": recompensa_final,
        "estado_final": estado_jogo(mao_jogador, carta_visivel_dealer),
        "mao_jogador": mao_jogador,
        "mao_dealer": mao_dealer,
        "historico": historico
    }