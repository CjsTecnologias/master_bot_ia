# Guia de Configuração de API Keys - QTradeX

Este guia explica como configurar as API keys dos provedores de dados no arquivo `.env` para que o sistema funcione automaticamente sem modificações no código.

## 📋 Visão Geral

O QTradeX agora suporta **seleção automática e inteligente de provedores** baseada nas API keys disponíveis no seu arquivo `.env`. O sistema escolhe automaticamente o provedor mais rápido e eficiente para cada tipo de ativo.

## 🔧 Configuração do Arquivo .env

### Estrutura Básica

Seu arquivo `.env` deve conter as seguintes seções:

```env
# ============================================
# CONFIGURAÇÕES DA EXCHANGE PRINCIPAL
# ============================================
EXCHANGE_NAME=binance
API_KEY=your_exchange_api_key_here
API_SECRET=your_exchange_api_secret_here

# ============================================
# API KEYS DOS PROVEDORES DE DADOS
# ============================================

# Alpha Vantage (Ações, Forex, Crypto)
# Obtenha sua chave gratuita em: https://www.alphavantage.co/support/#api-key
ALPHAVANTAGE_API_KEY=

# CryptoCompare (Dados de Crypto)
# Obtenha sua chave gratuita em: https://min-api.cryptocompare.com/pricing
CRYPTOCOMPARE_API_KEY=

# Nomics (Dados de Crypto por Exchange)
# Obtenha sua chave gratuita em: https://nomics.com/docs/
NOMICS_API_KEY=

# ============================================
# CONFIGURAÇÕES AVANÇADAS
# ============================================

# Modo sandbox (true/false)
SANDBOX_MODE=false

# Preferência de provedor de dados
# Opções: auto, yahoo, ccxt, alphavantage, cryptocompare, nomics, synthetic, fdr
DATA_PROVIDER_PREFERENCE=auto
```

## 🚀 Provedores Disponíveis

### 1. Yahoo Finance (Sempre Disponível)
- **Velocidade**: ⚡ Muito Rápida (12+ candles/segundo)
- **API Key**: ❌ Não necessária
- **Suporte**: Cryptos principais (BTC, ETH, etc.) e ações
- **Limitações**: Apenas dados diários, cryptos limitados

### 2. CCXT (Sempre Disponível)
- **Velocidade**: 🐌 Moderada (1 candle/segundo)
- **API Key**: ❌ Não necessária
- **Suporte**: 100+ exchanges, todos os timeframes
- **Limitações**: Rate limits por exchange

### 3. Alpha Vantage (Requer API Key)
- **Velocidade**: 🐌 Lenta (5 calls/minuto)
- **API Key**: ✅ Necessária
- **Suporte**: Ações, forex, crypto principais
- **Limitações**: Apenas dados diários, rate limit baixo

### 4. CryptoCompare (Requer API Key)
- **Velocidade**: ⚡ Rápida (100 calls/segundo)
- **API Key**: ✅ Necessária
- **Suporte**: Ampla gama de cryptos
- **Limitações**: Apenas dados diários, máximo 2000 candles

### 5. Nomics (Requer API Key)
- **Velocidade**: 🐌 Lenta (1 call/segundo)
- **API Key**: ✅ Necessária
- **Suporte**: Dados específicos por exchange
- **Limitações**: Apenas dados diários

### 6. Finance Data Reader (Sempre Disponível)
- **Velocidade**: 🐌 Moderada
- **API Key**: ❌ Não necessária
- **Suporte**: Ações principalmente
- **Limitações**: Apenas dados diários, foco em ações

## 🧠 Sistema de Seleção Inteligente

Quando `DATA_PROVIDER_PREFERENCE=auto`, o sistema escolhe automaticamente:

### Para Cryptos Principais (BTC, ETH, ADA, DOT, LTC, XRP, BCH, LINK):
1. **Yahoo Finance** (se disponível) - Mais rápido
2. **CryptoCompare** (se API key disponível)
3. **CCXT** (fallback)

