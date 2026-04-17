**Mission Briefing:**
Cadet, you have entered the Asteroid Belt — a chaotic region 
where data flies around in collections. To navigate safely, 
you must learn to store multiple items in a List and process 
them one by one using Loops. The inhabitants of Planet Caloria 
need to track everything they eat — and that means handling 
lists of food items.

**Stellar Points:** ⭐ 300 XP  
**Estimated Time:** 30 minutes  
**Planet Status:** 🔴 Unexplored

## 🎯 Mission Objective

By the end of this mission you will:
- Understand what a List is and why we need it
- Loop through a List using 'for' loops
- Build a basic food log that tracks meals
- Calculate total calories from a list of food items

---

## 🧠 The Concept: What is a List?

Think of a List like a shopping checklist on your spaceship.
Instead of creating a separate variable for every item,
you store them all in one organized collection.

Without a List — messy:
```dart
String food1 = "oatmeal";
String food2 = "chicken breast";
String food3 = "banana";
// What if you have 50 food items? 50 variables! ❌
```

With a List — clean:
```dart
List<String> foods = ["oatmeal", "chicken breast", "banana"];
// All items in one place ✅
```

## 🔄 What is a Loop?

A loop repeats the same action for every item in a List.
Think of it like a spaceship scanner — it checks every 
asteroid one by one automatically.
```dart
List<String> foods = ["oatmeal", "chicken breast", "banana"];

for (String food in foods) {
  print("Scanning: $food");
}
```

This prints:
```
Scanning: oatmeal
Scanning: chicken breast
Scanning: banana
```

## 🔑 Key Concepts

| Concept      | What it means                   | Example               |
|--------------|---------------------------------|-----------------------|
| List         | A collection of items           | ["oatmeal", "banana"] |
| List<String> | A list that only holds text.    | List<String> foods    |
| List<double> | A list that only holds decimals | List<double> calories |
| for loop     | Repeat for every item           | for (item in list)    |

## ☄️ Asteroid Warning — Common Mistakes

- List index starts at 0 not 1
  - foods[0] = "oatmeal" ✅
  - foods[1] = "chicken breast" ✅
- List type must match contents
  - List<String> cannot hold numbers
- Don't forget <> around the type name

📡 See: Code Vault → Lists in Dart
📡 See: Code Vault → Loops in Dart

---

## ⚔️ Your Mission Exercise

Open `calorie_tracker/lib/main.dart` and replace everything with this:
```dart
void main() {
  // Build your food log
  List<Map<String, dynamic>> foodLog = [];

  // Add food entries
  foodLog.add({"name": "oatmeal", "calories": 150, "protein": 5.0});
  foodLog.add({"name": "chicken breast", "calories": 165, "protein": 31.0});
  foodLog.add({"name": "banana", "calories": 89, "protein": 1.1});

  // Calculate totals
  double totalCalories = 0;
  double totalProtein = 0;

  for (Map<String, dynamic> entry in foodLog) {
    totalCalories += entry["calories"];
    totalProtein += entry["protein"];
    print("✅ Logged: ${entry["name"]} — ${entry["calories"]} cal");
  }

  print("━━━━━━━━━━━━━━━━━━━━━━━━");
  print("Total Calories: $totalCalories");
  print("Total Protein: ${totalProtein}g");
}
```

Run it:
```
dart lib/main.dart
```

**Mission complete when you see:**
```
✅ Logged: oatmeal — 150 cal
✅ Logged: chicken breast — 165 cal
✅ Logged: banana — 89 cal
━━━━━━━━━━━━━━━━━━━━━━━━
Total Calories: 404.0
Total Protein: 37.1g
```

---

## 🛸 Reading the Code — Line by Line
```dart
List<Map<String, dynamic>> foodLog = [];
```
→ "Create an empty list that holds food entries.
   Each entry is a Map — like a mini dictionary
   with labels and values"
```dart
foodLog.add({"name": "oatmeal", "calories": 150});
```
→ "Add a food entry to the log — like writing 
   a new row in a food diary"
```dart
for (Map<String, dynamic> entry in foodLog)
```
→ "Go through every food entry in the log 
   one by one"
```dart
totalCalories += entry["calories"];
```
→ "Add this entry's calories to the running total.
   += means add to existing value"

---

## 🐛 Debugging Tips

- `The argument type int can't be assigned to double`
  → Use 150.0 instead of 150 for calorie values
- `Null check operator used on a null value`
  → The key name doesn't match — check spelling exactly
- `type List is not a subtype of type Map`
  → You're accessing the list instead of an entry

---

## 🤖 Phone Mission Control

> "I am learning Dart Lists and loops for the first time.
> I am trying to build a food log using a List of Maps.
> I got this error: [paste error].
> Can you explain what it means and give me a hint only?"

---

## 🏆 Mission Complete!

You have navigated the Asteroid Belt! ⭐ +300 Stellar Points

You now know:
- What a List is and how to use it
- How to loop through items with a for loop
- How to use Maps to store labeled data
- You built a real food log in Dart!

📡 See: Code Vault → Lists in Dart
📡 See: Code Vault → Maps in Dart

**→ Ready for Mission 4? Head to Star Station 🌟**