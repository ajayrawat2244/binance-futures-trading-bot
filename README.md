# Binance Futures Trading Bot
A Python-based trading bot for Binance Futures Testnet that supports MARKET and LIMIT orders using CLI commands. The project includes logging, input validation, modular architecture, and exception handling.

---

## Features
- Place MARKET and LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- CLI-based input handling- Input validation
- Logging system for API requests and responses
- Exception handling for API and network errors
- Structured and reusable project architecture

---

## Technologies Used
- Python 3
- Requests
- python-dotenv
- Binance Futures Testnet API

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ajayrawat2244/binance-futures-trading-bot.git


## Move into Project Directory
cd binance-futures-trading-bot

## Create Virtual Environment
python -m venv venv

## Activate Virtual Environment
#Windows
venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Environment Setup
# Create a .env file in the project root directory and add your Binance Futures Testnet API credentials:
BINANCE_API_KEY=your_binance_testnet_api_keyBINANCE_API_SECRET=your_binance_testnet_secret_key

## Generate API keys from Binance Futures Testnet:
https://testnet.binancefuture.com/

## Usage
# MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000

## Example Output
===== ORDER REQUEST =====
Symbol: BTCUSDTSide: BUY
Order Type: MARKET
Quantity: 0.001
===== ORDER RESPONSE =====
Order ID: 13121393426
Status: NEW
Executed Qty: 0.0000
Average Price: 0.00Order placed successfully.

## Project Structure
binance-futures-trading-bot/
│├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│├── logs/
│   └── bot.log
│├── cli.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore

## Logging
# All API requests, responses, and errors are stored in:
logs/bot.log

## Error Handling
# The application handles:


Invalid user inputs


Missing parameters


API authentication errors


Network failures


Invalid order types



## Author
# Ajay Singh Rawat