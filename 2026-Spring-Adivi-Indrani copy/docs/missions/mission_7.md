**Mission Briefing:**
Cadet, you have reached Planet Caloria. The inhabitants 
are waiting. Their calorie tracking system has crashed 
and you are their only hope. Everything you have learned 
across 6 missions has prepared you for this moment.
It is time to put it all together and save the planet.

**Stellar Points:** ⭐ 1000 XP  
**Estimated Time:** 60 minutes  
**Planet Status:** 🔴 In Crisis

## 🎯 Mission Objective

By the end of this mission you will:
- Add food search using Spoonacular API to your app
- Log food items and track daily calories
- See remaining calories update in real time
- Have a complete working calorie tracker app

---

## 🧠 The Concept: Putting It All Together

You have learned 6 powerful skills on your journey:

| Mission | Skill | Used in final app |
|---|---|---|
| Mission 1 | Variables | Store user profile data |
| Mission 2 | Functions | BMR and calorie calculations |
| Mission 3 | Lists and Maps | Food log entries |
| Mission 4 | APIs | Spoonacular food search |
| Mission 5 | Flutter UI | App screens and widgets |
| Mission 6 | State management | Update UI with user input |

Now we combine ALL of them into one complete app
with two screens:
```
Screen 1: Profile Screen (Mission 6)
→ User enters weight, height, age, gender, goal
→ Calculates daily calorie and macro targets
→ Button navigates to Screen 2

Screen 2: Food Log Screen (NEW)
→ Search food using Spoonacular API
→ Add food items to daily log
→ See remaining calories update in real time
→ Track protein, fat and carbs
```

## 🔑 New Concept: Navigation Between Screens
```dart
// Navigate to a new screen
Navigator.push(
  context,
  MaterialPageRoute(
    builder: (context) => FoodLogScreen(
      dailyTargets: results,
    ),
  ),
);

// Go back to previous screen
Navigator.pop(context);
```

Think of navigation like moving between rooms 
on your spaceship:
- `Navigator.push` = open a new room
- `Navigator.pop` = go back to previous room
- You can pass data between rooms like passing 
  a note through the door

📡 See: Code Vault → Navigation
📡 See: Code Vault → Navigator

## ⚔️ Your Mission Exercise

You have already built this! Here is what your complete 
app does:

**Screen 1 — Cadet Profile:**
- Enter weight, height, age, gender and goal
- App calculates your daily calorie and macro targets
- Press Calculate to see your targets
- Press the button to navigate to Food Log

**Screen 2 — Planet Caloria Food Log:**
- See your remaining calories for the day
- Search any food using Spoonacular API
- Enter serving size in grams
- See full nutrition breakdown per food item
- Watch remaining calories update in real time

The complete code for this mission is in two files
in your project:

- `calorie_tracker/lib/main.dart` 
- `calorie_tracker/lib/food_log_screen.dart`

Rather than copying the full code at once, build it
incrementally by following these steps:

## Step 1 — Create food_log_screen.dart
Start with just the basic structure and state variables.
Reference: Mission 5 (StatefulWidget structure)

## Step 2 — Add the search function  
Add searchFood() using what you learned in Mission 4.
Reference: Mission 4 (API calls with http package)

## Step 3 — Add the UI
Add the search box, results list and food log display.
Reference: Mission 5 (Flutter widgets)

## Step 4 — Connect both screens
Add navigation from ProfileScreen to FoodLogScreen.
Reference: Navigator.push concept above

## Step 5 — Add serving size dialog
Ask user how much they ate before logging.
