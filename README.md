# 🚀 QTradeX Core — Build, Backtest & Optimize AI-Powered Crypto Trading Bots

<p>
  <img src="https://img.shields.io/github/stars/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
  <img src="https://img.shields.io/github/contributors/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
  <img src="https://img.shields.io/github/last-commit/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
  <img src="https://visitor-badge.laobi.icu/badge?page_id=squidKid-deluxe.QTradeX-Algo-Trading-SDK" />
  <img src="https://img.shields.io/github/languages/count/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
  <img src="https://img.shields.io/github/languages/top/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
  <img src="https://img.shields.io/github/issues/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
  <img src="https://img.shields.io/github/issues-pr/squidKid-deluxe/QTradeX-Algo-Trading-SDK" />
</p>

<p align="center">
  <img src="screenshots/Screenshot from 2025-05-02 18-50-54.png" width="100%" alt="QTradeX Demo Screenshot">
</p>

> 📸 See [screenshots.md](screenshots.md) for more visuals  
> 📚 Read the core docs on [QTradeX SDK DeepWiki](https://deepwiki.com/squidKid-deluxe/QTradeX-Algo-Trading-SDK)  
> 🤖 Explore the bots at [QTradeX AI Agents DeepWiki](https://deepwiki.com/squidKid-deluxe/QTradeX-AI-Agents)  
> 💬 Join our [Telegram Group](https://t.me/qtradex_sdk) for discussion & support

---

## ⚡️ TL;DR
**QTradeX** is a lightning-fast Python framework for designing, backtesting, and deploying algorithmic trading bots, built for **crypto markets** with support for **100+ exchanges**, **AI-driven optimization**, and **blazing-fast vectorized execution**.

Like what we're doing?  Give us a ⭐!

---

## 🎯 Why QTradeX?

Whether you're exploring a simple EMA crossover or engineering a strategy with 20+ indicators and genetic optimization, QTradeX gives you:

✅ Modular Architecture  
✅ Tulip + CCXT Integration  
✅ Custom Bot Classes  
✅ Fast, Disk-Cached Market Data  
✅ Near-Instant Backtests (even on Raspberry Pi!)

---

## 🔍 Features at a Glance

- 🧠 **Bot Development**: Extend `BaseBot` to craft custom strategies
- 🔁 **Backtesting**: Plug-and-play CLI & code-based testing
- 🧬 **Optimization**: Use QPSO or LSGA to fine-tune parameters
- 📊 **Indicators**: Wrapped Tulip indicators for blazing performance
- 🌐 **Data Sources**: Pull candles from 100+ CEXs/DEXs with CCXT

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/CjsTecnologias/master_bot_ia.git
cd master_bot_ia

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from qtradex.core.base_bot import BaseBot
from qtradex.indicators import qi

class MyBot(BaseBot):
    def __init__(self):
        super().__init__()
        
    def strategy(self, candles):
        # Your trading logic here
        ema_short = qi.ema(candles.close, 10)
        ema_long = qi.ema(candles.close, 20)
        
        if ema_short[-1] > ema_long[-1]:
            return 1  # Buy signal
        elif ema_short[-1] < ema_long[-1]:
            return -1  # Sell signal
        else:
            return 0  # Hold
```

---

## 📊 Backtesting

Run backtests with ease:

```bash
python -m qtradex.core.backtest --strategy MyBot --symbol BTCUSDT --timeframe 1h
```

---

## 🧬 Optimization

Optimize your strategies using genetic algorithms:

```python
from qtradex.optimizers import qpso

# Define parameter ranges
params = {
    'ema_short': (5, 15),
    'ema_long': (20, 50)
}

# Run optimization
best_params = qpso.optimize(MyBot, params, generations=100)
```

---

## 📈 Supported Exchanges

QTradeX supports 100+ exchanges through CCXT integration:

- Binance
- Coinbase Pro
- Kraken
- Bitfinex
- And many more...

---

## 🛠️ Advanced Features

### Custom Indicators
Create your own technical indicators or use our optimized Tulip wrappers.

### Risk Management
Built-in position sizing and risk management tools.

### Live Trading
Deploy your strategies to live markets with confidence.

### Paper Trading
Test strategies in real-time without risking capital.

---

## 📚 Documentation

- [Quick Start Guide](QUICKSTART.md)
- [Strategy Development](CUSTOMIZING_STRATEGIES.md)
- [Backtesting Guide](COMO_FUNCIONA_O_BACKTEST.md)
- [Optimization Guide](COMO_FUNCIONA_O_OTIMIZADOR.md)
- [Risk Management](RISK_MANAGEMENT.md)
- [API Keys Setup](API_KEYS_GUIDE.md)

---

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines for more details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

Trading cryptocurrencies involves substantial risk and may not be suitable for all investors. Past performance is not indicative of future results. Please trade responsibly and never invest more than you can afford to lose.

---

## 🌟 Support

If you find this project helpful, please give it a ⭐ on GitHub!

For support and discussions, join our [Telegram Group](https://t.me/qtradex_sdk).