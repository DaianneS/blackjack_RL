import random

ACOES = ["hit", "stick"]
VALORES_HI_LO = {1: -1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1}


class ShoeBlackjack:
    def __init__(self, num_baralhos=6):
        self.num_baralhos = num_baralhos
        self.cartas = []
        self.running_count = 0
        self.embaralhar()

    def embaralhar(self):
        # 13 cartas base * 4 naipes * número de baralhos
        # Nota: o 1 representa o Ás
        base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cartas = base * 4 * self.num_baralhos
        random.shuffle(self.cartas)
        self.running_count = 0

    def comprar_carta(self):
        # Se o baralho estiver acabando (ex: menos de 20% restante), reembaralha
        if len(self.cartas) < (52 * self.num_baralhos * 0.2):
            self.embaralhar()

        carta = self.cartas.pop()
        self.running_count += VALORES_HI_LO[carta]
        return carta

    def get_true_count(self):
        # True count = Running count / baralhos restantes
        baralhos_restantes = max(1, len(self.cartas) // 52)
        return round(self.running_count / baralhos_restantes)


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


def estado_jogo(mao_jogador, carta_dealer, true_count):
    return (
        valor_mao(mao_jogador),
        carta_dealer,
        int(tem_as_utilizavel(mao_jogador)),
        true_count
    )


def iniciar_partida(shoe):
    mao_jogador = [shoe.comprar_carta(), shoe.comprar_carta()]
    mao_dealer = [shoe.comprar_carta(), shoe.comprar_carta()]
    return mao_jogador, mao_dealer


def resolver_resultado_final(mao_jogador, mao_dealer, shoe):
    while valor_mao(mao_dealer) < 17:
        mao_dealer.append(shoe.comprar_carta())

    total_jogador = valor_mao(mao_jogador)
    total_dealer = valor_mao(mao_dealer)

    if total_dealer > 21 or total_jogador > total_dealer:
        return 1, "vitoria", mao_dealer
    elif total_jogador < total_dealer:
        return -1, "derrota", mao_dealer
    else:
        return 0, "empate", mao_dealer


def step_blackjack(mao_jogador, mao_dealer, acao, shoe):
    if acao == "hit":
        mao_jogador.append(shoe.comprar_carta())

        if valor_mao(mao_jogador) > 21:
            return None, -1, True, "derrota", mao_jogador, mao_dealer

        proximo_estado = estado_jogo(mao_jogador, mao_dealer[0], shoe.get_true_count())
        return proximo_estado, 0, False, "em_andamento", mao_jogador, mao_dealer

    elif acao == "stick":
        recompensa, resultado, mao_dealer = resolver_resultado_final(mao_jogador, mao_dealer, shoe)
        return None, recompensa, True, resultado, mao_jogador, mao_dealer

    else:
        raise ValueError("Ação inválida. Use 'hit' ou 'stick'.")


def partida_blackjack(shoe, policy=None, verbose=False, id_episodio=None):
    # Agora a partida exige a passagem do objeto shoe (baralho) instanciado
    mao_jogador, mao_dealer = iniciar_partida(shoe)
    carta_visivel_dealer = mao_dealer[0]

    historico = []
    done = False
    resultado_final = "em_andamento"
    recompensa_final = 0

    while not done:
        tc = shoe.get_true_count()
        estado_atual = estado_jogo(mao_jogador, carta_visivel_dealer, tc)

        if policy is None:
            acao_escolhida = random.choice(ACOES)
        else:
            acao_escolhida = policy(estado_atual)

        historico.append({
            "estado": estado_atual,
            "acao": acao_escolhida
        })

        _, recompensa_final, done, resultado_final, mao_jogador, mao_dealer = step_blackjack(
            mao_jogador, mao_dealer, acao_escolhida, shoe
        )

        if verbose:
            print(f"Estado: {estado_atual} | Ação: {acao_escolhida}")

    estado_final = estado_jogo(mao_jogador, carta_visivel_dealer, shoe.get_true_count())

    return {
        "id_episodio": id_episodio,
        "resultado": resultado_final,
        "recompensa": recompensa_final,
        "estado_final": estado_final,
        "mao_jogador": mao_jogador,
        "mao_dealer": mao_dealer,
        "historico": historico
    }