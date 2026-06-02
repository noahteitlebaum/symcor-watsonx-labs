from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Credit Card Recommendation Tool API")

# Canadian Bank credit card data with pricing information
CREDIT_CARDS = {
    "Maple Rewards Visa Infinite": {
        "annual_fee": 120,
        "description": "Premium travel rewards card with accelerated points on groceries, gas, and travel",
        "available_provinces": ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"],
        "credit_terms": [6, 12, 24, 36],
        "min_credit_limit": 5000,
        "rewards_preference": "travel"
    },
    "Maple Cash Back Mastercard": {
        "annual_fee": 99,
        "description": "Versatile cash back card with up to 4% cash back on groceries and recurring bills",
        "available_provinces": ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"],
        "credit_terms": [6, 12, 24, 36],
        "min_credit_limit": 2000,
        "rewards_preference": "cash back"
    },
    "Maple Travel Elite Visa": {
        "annual_fee": 599,
        "description": "Top-tier travel card with lounge access, travel credits, and comprehensive insurance",
        "available_provinces": ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"],
        "credit_terms": [6, 12, 24, 36],
        "min_credit_limit": 10000,
        "rewards_preference": "travel"
    },
    "Maple No-Fee Everyday Mastercard": {
        "annual_fee": 0,
        "description": "No-annual-fee card with 1% cash back on all purchases",
        "available_provinces": ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"],
        "credit_terms": [6, 12, 24, 36],
        "min_credit_limit": 500,
        "rewards_preference": "no fee"
    }
}


class RecommendationRequest(BaseModel):
    card: str
    intent: str  # e.g., "new card", "balance transfer", "credit limit increase"
    province: str
    credit_limit: float
    rewards_preference: str  # e.g., "cash back", "travel points", "no fee"


class RecommendationResponse(BaseModel):
    card: str
    intent: str
    province: str
    credit_limit: float
    rewards_preference: str
    annual_fee: float
    monthly_fee: float
    total_annual_cost: float
    description: str
    status: str
    message: Optional[str] = None


def calculate_monthly_fee(annual_fee: float, credit_limit: float, intent: str) -> float:
    """Calculate effective monthly cost based on intent type"""
    if intent.lower() == "balance transfer":
        # Balance transfer fee: 1% of credit limit + monthly portion of annual fee
        transfer_fee = credit_limit * 0.01
        monthly_fee = (annual_fee / 12) + (transfer_fee / 12)
    elif intent.lower() == "credit limit increase":
        # Credit limit increase: just monthly portion of annual fee
        monthly_fee = annual_fee / 12
    else:
        # New card: standard monthly portion of annual fee
        monthly_fee = annual_fee / 12

    return round(monthly_fee, 2)


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Credit Card Recommendation Tool API",
        "version": "1.0.0",
        "endpoints": {
            "recommendation": "/quotation_tool",
            "cards": "/models"
        }
    }


@app.get("/models")
async def get_models():
    """Get all available Canadian Bank credit cards"""
    return {
        "available_cards": list(CREDIT_CARDS.keys()),
        "cards_details": CREDIT_CARDS
    }


@app.post("/quotation_tool", response_model=RecommendationResponse)
async def quotation_tool(request: RecommendationRequest):
    """
    Generate a recommendation for a Canadian Bank credit card

    Parameters:
    - card: Canadian Bank card name (Maple Rewards Visa Infinite, Maple Cash Back Mastercard, Maple Travel Elite Visa, Maple No-Fee Everyday Mastercard)
    - intent: Application intent (new card, balance transfer, credit limit increase)
    - province: Canadian province code (ON, QC, BC, AB, etc.)
    - credit_limit: Requested credit limit in CAD
    - rewards_preference: Preferred rewards type (cash back, travel points, no fee)
    """

    # Validate card
    if request.card not in CREDIT_CARDS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid card. Available cards: {', '.join(CREDIT_CARDS.keys())}"
        )

    card_data = CREDIT_CARDS[request.card]

    # Validate province
    if request.province.upper() not in card_data["available_provinces"]:
        raise HTTPException(
            status_code=400,
            detail=f"Card not available in {request.province}. Available provinces: {', '.join(card_data['available_provinces'])}"
        )

    # Validate credit limit
    if request.credit_limit < card_data["min_credit_limit"]:
        raise HTTPException(
            status_code=400,
            detail=f"Credit limit must be at least ${card_data['min_credit_limit']} CAD for this card"
        )

    # Validate rewards preference
    valid_preferences = ["cash back", "travel points", "no fee"]
    if request.rewards_preference.lower() not in valid_preferences:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid rewards preference. Options: {', '.join(valid_preferences)}"
        )

    # Calculate monthly fee
    monthly_fee = calculate_monthly_fee(
        card_data["annual_fee"],
        request.credit_limit,
        request.intent
    )

    total_annual_cost = round(card_data["annual_fee"] + (
        request.credit_limit * 0.01 if request.intent.lower() == "balance transfer" else 0
    ), 2)

    return RecommendationResponse(
        card=request.card,
        intent=request.intent,
        province=request.province.upper(),
        credit_limit=request.credit_limit,
        rewards_preference=request.rewards_preference,
        annual_fee=card_data["annual_fee"],
        monthly_fee=monthly_fee,
        total_annual_cost=total_annual_cost,
        description=card_data["description"],
        status="success",
        message=f"Recommendation generated successfully for {request.card}"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Made with Bob