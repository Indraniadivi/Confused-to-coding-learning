**Mission Briefing:**
Cadet, you have reached the Gas Giant — the most 
challenging planet in your journey. Here you will 
combine everything you have learned. Your BMR calculator, 
your food log, your API call, and your Flutter UI will 
all connect into one working app. Planet Caloria is 
almost saved!

**Stellar Points:** ⭐ 600 XP  
**Estimated Time:** 60 minutes  
**Planet Status:** 🔴 Unexplored

## 🎯 Mission Objective

By the end of this mission you will:
- Add user input fields to collect profile data
- Calculate BMR and calorie targets from user input
- Search food using Spoonacular API from the app
- Display results on screen — not just in terminal

---

## 🧠 The Concept: State and User Input

Until now your widgets were StatelessWidget — they 
never changed. But a real app changes based on what 
the user does. When a user types their weight, the 
app needs to remember it. This is called STATE.

Think of State like the fuel gauge on your spaceship:
- It starts at 0
- It changes as you add fuel
- The screen updates automatically to show the new value

**StatelessWidget vs StatefulWidget:**
```dart
// StatelessWidget — never changes
// Like a printed poster on your spaceship wall
class WelcomeScreen extends StatelessWidget { }

// StatefulWidget — changes based on user input  
// Like a live dashboard that updates in real time
class ProfileScreen extends StatefulWidget { }
```

## 🔑 How StatefulWidget works
```dart
class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  // Variables that can change go here
  double weight = 0;
  String gender = "female";
  String goal = "maintain";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // your UI here
    );
  }
}
```

## 🔑 Getting Text Input from User
```dart
// Create a controller to read what user typed
TextEditingController weightController = TextEditingController();

// Use it in a TextField
TextField(
  controller: weightController,
  decoration: InputDecoration(
    labelText: 'Weight (kg)',
  ),
  keyboardType: TextInputType.number,
)

// Read the value when button is pressed
double weight = double.parse(weightController.text);
```

## ☄️ Asteroid Warning

- Always use StatefulWidget when screen needs to update
- TextEditingController must be disposed when done
- double.parse() will crash if user types letters
  → Always validate input before parsing
- setState() must be called to update the screen
  → Without it the UI won't refresh

📡 See: Code Vault → StatefulWidget
📡 See: Code Vault → setState

---

## ⚔️ Your Mission Exercise

