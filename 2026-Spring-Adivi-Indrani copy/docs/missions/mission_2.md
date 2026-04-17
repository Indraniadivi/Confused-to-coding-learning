**Mission Briefing:**
Welcome back, Cadet. Your next destination is The Dark Moon — 
a place where nothing works unless you organize your code into 
reusable instructions called functions. The inhabitants here 
refuse to repeat themselves. You must learn to think the same way.

**Stellar Points:** ⭐ 200 XP  
**Estimated Time:** 30 minutes  
**Planet Status:** 🔴 Unexplored

## Mission Objective

By the end of this mission you will:
- Understand what a function is and why we need one
- Write your first Dart function
- Use if/else logic to make decisions in code
- Build the BMR calculator from calorie_logic.py in Dart

---

## The Concept: What is a Function?

Think of a function like a recipe card on your spaceship.
You write the steps ONCE on the card. Every time you need 
that recipe, you just call its name — you don't rewrite 
the steps every time.

Without functions:
```dart
// Without a function — repeated code everywhere ❌
double weight = 65.0;
double height = 165.0;
int age = 25;
double bmr1 = (10 * weight) + (6.25 * height) - (5 * age) - 161;

double weight2 = 80.0;
double height2 = 178.0;
int age2 = 30;
double bmr2 = (10 * weight2) + (6.25 * height2) - (5 * age2) + 5;
```

With functions:
```dart
// With a function — write once, use many times
double calculateBMR(double weight, double height, int age, String gender) {
  double base = (10 * weight) + (6.25 * height) - (5 * age);
  if (gender == "male") {
    return base + 5;
  } else {
    return base - 161;
  }
}

// Now call it as many times as you need!
double bmr1 = calculateBMR(65, 165, 25, "female");
double bmr2 = calculateBMR(80, 178, 30, "male");
```

## Key Parts of a Function

| Part             | What it means                    | Example             |
|------------------|----------------------------------|---------------------|
| Return type      | What kind of value it gives back | double              |
| Function name    | What you call it                 | calculateBMR        | 
| Parameters       | Information it needs to work     | weight, height, age |
| Return statement | The answer it gives back         | return base + 5     |

## Asteroid Warning — Common Mistakes

- Return type must match what you actually return
- Every parameter needs a type: double weight not just weight
- if/else must use "==" not "=" for comparison
- Don't forget curly braces {} around function body

---

## Your Mission Exercise

Open `calorie_tracker/lib/main.dart` and replace everything with this:
```dart
void main() {
  // Test your BMR calculator
  double bmr1 = calculateBMR(65, 165, 25, "female");
  double bmr2 = calculateBMR(80, 178, 30, "male");

  print("Female BMR: $bmr1 calories/day");
  print("Male BMR: $bmr2 calories/day");
}

double calculateBMR(double weight, double height, int age, String gender) {
  double base = (10 * weight) + (6.25 * height) - (5 * age);
  
  if (gender == "male") {
    return base + 5;
  } else {
    return base - 161;
  }
}
```

Then run it:
```
dart lib/main.dart
```

**Mission complete when you see:** 
```
Female BMR: 1395.25 calories/day
Male BMR: 1767.5 calories/day
```

📡 [Deep dive → Code Vault: Functions in Dart]
📡 [Deep dive → Code Vault: if/else in Dart]

---

## Debugging Tips

- `A non-null value must be returned` → Your function is 
  missing a return statement
- `Too many positional arguments` → You passed too many 
  values when calling the function
- `The argument type int can't be assigned to double` → 
  Pass 65.0 instead of 65

---

## 🤖 Phone Mission Control

Stuck? Copy this into ChatGPT:

> "I am learning Dart functions for the first time. 
> I wrote this function: [paste your code]. 
> I am getting this error: [paste error].
> Can you explain what the error means and give me 
> a hint — without solving it for me?"

---

Asteroid Warning — Always verify your math!
When building calculation functions, manually verify 
the result with a calculator before assuming your 
code is wrong. Sometimes the expected output is 
what needs fixing, not the code!

## Mission Complete!

You have conquered The Dark Moon! ⭐ +200 Stellar Points

You now know:
- What a function is and why we use it
- How to write a Dart function with parameters
- How to use if/else logic
- You built a real BMR calculator in Dart!



**→ Ready for Mission 3? Head to the Asteroid Belt**
