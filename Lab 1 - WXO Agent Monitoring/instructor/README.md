# Credit Card Recommendation Tool API

A FastAPI application that provides credit card recommendation services for Canadian Bank products.

## Features

- **Recommendation Tool Endpoint**: Generate recommendations for Canadian Bank credit cards based on card type, intent, province, credit limit, and rewards preference
- **Card Information**: Retrieve details about available Canadian Bank credit cards
- **Input Validation**: Comprehensive validation for all input parameters
- **Monthly Fee Calculation**: Automatic calculation based on intent and credit limit

## Available Canadian Bank Credit Cards

1. **Maple Rewards Visa Infinite** - Premium travel rewards card with accelerated points on groceries, gas, and travel (Annual Fee: $120 CAD)
2. **Maple Cash Back Mastercard** - Versatile cash back card with up to 4% cash back on groceries and recurring bills (Annual Fee: $99 CAD)
3. **Maple Travel Elite Visa** - Top-tier travel card with lounge access, travel credits, and comprehensive insurance (Annual Fee: $599 CAD)
4. **Maple No-Fee Everyday Mastercard** - No-annual-fee card with 1% cash back on all purchases (Annual Fee: $0 CAD)

## Installation

### Option 1: Local Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Option 2: Docker Installation

#### Using Docker

1. Build the Docker image:
```bash
docker build -t credit-card-recommendation-api .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --name credit-card-recommendation-tool credit-card-recommendation-api
```

3. Check container status:
```bash
docker ps
```

4. View logs:
```bash
docker logs credit-card-recommendation-tool
```

5. Stop the container:
```bash
docker stop credit-card-recommendation-tool
```

6. Remove the container:
```bash
docker rm credit-card-recommendation-tool
```

#### Using Docker Compose (Recommended)

1. Start the service:
```bash
docker-compose up -d
```

2. Check status:
```bash
docker-compose ps
```

3. View logs:
```bash
docker-compose logs -f
```

4. Stop the service:
```bash
docker-compose down
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns API information and available endpoints.

### 2. Get Cards
```
GET /models
```
Returns all available Canadian Bank credit cards with their details.

**Response Example:**
```json
{
  "available_cards": ["Maple Rewards Visa Infinite", "Maple Cash Back Mastercard", "Maple Travel Elite Visa", "Maple No-Fee Everyday Mastercard"],
  "cards_details": {
    "Maple Rewards Visa Infinite": {
      "annual_fee": 120,
      "description": "Premium travel rewards card with accelerated points on groceries, gas, and travel",
      "available_provinces": ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"],
      "credit_terms": [6, 12, 24, 36],
      "min_credit_limit": 5000,
      "rewards_preference": "travel"
    }
  }
}
```

### 3. Recommendation Tool (Main Endpoint)
```
POST /quotation_tool
```

**Request Body:**
```json
{
  "card": "Maple Rewards Visa Infinite",
  "intent": "new card",
  "province": "ON",
  "credit_limit": 10000,
  "rewards_preference": "travel points"
}
```

**Parameters:**
- `card` (string, required): Canadian Bank credit card name
  - Options: "Maple Rewards Visa Infinite", "Maple Cash Back Mastercard", "Maple Travel Elite Visa", "Maple No-Fee Everyday Mastercard"
- `intent` (string, required): Application intent
  - Options: "new card", "balance transfer", "credit limit increase"
- `province` (string, required): Canadian province code
  - Options: "ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "PE", "NL"
- `credit_limit` (float, required): Requested credit limit in CAD
  - Must be >= minimum credit limit for the selected card
- `rewards_preference` (string, required): Preferred rewards type
  - Options: "cash back", "travel points", "no fee"

**Response Example:**
```json
{
  "card": "Maple Rewards Visa Infinite",
  "intent": "new card",
  "province": "ON",
  "credit_limit": 10000,
  "rewards_preference": "travel points",
  "annual_fee": 120,
  "monthly_fee": 10.00,
  "total_annual_cost": 120.00,
  "description": "Premium travel rewards card with accelerated points on groceries, gas, and travel",
  "status": "success",
  "message": "Recommendation generated successfully for Maple Rewards Visa Infinite"
}
```

## Usage Examples

### Using cURL

```bash
# Get all cards
curl http://localhost:8000/models

# Generate a recommendation
curl -X POST http://localhost:8000/quotation_tool \
  -H "Content-Type: application/json" \
  -d '{
    "card": "Maple Cash Back Mastercard",
    "intent": "new card",
    "province": "ON",
    "credit_limit": 5000,
    "rewards_preference": "cash back"
  }'
```

### Using Python requests

```python
import requests

# Get cards
response = requests.get("http://localhost:8000/models")
print(response.json())

# Generate recommendation
recommendation_data = {
    "card": "Maple Travel Elite Visa",
    "intent": "balance transfer",
    "province": "BC",
    "credit_limit": 15000,
    "rewards_preference": "travel points"
}

response = requests.post(
    "http://localhost:8000/quotation_tool",
    json=recommendation_data
)
print(response.json())
```

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Validation Rules

1. **Card**: Must be one of the four available Canadian Bank credit cards
2. **Province**: Must be a valid Canadian province code where the card is available
3. **Credit Limit**: Must be >= minimum credit limit for the selected card
4. **Rewards Preference**: Must be one of "cash back", "travel points", or "no fee"

## Fee Calculation

The API calculates monthly fees based on the intent:

- **New Card**: Annual fee divided by 12
- **Balance Transfer**: Annual fee divided by 12 plus 1% of credit limit divided by 12
- **Credit Limit Increase**: Annual fee divided by 12

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: Invalid input parameters
- `422 Unprocessable Entity`: Invalid request format

Example error response:
```json
{
  "detail": "Invalid card. Available cards: Maple Rewards Visa Infinite, Maple Cash Back Mastercard, Maple Travel Elite Visa, Maple No-Fee Everyday Mastercard"
}
```

## Uploading to watsonx Orchestrate

The API includes an OpenAPI specification file (`product_tool.json`) that can be uploaded to watsonx Orchestrate as a tool.

### Steps to Upload:

1. **Ensure the API is accessible**: Make sure your FastAPI server is running and accessible from watsonx Orchestrate. If running locally, you may need to use a tunneling service like ngrok or deploy to a public server.

2. **Update the server URL in product_tool.json**:
   - Open `product_tool.json`
   - Update the `servers[0].url` field to your actual server URL
   - Example: `"url": "https://your-server.com"` or `"url": "https://your-ngrok-url.ngrok.io"`

3. **Upload to watsonx Orchestrate**:
   - Log in to watsonx Orchestrate
   - Navigate to the Tools section
   - Click "Add Tool" or "Import Tool"
   - Select "OpenAPI" as the tool type
   - Upload the `product_tool.json` file
   - Configure authentication if required
   - Save and deploy the tool

4. **Use in Agents**:
   - Once uploaded, the recommendation endpoint will be available as a tool
   - You can add it to your agents to enable credit card recommendation capabilities
   - The tool will accept the required parameters (card, intent, province, credit_limit, rewards_preference)
   - It will return complete recommendation details including monthly fee and total annual cost

### Example Usage in watsonx Orchestrate:

Once configured, you can ask your agent questions like:
- "Generate a recommendation for a Maple Rewards Visa Infinite new card application in Ontario with a $10,000 credit limit and travel points preference"
- "What would be the monthly fee for a Maple Travel Elite Visa balance transfer in BC with a $15,000 credit limit?"
- "Show me all available Canadian Bank credit cards"

## License

This is a demonstration API for educational purposes.