### Para Outros Cryptos:
1. **CryptoCompare** (se API key disponível)
2. **CCXT** (fallback)

### Para Ações:
1. **Alpha Vantage** (se API key disponível)
2. **Yahoo Finance** (fallback)
3. **Finance Data Reader** (fallback)

## 📝 Como Obter as API Keys

### Alpha Vantage
1. Acesse: https://www.alphavantage.co/support/#api-key
2. Registre-se gratuitamente
3. Copie sua API key
4. Adicione no `.env`: `ALPHAVANTAGE_API_KEY=sua_chave_aqui`

### CryptoCompare
1. Acesse: https://min-api.cryptocompare.com/pricing
2. Crie uma conta gratuita
3. Gere sua API key
4. Adicione no `.env`: `CRYPTOCOMPARE_API_KEY=sua_chave_aqui`

### Nomics
1. Acesse: https://nomics.com/docs/
2. Registre-se para uma conta gratuita
3. Obtenha sua API key
4. Adicione no `.env`: `NOMICS_API_KEY=sua_chave_aqui`

## ⚙️ Configurações Avançadas

### Forçar um Provedor Específico
Se você quiser usar sempre um provedor específico:

```env
DATA_PROVIDER_PREFERENCE=yahoo
```

Opções disponíveis:
- `auto` - Seleção automática (recomendado)
- `yahoo` - Sempre Yahoo Finance
- `ccxt` - Sempre CCXT
- `alphavantage` - Sempre Alpha Vantage
- `cryptocompare` - Sempre CryptoCompare
- `nomics` - Sempre Nomics
- `synthetic` - Dados sintéticos
- `fdr` - Finance Data Reader

### Modo Sandbox
Para testes, você pode ativar o modo sandbox:

```env
SANDBOX_MODE=true
```

## 🔍 Verificação de Status

O sistema automaticamente:
- ✅ Detecta quais API keys estão configuradas
- ✅ Escolhe o melhor provedor disponível
- ✅ Faz fallback para provedores alternativos
- ✅ Exibe mensagens informativas sobre qual provedor está sendo usado

## ⚠️ Troubleshooting

### Erro: "You must get an API key from..."
- Verifique se a API key está corretamente configurada no `.env`
- Certifique-se de que não há espaços extras na chave
- Verifique se o arquivo `.env` está na raiz do projeto

### Provedor não está sendo usado
- Verifique se `DATA_PROVIDER_PREFERENCE=auto`
- Confirme se a API key está válida
- Verifique os logs para ver qual provedor está sendo selecionado

### Performance lenta
- Configure as API keys dos provedores mais rápidos (CryptoCompare, Yahoo)
- Use `DATA_PROVIDER_PREFERENCE=yahoo` para cryptos principais
- Evite Alpha Vantage para uso intensivo (rate limit baixo)

## 📊 Comparação de Performance

| Provedor | Velocidade | API Key | Melhor Para |
|----------|------------|---------|-------------|
| Yahoo Finance | 12+ candles/s | ❌ | Cryptos principais |
| CryptoCompare | 100 calls/s | ✅ | Todos os cryptos |
| CCXT | 1 candle/s | ❌ | Exchanges específicas |
| Alpha Vantage | 5 calls/min | ✅ | Ações |
| Nomics | 1 call/s | ✅ | Dados por exchange |
| FDR | Moderada | ❌ | Ações |

## 🎯 Recomendações

1. **Para uso geral**: Configure `CRYPTOCOMPARE_API_KEY` e use `DATA_PROVIDER_PREFERENCE=auto`
2. **Para cryptos principais**: Yahoo Finance é o mais rápido
3. **Para ações**: Configure `ALPHAVANTAGE_API_KEY`
4. **Para exchanges específicas**: Use CCXT
5. **Para máxima velocidade**: Configure todas as API keys e use `auto`

---

💡 **Dica**: O sistema é inteligente e sempre escolherá o provedor mais eficiente baseado no que você tem configurado. Não é necessário modificar código!