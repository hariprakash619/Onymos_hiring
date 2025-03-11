# Stock Order Matching System

This project simulates a stock order matching system where multiple threads (representing stockbrokers) add and match buy and sell orders concurrently. The system supports 1,024 different tickers (stocks) being traded.

## Features

- Add buy and sell orders for different tickers.
- Match buy and sell orders based on price.
- Simulate active stock transactions with multiple threads.
- Handle race conditions when multiple threads modify the stock order book.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the `main.py` file to start the simulation.

```bash
python3 main.py
