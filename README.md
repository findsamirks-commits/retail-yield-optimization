# 📉 Retail Yield Optimization API

An autonomous decision engine built to maximize gross margin and clear highly perishable grocery inventory before spoilage. 

## Features
* **Spoilage Risk Flagging:** Calculates Days of Supply (DOS) against remaining shelf life to automatically flag high-risk inventory.
* **Dynamic Markdown Engine:** Replaces static discounting with mathematical price elasticity models, prescribing the exact markdown percentage required to clear stock.
* **Margin Protection:** Automatically caps clearance markdowns at 50% to prevent unnecessary revenue leakage.

## Tech Stack
* **Analysis & Modeling:** Python, Pandas, Matplotlib, Seaborn
* **API Deployment:** FastAPI, Uvicorn, Pydantic

## Local Testing
Start the server by running `python -m uvicorn app:app --reload` and navigate to `http://127.0.0.1:8000/docs` to test inventory variables interactively.