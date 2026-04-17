**Mission Briefing:**
Welcome to the Red Nebula, Cadet. Until now everything 
you built ran in the terminal. Today that changes. You 
will build your first real screen — something you can 
see, touch, and show to others. This is where your 
calorie tracker starts to look like a real app.

**Stellar Points:** ⭐ 500 XP  
**Estimated Time:** 45 minutes  
**Planet Status:** 🔴 Unexplored

## 🎯 Mission Objective

By the end of this mission you will:
- Understand what a Widget is in Flutter
- Build your first screen with text and a button
- Run the app on the emulator and see it live
- Create the profile input screen for the calorie tracker

## Mission content coming in next commit...

---

## 🧠 The Concept: What is a Widget?

In Flutter, everything you see on screen is a Widget.
Text? Widget. Button? Widget. Image? Widget. 
Even the entire screen is a Widget.

Think of Widgets like LEGO blocks on your spaceship:
- Each block does one specific thing
- You combine blocks to build something bigger
- You can reuse the same block in different places
```
Screen (Scaffold)
├── Top bar (AppBar)
│   └── Title text (Text)
└── Body (Center)
    └── Column
        ├── Text "Welcome Cadet"
        ├── TextField (name input)
        └── Button (ElevatedButton)
```

## 🔑 The Most Important Widgets

| Widget         | What it does             | Like...        |
|----------------|--------------------------|----------------|
| Scaffold       | The full screen container| A blank page.  |
| AppBar         | The top bar with title   | Page header.   |
| Text           | Displays text            | A label        |
| TextField      | Input box for typing.    | A form field   |
| ElevatedButton | A clickable button       | A submit button|
| Column         | Stacks widgets vertically| A vertical list|
| Center         | Centers its child        | Align center   |
| Padding        | Adds space around widget | Margin in CSS  |

## ☄️ Asteroid Warning — Common Mistakes

- Every Widget needs to be inside another Widget
- Column children must be a List: children: []
- Text needs a String: Text("Hello") not Text(42)
- Missing comma between widgets causes cryptic errors
- Flutter is VERY sensitive to indentation and commas

📡 See: Code Vault → Flutter Widgets
📡 See: Code Vault → Widget Tree

---

## ⚔️ Your Mission Exercise

Open `calorie_tracker/lib/main.dart` and replace everything with this:
```dart
import 'package:flutter/material.dart';

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

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('🚀 Mission to Planet Caloria'),
        backgroundColor: Colors.deepPurple,
        foregroundColor: Colors.white,
      ),
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              '👨‍🚀 Welcome, Cadet!',
              style: TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 16),
            Text(
              'Planet Caloria needs your help.',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 8),
            Text(
              'Begin your mission to save the planet!',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 32),
            ElevatedButton(
              onPressed: null,
              child: Text('🌍 Accept Mission'),
            ),
          ],
        ),
      ),
    );
  }
}
```

Run it on the emulator:
```bash
flutter run
```

**Mission complete when you see the welcome screen on your emulator! ✅**

---

## 🛸 Reading the Code — Line by Line
```dart
void main() {
  runApp(const CaloriaApp());
}
```
→ "Start the app by running CaloriaApp
   runApp() hands control to Flutter"
```dart
class CaloriaApp extends StatelessWidget {
```
→ "Create a new Widget called CaloriaApp
   StatelessWidget = this screen never changes"
```dart
Widget build(BuildContext context) {
```
→ "Build means describe what this widget looks like
   Flutter calls this automatically"
```dart
return MaterialApp(...)
```
→ "Return a complete app with theme and home screen
   MaterialApp is the root of every Flutter app"
```dart
home: const ProfileScreen(),
```
→ "The first screen to show when app opens"
```dart
return Scaffold(...)
```
→ "Scaffold = a blank page with optional
   top bar, body, and bottom bar"
```dart
AppBar(title: const Text('🚀 Mission to Planet Caloria'))
```
→ "Create a top bar with a title"
```dart
Column(
  mainAxisAlignment: MainAxisAlignment.center,
  children: [...],
)
```
→ "Stack widgets vertically, centered on screen
   children = the list of widgets inside"
```dart
SizedBox(height: 16),
```
→ "Add 16 pixels of empty space between widgets
   Like pressing Enter in a Word document"
```dart
ElevatedButton(
  onPressed: null,
  child: Text('🌍 Accept Mission'),
)
```
→ "A button that says Accept Mission
   onPressed: null means disabled for now
   We will make it work in Mission 6"

---

## 🐛 Debugging Tips

- `Expected to find widget` → missing comma between widgets
- `The argument type Widget can't be assigned` → 
  wrong widget in wrong place
- Screen is blank → check runApp() is called in main()
- Button does nothing → onPressed is null, fixed in Mission 6

---

## 🤖 Phone Mission Control

> "I am learning Flutter widgets for the first time.
> I am trying to build a simple screen with text 
> and a button. I got this error: [paste error].
> Can you explain what it means and give me a hint only?"

---

## 🏆 Mission Complete!

You have entered the Red Nebula! ⭐ +500 Stellar Points

You now know:
- What a Widget is and how they nest together
- How to build a screen with AppBar and body
- How to use Column, Text and ElevatedButton
- Your app is now visible on the emulator!

📡 See: Code Vault → Flutter Widgets
📡 See: Code Vault → StatelessWidget

**→ Ready for Mission 6? Head to the Gas Giant 🪐**