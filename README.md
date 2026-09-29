# automation-tool-45

`automation-tool-45` is a high-performance Python framework designed to automate trade execution and portfolio rebalancing across multiple decentralized exchanges. It leverages asynchronous processing to minimize latency, ensuring optimal order routing in volatile crypto markets.

## Features
*   **Multi-DEX Aggregator:** Seamlessly interacts with Uniswap V3, PancakeSwap, and SushiSwap via unified APIs.
*   **Asynchronous Execution:** Utilizes `asyncio` and `aiohttp` to manage concurrent order requests with sub-millisecond precision.
*   **Risk Management Engine:** Configurable circuit breakers that halt trading automatically based on user-defined drawdown thresholds.
*   **Encrypted Key Storage:** Implements Fernet symmetric encryption to secure private keys locally, preventing exposure in configuration files.

## Installation

Ensure you have Python 3.10+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-45.git
cd automation-tool-45
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Basic Usage

1. **Configure Environment:** Create a `.env` file and populate your node provider URL and encrypted credentials:
   ```bash
   cp .env.example .env
   # Edit .env with your RPC URL and API keys
   ```

2. **Run Strategy:** Execute a basic market-making strategy:
   ```bash
   python main.py --strategy mm_base --pair ETH/USDT --amount 1.5
   ```

3. **Monitor:** Real-time trade logs will be generated in `logs/trading.log`.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.

---
*Disclaimer: This tool is for educational and experimental purposes. Always test strategies on testnets before deploying capital to mainnet environments.*