# Code Vault
----

### Python
**What it is:** A beginner-friendly programming language.

**Why you need it:**
- You write your first programs in Python
- It is easy to read and perfect for learning coding basics

### VS Code
**What it is:** A code editor (the app where you write and run code).

**Why you need it:**
- You write files like `hello.py`
- You use the built-in terminal to run your code
- You install extensions (like Python) for beginner support

### Flutter
**What it is:** A framework for building app user interfaces.

**Why you need it:**
- You will build the Caloria app screens
- It lets you run one codebase on Android (and more platforms)

### Android Studio
**What it is:** Android development software that includes the Android emulator.

**Why you need it:**
- The emulator acts like a virtual phone on your computer
- You test your Flutter app even if you do not have a physical Android phone

---

## Data Types in Dart

**One line definition:**
A data type tells Dart what KIND of value you are storing.

| Type   | Stores          | Example          |
|--------|-----------------|------------------|
| String | Text            | "Planet Caloria" |
| int    | Whole numbers   | 7                |
| double | Decimal numbers | 98.5             |
| bool   | True or False   | true             |

**Real world analogy:**
Like different shaped containers on your spaceship:
- String = a text document
- int = a whole number display
- double = a decimal gauge
- bool = an on/off switch

---

## Functions in Dart

**One line definition:**
A reusable set of instructions you write once and 
call by name whenever you need them.

**Real world analogy:**
A recipe card — write the steps once, follow it 
as many times as you need.

**Anatomy of a function:**
```dart
double calculateBMR(double weight, int age) {
//↑           ↑          ↑              ↑
//return    function   parameter      parameter
//type      name       1              2
  return weight * age; // simplified
}
```

---

## if / else in Dart

**One line definition:**
Makes a decision based on a condition — 
if something is true, do this, otherwise do that.

**Real world analogy:**
Like a spaceship navigation system:
"IF fuel > 50% → continue mission
 ELSE → return to base"

**In code:**
```dart
if (gender == "male") {
  return base + 5;   // male offset
} else {
  return base - 161; // female offset
}
```

**Watch out:**
- Use == for comparison, not =
- = means "store this value"
- == means "are these equal?"

## Maps in Dart

**One line definition:**
A Map stores data in labeled key-value pairs — like a 
mini spreadsheet row.

**Real world analogy:**
Think of a Map like a patient's medical form:
- "name": "Indrani"
- "age": 25
- "weight": 65.0
Each field has a label and a value.

**In code:**
```dart
Map<String, dynamic> food = {
  "name": "oatmeal",
  "calories": 150,
  "protein": 5.0
};

print(food["name"]);     // oatmeal
print(food["calories"]); // 150
```

**When to use Map vs List:**
- List → ordered collection of same type items
- Map  → labeled collection of different type values

## Lists in Dart

**One line definition:**
A List is an ordered collection of items stored 
in a single variable.

**Real world analogy:**
Think of a List like a checklist on your spaceship:
```
Shopping List:
1. oatmeal
2. chicken breast  
3. banana
```
Each item has a position (index) starting from 0.

**In code:**
```dart
List<String> foods = ["oatmeal", "chicken breast", "banana"];

// Access by position
print(foods[0]); // oatmeal
print(foods[1]); // chicken breast
print(foods[2]); // banana

// Add new item
foods.add("apple");

// How many items?
print(foods.length); // 4
```

**List of numbers:**
```dart
List<double> calories = [150, 165, 89];
```

**Empty list — add later:**
```dart
List<String> foodLog = []; // start empty
foodLog.add("oatmeal");    // add items later
```

**Watch Out — Index starts at 0!**
```
foods[0] = "oatmeal"       ← first item is 0 not 1
foods[1] = "chicken breast"
foods[2] = "banana"
foods[3] = ???             ← this would crash!
                              only 3 items exist
```

**List vs Map — when to use which:**
| When to use|     List           | Map                   |
|------------|--------------------|-----------------------|
| Use when   | Order matters      | Labels matter         |
| Example    | [150, 165, 89]     | {"calories": 150}     |
| Access by  | Position foods[0]  | Label food["calories"]|
| Real world | Numbered checklist | Labeled form          |
