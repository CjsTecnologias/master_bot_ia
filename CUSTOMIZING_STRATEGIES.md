# Guia Rápido para Personalizar Suas Estratégias de Trading

Este documento explica como você pode facilmente modificar os parâmetros de qualquer estratégia dentro do diretório `strategies` para realizar backtests ou prepará-la para negociação em tempo real.

As modificações são feitas diretamente no arquivo Python da estratégia (por exemplo, `extinction_event.py`). A maioria das configurações importantes se encontra na função `main()`, localizada no final do arquivo.

---

### 1. Como Alterar o Par de Negociação (Ativo)

Para testar a estratégia com um par de moedas diferente (ex: `BTC/USD`), você só precisa alterar as variáveis `asset` e `currency`.

**Onde modificar:** Dentro da função `main()`.

**Exemplo:**
```python
def main():
    # Altere o par de negociação aqui
    asset, currency = "BTC", "USD"
    
    # O restante do código usará esses novos valores
    wallet = qx.PaperWallet({asset: 0, currency: 1000})
    data = qx.Data(
        exchange="binance", # Certifique-se de que a exchange tem o par
        asset=asset,
        currency=currency,
        begin="2022-01-01",
    )
    # ...
```

---

### 2. Como Ajustar o Período do Backtest

Você pode definir um intervalo de tempo específico para seus testes históricos, alterando os parâmetros `begin` (início) e `end` (fim).

**Onde modificar:** Na chamada `qx.Data()` dentro da função `main()`.

**Exemplo:**
```python
def main():
    # ...
    data = qx.Data(
        exchange="binance",
        asset=asset,
        currency=currency,
        begin="2021-01-01",  # <-- Altere a data de início
        end="2023-06-30",      # <-- Altere ou adicione a data de fim
    )
    # ...
```
**Nota:** Se o parâmetro `end` for omitido, o backtest usará dados até a data mais recente disponível.

---

### 3. Como Configurar o Saldo Inicial (Carteira)

Para simular um backtest com um capital inicial diferente, ajuste os valores na criação da `PaperWallet`.

**Onde modificar:** Na chamada `qx.PaperWallet()` dentro da função `main()`.

**Exemplo:**
```python
def main():
    asset, currency = "BTC", "USD"

    # Configurando um saldo inicial de 0 BTC e 5000 USD
    wallet = qx.PaperWallet({asset: 0, currency: 5000}) # <-- Altere os valores aqui
    
    # ...
```

---

### 4. Como Otimizar os Parâmetros da Estratégia

Esta é a parte mais poderosa da personalização. Cada estratégia possui um dicionário chamado `self.tune` que controla o comportamento dos indicadores (médias móveis, RSI, etc.). Ajustar esses valores é fundamental para otimizar a performance.

**Onde modificar:** Dentro do método `__init__` da classe da sua estratégia.

**Exemplo (`ExtinctionEvent`):**
```python
class ExtinctionEvent(qx.BaseBot):
    def __init__(self):
        # Estes são os "ajustes finos" da sua estratégia
        self.tune = {
            "ma1_period": 5.8,       # Período da primeira média móvel
            "ma2_period": 15.0,      # Período da segunda média móvel
            "ma3_period": 30.0,      # Período da terceira média móvel
            "selloff_ratio": 0.5,    # Sensibilidade para venda
            # ... outros parâmetros
        }
        # ...
```
Experimente alterar esses números para ver como a estratégia reage de maneira diferente às condições de mercado.

---

### 5. Como Mudar a Fonte dos Dados (Exchange)