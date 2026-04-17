# Research: Comparative Analysis of Nutrition APIs for Food Data Integration

**Issue:** #11  
**Branch:** issue-11-nutrition-api-research

## Objective
Evaluate and compare two widely used nutrition APIs — Spoonacular and Nutritionix 
to determine which is most appropriate for integration into the calorie tracking 
app that learners build through the "From Confused to Coding platform". The evaluation prioritizes 
teachability and beginner-friendliness alongside technical capability, since 
learners will be following along with the integration step by step.

## APIs Evaluated

### 1. Spoonacular API
**Overview:**
Spoonacular is a food and recipe API that also provides detailed nutritional data. 
It supports ingredient search, recipe analysis, and meal planning endpoints. 
Originally built for recipe apps, it has grown into a comprehensive food data 
platform.

**Access:**
- Free tier available (150 requests/day)
- API key required — single key passed as query parameter
- Paid plans start at $29/month for higher limits
**Authentication Example:**
```
GET "https://api.spoonacular.com/food/ingredients/search?query=banana&apiKey=YOUR_KEY"
```
**Pros:**
- Single API key, simple to set up
- Excellent documentation with interactive playground
- Returns nutrients in a clean, labeled JSON structure
- Good beginner resources and community examples

**Cons:**
- Free tier limited to 150 requests/day — easy to hit in development
- Points-based quota system is confusing
- Recipe-focused design means some food database endpoints feel secondary

**Teachability Score: 7/10**
The single API key and clear documentation make setup approachable. The 
points-based quota system is confusing but can be ignored at the learning stage.

### 2. Nutritionix API
**Overview:**
Nutritionix is a nutrition-focused API built specifically for food logging and 
calorie tracking applications. It powers several major diet apps. Unlike 
Spoonacular, its core purpose is nutrition data — not recipes — which aligns 
more directly with a calorie tracker use case.

**Access:**
- Free tier available (500 requests/day on Natural Language endpoint)
- Requires both an App ID and API Key (two credentials)
- Academic/developer access available at no cost with registration

**Authentication Example:**
```
POST https://trackapi.nutritionix.com/v2/natural/nutrients
Headers:
  x-app-id: YOUR_APP_ID
  x-app-key: YOUR_APP_KEY
  Content-Type: application/json

Body:
  { "query": "1 cup of oatmeal and 2 eggs" }
```
**Pros:**
- Purpose-built for calorie tracking — endpoints map directly to the use case
- Natural language endpoint handles input like "a bowl of pasta"
- Higher free tier limit (500/day) than Spoonacular
- Branded food database is comprehensive

**Cons:**
- Dual credential system (App ID + API Key) passed as headers
- POST-based primary endpoint is harder to test in a browser
- Documentation is less polished than Spoonacular
- Some response fields inconsistently populated for less common foods

**Teachability Score: 6/10**
The natural language endpoint is exciting and motivating, but the dual-header 
auth and POST-only primary endpoint add friction for absolute beginners who 
haven't written a POST request yet.
## Comparison Summary
## Side-by-Side Comparison

| Criteria                | Spoonacular | Nutritionix |
|-------------------------|------------------------------|-----------------------------------|
| Authentication          | Single API key (query param) | App ID + API Key (headers)        |
| Free Tier               | 150 requests/day             | 500 requests/day                  |
| Primary Use Case        | Recipes + nutrition          | Calorie tracking / food logging   |
| Natural Language Input  | Yes (POST endpoint)          | Yes (POST endpoint — core feature)|
| Branded Foods           | Limited                      | Extensive                         |
| Response Format         | Labeled nutrient array       | Flat nutrition fields             |
| Documentation Quality   | Excellent                    | Good                              |
| Beginner Setup Friction | Low                          | Medium                            |
| Teachability Score      | 7/10                         | 6/10                              |

## Trade-off Analysis

**Where Spoonacular wins:**
Simpler authentication means learners can make their first API call directly 
in a browser URL bar, a powerful early win. The labeled nutrient array format 
(name + amount + unit) is easier to explain than Nutritionix's flat field names 
like nf_total_carbohydrate.

**Where Nutritionix wins:**
The natural language POST endpoint is a better match for a real food logging app users type "I had a bowl of oatmeal and a banana" and get structured data back. 
The higher free tier limit (500 vs 150) also reduces the risk of hitting quota 
during a coding session.

**The key tension:**
Spoonacular is easier to start with, but Nutritionix is closer to what a real 
calorie tracker would use. This is a genuine trade-off between onboarding 
simplicity and use-case authenticity.

## Recommendation

**Selected API: Spoonacular — for initial integration in From Confused to Coding**

For the purposes of the learning platform, Spoonacular's lower setup friction 
is the deciding factor. Learners on Mission 1 should be able to paste a URL 
into their browser and see real nutrition data immediately — without setting up 
headers, writing a POST request, or managing two credentials. This immediate 
feedback loop is essential for keeping beginners motivated.

Nutritionix will be introduced in a later mission as a comparison exercise, 
specifically to teach:
- The difference between GET and POST requests
- Header-based vs query-parameter authentication
- How to evaluate APIs for a specific use case

**Integration Plan for CodeQuest Missions:**
- Mission 4: Explain what an API is, show Spoonacular GET request in browser
- Mission 5: Call Spoonacular in Python, parse JSON response
- Mission 6: Connect API data to calorie_logic.py calculations
- Mission 7: Full calorie tracker with live food data from Spoonacular
- Mission 6 (advanced): Compare with Nutritionix POST request

## References

- Spoonacular API Documentation: https://spoonacular.com/food-api/docs
- Nutritionix API : https://nutritionix.com/
- Spoonacular Pricing: https://spoonacular.com/food-api/pricing

