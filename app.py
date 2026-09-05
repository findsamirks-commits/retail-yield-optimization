from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Yield Optimization API")

# Define the expected input from the analytics team
class InventoryItem(BaseModel):
    sku_name: str
    current_inventory: int
    units_sold_yesterday: int
    days_to_expiry: int
    base_price: float

@app.post("/optimize-markdown")
def optimize_markdown(item: InventoryItem):
    # 1. Calculate operational risk
    days_of_supply = round(item.current_inventory / (item.units_sold_yesterday + 0.1), 1)
    
    if item.days_to_expiry <= 0:
        return {"risk_flag": "🚨 Expired / Write-off", "markdown": 0.0, "new_price": 0.0}
        
    # 2. Calculate target velocity gap
    target_velocity = item.current_inventory / item.days_to_expiry
    velocity_gap = target_velocity - item.units_sold_yesterday
    
    # 3. Prescribe pricing if high risk
    if velocity_gap <= 0 or days_of_supply <= item.days_to_expiry:
        return {"risk_flag": "✅ Safe", "markdown": 0.0, "new_price": item.base_price}
        
    percent_increase_needed = velocity_gap / (item.units_sold_yesterday + 0.1)
    required_discount = percent_increase_needed / 2.5
    
    # Cap at 50% and round to nearest 5%
    optimal_discount = min(0.50, max(0.0, required_discount))
    final_markdown = round(optimal_discount * 20) / 20
    
    return {
        "sku": item.sku_name,
        "risk_flag": "⚠️ High Risk (Markdown Required)",
        "recommended_markdown": final_markdown,
        "new_selling_price": round(item.base_price * (1 - final_markdown), 2)
    }