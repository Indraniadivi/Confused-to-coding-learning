**Mission Briefing:**
Welcome to Star Station, Cadet. This is the most important 
stop on your journey. Every modern app — from Instagram to 
Spotify to your future calorie tracker — talks to the outside 
world through something called an API. Master this and you 
will unlock the true power of app development.

**Stellar Points:** ⭐ 400 XP  
**Estimated Time:** 40 minutes  
**Planet Status:** 🔴 Unexplored

## 🎯 Mission Objective

By the end of this mission you will:
- Understand what an API is in plain English
- Know what HTTP requests and JSON responses are
- Get your Spoonacular API key
- Make your first real API call and see live food data

## Mission content coming in next commit...

---

## The Concept: What is an API?

Imagine you are at a restaurant on Star Station.
You don't walk into the kitchen and cook your own food.
Instead you tell the **waiter** what you want, the waiter 
goes to the kitchen, and brings back your order.
```
YOU          WAITER        KITCHEN
(your app) → (API)      → (server/database)
           ← brings back ← food data
```

That waiter is the API.

- **You** = your Flutter app
- **Waiter** = Spoonacular API
- **Kitchen** = Spoonacular's food database
- **Your order** = "give me nutrition data for banana"
- **Your food** = JSON response with calories, protein, fat

---

## 🌐 What is an HTTP Request?

When your app talks to an API it sends an HTTP request.
Think of it like sending a letter to the kitchen:
```
GET https://api.spoonacular.com/food/ingredients/search?query=banana&apiKey=YOUR_KEY
━━━  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
↑    ↑                                                  ↑           ↑
Type Address of the server                              What you    Your
of   (like a website URL)                               want        membership
req.                                                                card
```

**Two types of requests:**
| Type | What it does.            | Like...           |
|------|--------------------------|-------------------|
| GET  | Ask for data.            | Asking a question |
| POST | Send data + get response | Filling a form    |

---

## 📦 What is JSON?

JSON is the format APIs use to send data back.
Think of it like a neatly organized form:
```json
{
  "name": "banana",
  "calories": 89,
  "protein": 1.1,
  "fat": 0.3,
  "carbs": 23.0
}
```

Instead of a paragraph saying "banana has 89 calories and 
1.1g protein", JSON organizes it with labels and values —
easy for both humans and computers to read.

---

## 🔑 Getting Your Spoonacular API Key

Before calling the API you need permission — an API key.
Think of it like a membership card for the restaurant.

**Step 1:** Go to spoonacular.com/food-api/console
**Step 2:** Click "Start for Free" and create account
**Step 3:** Go to "My Console" and copy your API key

**Step 4:** Test it in your terminal:
```
curl "https://api.spoonacular.com/food/ingredients/search?query=banana&apiKey=YOUR_KEY"
```

**If you see JSON data — your key works! ✅**
**If you see this — key is missing or wrong:**
```json
{
  "status": "failure",
  "code": 401,
  "message": "You are not authorized."
}
```

⚠️ Important Rules About API Keys:
- Never share your API key publicly
- Never commit it to GitHub
- Free tier = 150 requests/day

📡 See: Code Vault → APIs
📡 See: Code Vault → JSON
📡 See: Code Vault → HTTP Requests

---

## ⚔️ Your Mission Exercise

In this mission we make our first real API call in Dart!

First add the http package to your Flutter project:
```bash
cd calorie_tracker
flutter pub add http
```

Then open `calorie_tracker/lib/main.dart` and replace everything with this:
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  print("🚀 Calling Spoonacular API...");
  
  String apiKey = "YOUR_API_KEY_HERE";
  String food = "banana";
  
  String url = "https://api.spoonacular.com/food/ingredients"
      "/search?query=$food&apiKey=$apiKey";

  http.Response response = await http.get(Uri.parse(url));

  if (response.statusCode == 200) {
    Map<String, dynamic> data = jsonDecode(response.body);
    print("✅ API call successful!");
    print("Food found: ${data['results'][0]['name']}");
    print("Food ID: ${data['results'][0]['id']}");
  } else {
    print("❌ Houston, we have a problem!");
    print("Status code: ${response.statusCode}");
  }
}
```

Run it:
```
dart lib/main.dart
```

**Mission complete when you see:**
```
🚀 Calling Spoonacular API...
✅ API call successful!
Food found: banana
Food ID: 9040
```

---

## 🛸 Reading the Code — Line by Line
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;
```
→ "Bring in two toolboxes — one for converting JSON,
   one for making HTTP requests"
```dart
void main() async {
```
→ "async means this function will wait for things
   that take time — like waiting for API response"
```dart
http.Response response = await http.get(Uri.parse(url));
```
→ "Send a GET request to the URL and WAIT for 
   the response before continuing"
→ "await = pause here until the waiter comes back"
```dart
if (response.statusCode == 200) {
```
→ "200 means success in HTTP language
   Like getting a thumbs up from the kitchen"
```dart
Map<String, dynamic> data = jsonDecode(response.body);
```
→ "Convert the JSON text response into a Dart Map
   so we can access it with labels like data['results']"

---

## ☄️ Asteroid Warning

- Never hardcode your API key in real apps
  → Use environment variables instead
- Always check statusCode before using response
  → 200 = success, 401 = unauthorized, 404 = not found
- API calls need async/await — they take time
  → Without await your app won't wait for the response

Replace YOUR_API_KEY_HERE!
- When you see YOUR_API_KEY_HERE in any code sample,
  that is a placeholder — replace it with your actual 
- API key before running. If you see:
  `Connection failed: Operation not permitted`
- This is almost always why — the placeholder was 
  never replaced with a real key!

---

## 🐛 Debugging Tips

- `Could not find package http` 
  → Run flutter pub add http first
- `SocketException: Failed host lookup`
  → Check your internet connection
- `Null check operator on null value`
  → API returned empty results — check your query

---

## 🤖 Phone Mission Control

> "I am learning how to call APIs in Dart for the 
> first time. I am using the http package to make 
> a GET request to Spoonacular. I got this error: 
> [paste error]. Can you explain what it means 
> and give me a hint only?"

---

## 🏆 Mission Complete!

You have conquered Star Station! ⭐ +400 Stellar Points

You now know:
- What an API is and how it works
- What HTTP requests and JSON responses are
- How to make a real API call in Dart
- How to read and handle the response

📡 See: Code Vault → async/await
📡 See: Code Vault → HTTP Status Codes

**→ Ready for Mission 5? Head to the Red Nebula 🔴**
