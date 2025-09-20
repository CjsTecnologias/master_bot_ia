"""
╔═╗╔═╗╔═╗╔═╗╦╔═╗
╚═╗╠═╣╠═╝║  ║║
╚═╝╩ ╩╩  ╚═╝╩╚═╝

Este arquivo define a classe `BaseBot`, que serve como o "esqueleto" ou a
classe base para todas as estratégias de trading no ecossistema QTradeX.

O OBJETIVO DESTE ARQUIVO é fornecer uma estrutura padrão que garante que
todas as estratégias tenham os mesmos métodos essenciais, permitindo que o motor
do QTradeX (seja para backtest, live trading ou otimização) possa interagir
com elas de forma consistente.

Qualquer nova estratégia que você criar DEVE herdar desta classe.

-------------------------------------------------------------------------------
FUNÇÕES (MÉTODOS) PRINCIPAIS A SEREM IMPLEMENTADOS/SOBRESCRITOS:
-------------------------------------------------------------------------------

1.  `__init__(self)`:
    - Onde você define os parâmetros iniciais da sua estratégia, como os
      períodos dos indicadores. Estes parâmetros ficam no dicionário `self.tune`.
    - É aqui também que definimos o controle de risco (`self.trade_amount_percentage`).

2.  `indicators(self, data)`:
    - **Obrigatório.**
    - Recebe os dados de mercado (`data`) e deve retornar um dicionário com todos
      os indicadores técnicos calculados (ex: Médias Móveis, RSI, Bandas de
      Bollinger, etc.).

3.  `strategy(self, state, indicators)`:
    - **Obrigatório.**
    - O coração da sua estratégia. Este método recebe o estado atual do mercado
      e os indicadores calculados e deve decidir qual ação tomar.
    - Deve retornar `qx.Buy()`, `qx.Sell()` ou `None` (para não fazer nada).

4.  `get_trade_amount(self, currency_balance)`:
    - **Opcional, mas recomendado para controle de risco.**
    - Define a quantidade de capital a ser usada em cada negociação.
    - Por padrão (se não for sobrescrito), o sistema usará 100% do saldo
      disponível, o que é arriscado.
    - As estratégias no repositório já sobrescrevem este método para usar
      apenas uma porcentagem do saldo.

5.  `plot(self, ...)`:
    - **Opcional.**
    - Permite que você visualize seus indicadores customizados nos gráficos
      gerados pelo QTradeX.

6.  `fitness(self, ...)`:
    - **Opcional.**
    - Usado pelo otimizador (`tune_manager`). Define quais métricas de
      performance (ex: ROI, Sortino Ratio, Win Rate) serão usadas para
      avaliar e "pontuar" uma determinada configuração de parâmetros.

"""
from math import ceil, inf

import matplotlib.pyplot as plt


class BaseBot:
    def autorange(self):
        """
        Returns:
         -Um número inteiro de dias que este bot requer para aquecer seus indicadores
        """
        return (
            ceil(max(v for k, v in self.tune.items() if k.endswith("_period")))
            if any(k.endswith("_period") for k in self.tune)
            else 0
        )

    def indicators(self, data):
        raise NotImplementedError

    def plot(self, data, states, indicators, block):
        raise NotImplementedError

    def strategy(self, state, indicators):
        raise NotImplementedError

    def reset(self):
        """
        redefinir quaisquer classes de armazenamento interno
        a serem implementadas pelo usuário
        """
        pass

    def execution(self, signal, indicators, wallet):
        return signal

    def fitness(self, states, raw_states, asset, currency):
        return ["roi"], {}


class Info(dict):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        raise TypeError(
            "Este dicionário é somente leitura. Use o método '_set' para atualizar os valores."
        )

    def _set(self, key, value):
        self._data[key] = value

    def __repr__(self):
        return repr(self._data)

    def __contains__(self, key):
        return key in self._data