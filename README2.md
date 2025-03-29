# 🦍 Trading Bot — Modular Screener, Backtester & Execution Engine

## 🎯 Project Overview

This project is an automated stock trading system built in **usable, modular chunks**, allowing for **manual trading, strategy validation, and full automation over time.**

It is designed to:

1. **Screen potential trade candidates** based on technical analysis criteria.
2. **Support manual trading with saved screener output and configs.**
3. **Backtest different screener + order configs on historical data.**
4. **Optionally execute trades automatically** via Interactive Brokers API.
5. **Track trade outcomes and generate daily reports.**
6. **Provide strategy analysis & performance reporting.**
7. **Optionally run fully automated 24/7.**
8. **Optionally include a web UI for live monitoring & control.**

The project is:

- **Modular** → Each piece (screener, backtester, executor) is cleanly separated.
- **Typed & Configurable** → Strategy configs are stored and versioned.
- **Usable early** → Starts as a practical manual screener + logger.
- **Tested** → Unit + integration tested with `pytest`.
- **Scalable** → Grows into a full auto-trading engine with analytics & UI.

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **SQLite** (initial DB)
- **Yahoo Finance API (via yfinance)** → Phase 1
- **IBKR API** (via `ib_insync`) → Phase 3
- **pytest** for testing
- **Pandas, NumPy** for backtesting & analysis
- **Next.js + FastAPI (optional UI)** → Phase 6
- **VPS/Cloud Server deployment** → Phase 5

---

## 🧩 Key Concepts

- **ScreenerConfig** defines both external (query) and internal (post-fetch) filters.
- **OrderConfig** defines trade entry logic (entry price, stop loss, take profit).
- **Trade tracking** handled via DB, and later enriched by IBKR account queries.
- **Backtesting** provides strategy confidence before automating trades.
- **Reports & analysis** provide insights to refine strategy over time.
- **Full automation** ensures system runs without human intervention.
- **Optional UI** allows for live trade monitoring, approval, and config changes.

---

## 🗂️ Folder Structure & Responsibilities

| Folder         | Responsibility                                                                      |
| -------------- | ----------------------------------------------------------------------------------- |
| `config/`      | Global settings & static config (DB path, API creds)                                |
| `database/`    | Handles DB schema, operations & typed data models                                   |
| `market_data/` | Pulls external market data (e.g. Yahoo) + ticker list scraper + query-level filters |
| `screener/`    | Applies post-fetch strategy rules & candidate ranking                               |
| `execution/`   | Sends trade orders to broker & queries trade/account status (for Phase 3)           |
| `reports/`     | Generates CLI + Markdown reports + analysis (Phase 4)                               |
| `analysis/`    | Backtesting logic + performance analysis tools                                      |
| `ui/`          | (Optional) Web-based dashboard & control panel (Phase 6)                            |
| `tests/`       | Unit + integration tests for all components                                         |
| `main.py`      | Master pipeline script (manual or automated runs)                                   |

---

## 🚀 Project Phases

### ✅ Phase 1 — Screener + Logger (Manual Use)

- Create ScreenerConfig structure (query + post-fetch filters).
- Implement screener logic using Yahoo Finance (EOD data).
- Save screener results + config to SQLite.
- Unit tests for screener logic.
- CLI + Markdown report of daily screener results.
- _Manually place trades based on screener output._

---

### 🔁 Phase 2 — Backtester

- Add OrderConfig structure.
- Build backtester module using historical data.
- Simulate trades using ScreenerConfig + OrderConfig.
- Log and analyze simulated results.
- Unit tests for backtester logic.
- _(Strategy tuning becomes possible here.)_

---

### 🔒 Phase 3 — Execution Engine

- Integrate Interactive Brokers API.
- Create order placement logic from screener output.
- Query account status & trade results.
- Paper Trading first → Live Trading optional.
- E2E testing (screen → place → update).
- Manual trade approval option (optional safety).

---

### 📊 Phase 4 — Reports & Analysis

- Build Pandas-based analysis notebooks/scripts.
- Automate daily/weekly/monthly performance reports.
- CLI summary script for trade history & stats.
- Optional: Web dashboard for visualization.
- Track long-term performance & strategy effectiveness.

---

### ⚙️ Phase 5 — Full Automation & Deployment (Optional)

- Automate full daily pipeline (screener → orders → tracking → reports).
- Add error handling & retry logic.
- Optional trade approval workflow.
- Notification system (email/Telegram) for trade status & errors.
- Deploy to VPS or cloud server for 24/7 operation.
- Live risk management settings (max position size, daily loss cap).

---

### 🖥️ Phase 6 — User Interface & Control Panel (Optional)

- Build a web-based dashboard (Next.js + FastAPI backend).
- View screener results, trade history, config versions.
- Visual P/L charts and trade performance stats.
- Optional trade approval & manual execution controls.
- Live account status monitoring.
- Strategy config editing via UI (optional).

---

## 📝 Status

**Current Stage:** 🟢 Building usable manual screener (Phase 1)  
**Next Milestone:** CLI screener output → DB → report → start placing trades manually

---

**Built by Ardalan Jaf**
