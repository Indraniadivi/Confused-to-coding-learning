# Prerequisites: Setting Up Your Development Environment

## What you will install
- Python 3
- VS Code
- Flutter
- Chrome

## What you will build
A running Flutter app in Chrome before writing your own code.

### 📋 Prerequisites: Setting Up Your Computer

**Complete this before starting Mission 1. This is a one-time setup only.**

---

# Mac Setup

### Step 1: Check if Python is installed
1. Press `Command + Space`
2. Type `Terminal` and press Enter
3. Type this and press Enter:

```bash
python3 --version
```

**If you see** `Python 3.x.x` → skip to Step 3  
**If you see an error** → go to Step 2

---

### Step 2: Install Python (Mac)
1. Go to https://www.python.org/downloads/
2. Click the big **Download Python** button
3. Open the downloaded `.pkg` file
4. Follow the installer steps
5. Go back to Terminal and type:

```bash
python3 --version
```

---

### Step 3: Install VS Code (Mac)
1. Go to https://code.visualstudio.com/
2. Click **Download for Mac**
3. Open the downloaded `.zip` file
4. Drag **Visual Studio Code** into your **Applications** folder
5. Open VS Code from Applications

---

### Step 4: Install Python Extension in VS Code (Mac)
1. Open VS Code
2. Click the **Extensions** icon on the left sidebar
3. Search for **Python**
4. Click **Install** on the one made by Microsoft

---

### Step 5: Install Flutter (Mac)
1. Go to https://docs.flutter.dev/get-started/install
2. Download the Flutter SDK for Mac
3. Extract the zip file
4. Add Flutter to your PATH
5. Verify Flutter is installed:

```bash
flutter doctor
```

---

### Step 6: Create and run your first Flutter app in Chrome (Mac)
1. Open Terminal
2. Run:

```bash
flutter create calorie_tracker
cd calorie_tracker
code .
flutter run -d chrome
```

✅ Success! A Chrome window should open with the default Flutter app.

---

## Windows Setup

### Step 1: Check if Python is installed
1. Press the `Windows key`
2. Type `cmd` and press Enter
3. Type this and press Enter:

```bash
python --version
```

**If you see** `Python 3.x.x` → skip to Step 3  
**If you see an error** → go to Step 2

---

### Step 2: Install Python (Windows)
1. Go to https://www.python.org/downloads/
2. Click the big **Download Python** button
3. Open the downloaded `.exe` file
4. Before clicking Install, check the box that says **Add Python to PATH**
5. Click **Install Now**
6. Open Command Prompt again and type:

```bash
python --version
```

---

### Step 3: Install VS Code (Windows)
1. Go to https://code.visualstudio.com/
2. Click **Download for Windows**
3. Open the downloaded `.exe` file
4. Follow the installer
5. Open VS Code when done

---

### Step 4: Install Python Extension in VS Code (Windows)
1. Open VS Code
2. Click the **Extensions** icon on the left sidebar
3. Search for **Python**
4. Click **Install** on the one made by Microsoft

---

### Step 5: Install Flutter (Windows)
1. Go to https://docs.flutter.dev/get-started/install
2. Download the Flutter SDK for Windows
3. Extract it to a folder such as `C:\flutter`
4. Add Flutter to PATH
5. Verify Flutter is installed:

```bash
flutter doctor
```

---

### Step 6: Create and run your first Flutter app in Chrome (Windows)
1. Open Command Prompt
2. Run:

```bash
flutter create calorie_tracker
cd calorie_tracker
code .
flutter run -d chrome
```

✅ Success! A Chrome window should open with the default Flutter app.

---

## Stuck? Use these AI prompts

**If Python installation isn't working:**
> I am trying to install Python on my [Mac/Windows] computer for the first time and I am getting this error: [paste your error here]. Can you help me fix it in simple steps?

**If VS Code isn't working:**
> I installed VS Code on my [Mac/Windows] computer but when I try to run my Python file I see this error: [paste your error here]. I am a complete beginner, can you help me fix this?

**If Flutter isn't working:**
> I am trying to set up Flutter on my [Mac/Windows] computer and I am getting this error: [paste error]. Can you help me fix it in simple steps?

---

## Setup Checklist
Before moving forward, make sure you can check all of these:

- [ ] Python is installed and shows a version number in terminal
- [ ] VS Code is installed and opens correctly
- [ ] Python extension is installed in VS Code
- [ ] Flutter is installed and `flutter doctor` runs
- [ ] You created `calorie_tracker`
- [ ] You ran the Flutter app in Chrome

---

## 🎉 Prerequisites Complete
Congratulations on setting up your environment!  
You are now ready to begin Mission 1. 🚀

🎊🎊🎊
**All checked? You are ready for Mission 1!**