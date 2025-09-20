# QX Framework: Writing a New Bot

The **QX Framework** is a powerful and flexible platform for creating and backtesting trading bots. In this guide, we'll walk you through the process of creating a new bot from scratch, detailing key concepts, configuration options, and strategies.

For examples on how to build bots for QX, see [this repository](https://github.com/squidKid-deluxe/qtradex-ai-agents).

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Creating a New Bot](#creating-a-new-bot)
    1. [Bot Structure](#bot-structure)
    2. [Configuring the Bot Parameters](#configuring-the-bot-parameters)
    3. [Defining Indicators](#defining-indicators)
    4. [Building a Strategy](#building-a-strategy)
4. [Testing and Backtesting](#testing-and-backtesting)
5. [Plotting and Visualization](#plotting-and-visualization)
6. [Optimizing the Bot](#optimizing-the-bot)
7. [Deployment](#deployment)
8. [Advanced Topics](#advanced-topics)
9. [Resources and Documentation](#resources-and-documentation)

---

## Introduction

The QX framework allows you to write sophisticated trading bots that interact with various cryptocurrency exchanges. By providing high-level abstractions for trading strategies, risk management, and data handling, QX simplifies the development process for algorithmic traders. This guide will help you create a bot, configure it, and deploy it to trade in various market conditions.

---

## Prerequisites

Before you begin, ensure you have the following:

1. **Python 3.9+**: The QX framework relies on Python, so make sure you have Python 3.9 or higher installed.
2. **QX Framework**: Install QX using pip:
   ```bash
   pip install qtradex
   ```
3. **Knowledge of Trading Concepts**: Familiarity with trading concepts (e.g., moving averages, stop loss, take profit, etc.) will be helpful.
4. **API Key for Exchange**: You'll need an API key from an exchange (e.g., Poloniex, Binance) for live trading or backtesting.

---

## Creating a New Bot

To create a new bot, you will subclass the `qx.core.BaseBot` class. This base class provides several methods and functionalities that can be customized to define your own trading logic.

### Bot Structure

A QX bot generally consists of the following components:

- **Initialization (`__init__`)**: Set up parameters and initial values.
- **Indicators**: Define the technical indicators that your bot will use to make decisions (e.g., moving averages, RSI, MACD).
- **Strategy**: Define the trading logic — the rules for buying, selling, and holding positions.
- **Fitness**: Define the performance metrics (e.g., ROI, Sortino ratio) used for evaluating the bot's success.
- **Plotting**: Visualize the bot's trades and indicators.
- **Autorange**: Automatically adjust parameters based on market conditions.

#### Example Bot Template:

```python
import qtradex as qx
from qtradex.indicators import tulipy as tu
from qtradex.private.signals import Buy, Sell, Thresholds

class Bot(qx.core.BaseBot):
    def __init__(self):
        self.tune = {
            "ema": 14,
            "std": 14,
            "buy_factor": 1.05,
            "sell_factor": 0.95,
        }
        self.clamps = [
            [5, 100, 0.5],  # Clamps for period of EMA
            [1.0, 4.0, 0.5],  # Clamps for Standard Deviation
        ]

    def indicators(self, data):
        metrics = {}
        metrics["ema"] = tu.ema(data["close"], self.tune["ema"])
        metrics["std"] = tu.stddev(data["close"], self.tune["std"])
        return metrics

    def strategy(self, tick_info, indicators):
        price = tick_info["close"]
        ema = indicators["ema"]
        std = indicators["std"]

        # Example trading strategy
        if price < ema - std * self.tune["buy_factor"]:
            return Buy()
        elif price > ema + std * self.tune["sell_factor"]:
            return Sell()
        else:
            return Thresholds(buying=price, selling=price)

    def fitness(self, states, raw_states, asset, currency):
        return ["roi", "cagr", "sortino", "maximum_drawdown"], {}
```