Open `calorie_tracker/lib/main.dart` and replace everything with this:
```dart
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

void main() {
  runApp(const CaloriaApp());
}

class CaloriaApp extends StatelessWidget {
  const CaloriaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mission to Planet Caloria',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.deepPurple,
        ),
      ),
      home: const ProfileScreen(),
    );
  }
}

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  // Controllers for text input
  final TextEditingController weightController = TextEditingController();
  final TextEditingController heightController = TextEditingController();
  final TextEditingController ageController = TextEditingController();

  // State variables
  String gender = "female";
  String goal = "maintain";
  String fitnessGoal = "general";
  Map<String, dynamic>? results;

  // BMR Calculation
  double calculateBMR(double weight, double height, int age, String gender) {
    double base = (10 * weight) + (6.25 * height) - (5 * age);
    return gender == "male" ? base + 5 : base - 161;
  }

  // Daily calories based on goal
  double calculateDailyCalories(double bmr, String goal) {
    Map<String, double> multipliers = {
      "lose": 0.85,
      "gain": 1.15,
      "maintain": 1.0,
    };
    return bmr * (multipliers[goal] ?? 1.0);
  }

  // Macro calculation
  Map<String, double> calculateMacros(double weight, double calories, String fitnessGoal) {
    double protein = fitnessGoal == "build_muscle" ? weight * 2 : weight * 0.8;
    double fat = weight * 0.8;
    double carbs = (calories - (protein * 4) - (fat * 9)) / 4;
    return {
      "protein": protein,
      "fat": fat,
      "carbs": carbs.clamp(0, double.infinity),
    };
  }

  // Calculate and show results
  void calculateTargets() {
    double weight = double.tryParse(weightController.text) ?? 0;
    double height = double.tryParse(heightController.text) ?? 0;
    int age = int.tryParse(ageController.text) ?? 0;

    if (weight == 0 || height == 0 || age == 0) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('⚠️ Please fill in all fields!')),
      );
      return;
    }

    double bmr = calculateBMR(weight, height, age, gender);
    double dailyCalories = calculateDailyCalories(bmr, goal);
    Map<String, double> macros = calculateMacros(weight, dailyCalories, fitnessGoal);

    setState(() {
      results = {
        "calories": dailyCalories.round(),
        "protein": macros["protein"]!.round(),
        "fat": macros["fat"]!.round(),
        "carbs": macros["carbs"]!.round(),
      };
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('🚀 Mission to Planet Caloria'),
        backgroundColor: Colors.deepPurple,
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              '👨‍🚀 Cadet Profile',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 24),
            TextField(
              controller: weightController,
              decoration: const InputDecoration(
                labelText: 'Weight (kg)',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.monitor_weight),
              ),
              keyboardType: TextInputType.number,
            ),
            const SizedBox(height: 16),
            TextField(
              controller: heightController,
              decoration: const InputDecoration(
                labelText: 'Height (cm)',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.height),
              ),
              keyboardType: TextInputType.number,
            ),
            const SizedBox(height: 16),
            TextField(
              controller: ageController,
              decoration: const InputDecoration(
                labelText: 'Age',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.cake),
              ),
              keyboardType: TextInputType.number,
            ),
            const SizedBox(height: 16),
            // Gender selector
            const Text('Gender:', style: TextStyle(fontSize: 16)),
            Row(
              children: [
                Radio(
                  value: "female",
                  groupValue: gender,
                  onChanged: (value) => setState(() => gender = value!),
                ),
                const Text('Female'),
                Radio(
                  value: "male",
                  groupValue: gender,
                  onChanged: (value) => setState(() => gender = value!),
                ),
                const Text('Male'),
              ],
            ),
            const SizedBox(height: 16),
            // Goal selector
            const Text('Goal:', style: TextStyle(fontSize: 16)),
            DropdownButton<String>(
              value: goal,
              isExpanded: true,
              items: const [
                DropdownMenuItem(value: "lose", child: Text("Lose Weight")),
                DropdownMenuItem(value: "maintain", child: Text("Maintain")),
                DropdownMenuItem(value: "gain", child: Text("Gain Weight")),
              ],
              onChanged: (value) => setState(() => goal = value!),
            ),
            const SizedBox(height: 16),
            // Fitness goal selector
            const Text('Fitness Goal:', style: TextStyle(fontSize: 16)),
            DropdownButton<String>(
              value: fitnessGoal,
              isExpanded: true,
              items: const [
                DropdownMenuItem(value: "general", child: Text("General Health")),
                DropdownMenuItem(value: "build_muscle", child: Text("Build Muscle")),
              ],
              onChanged: (value) => setState(() => fitnessGoal = value!),
            ),
            const SizedBox(height: 24),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: calculateTargets,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.deepPurple,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                child: const Text(
                  '🌍 Calculate My Targets',
                  style: TextStyle(fontSize: 18),
                ),
              ),
            ),
            // Results section
            if (results != null) ...[
              const SizedBox(height: 32),
              const Divider(),
              const SizedBox(height: 16),
              const Text(
                '🎯 Your Daily Targets',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              _buildResultCard('🔥 Calories', '${results!['calories']} kcal', Colors.orange),
              _buildResultCard('💪 Protein', '${results!['protein']}g', Colors.blue),
              _buildResultCard('🥑 Fat', '${results!['fat']}g', Colors.green),
              _buildResultCard('🍞 Carbs', '${results!['carbs']}g', Colors.amber),
            ],
          ],
        ),
      ),
    );
  }

  Widget _buildResultCard(String label, String value, Color color) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: color.withOpacity(0.3)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label, style: const TextStyle(fontSize: 16)),
          Text(
            value,
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: color,
            ),
          ),
        ],
      ),
    );
  }
}
```

Run it on the emulator:
```bash
flutter run
```

**Mission complete when you can:**
- ✅ Enter your weight, height and age
- ✅ Select gender and goal
- ✅ Press Calculate and see your daily targets

---

## 🛸 Reading the Code — Key Parts
```dart
final TextEditingController weightController = TextEditingController();
```
→ "Create a controller that reads what user types 
   in the weight field"
```dart
setState(() {
  results = { "calories": dailyCalories.round() ... };
});
```
→ "Update the results AND tell Flutter to 
   redraw the screen with new values"
```dart
if (results != null) ...[
```
→ "Only show results section IF calculate 
   button has been pressed"
```dart
double weight = double.tryParse(weightController.text) ?? 0;
```
→ "Try to convert text to number — if it fails 
   use 0 instead of crashing"

---

## 🐛 Debugging Tips

- Screen not updating → forgot setState()
- App crashes on Calculate → user left a field empty
  → fixed by tryParse with ?? 0
- Dropdown not showing → missing isExpanded: true
- Results not showing → check if results != null

---

## 🤖 Phone Mission Control

> "I am learning Flutter StatefulWidget for the first 
> time. I am trying to build a profile input screen 
> that calculates BMR. I got this error: [paste error].
> Can you explain what it means and give me a hint only?"

---

## 🏆 Mission Complete!

You have conquered the Gas Giant! ⭐ +600 Stellar Points

You now know:
- How StatefulWidget works
- How to collect user input with TextField
- How to update UI with setState
- Your app calculates real nutrition targets!

📡 See: Code Vault → StatefulWidget
📡 See: Code Vault → setState

**→ One last mission! Head to Planet Caloria 🌍**
