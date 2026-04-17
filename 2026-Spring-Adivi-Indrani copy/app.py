from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).parent
PREREQUISITES_PATH = BASE_DIR / "docs" / "missions" / "prerequisites.md"
VAULT_PATH = BASE_DIR / "docs" / "missions" / "concept_vault.md"
MISSION_PATHS = {
    "mission_1": BASE_DIR / "docs" / "missions" / "mission_1.md",
    "mission_2": BASE_DIR / "docs" / "missions" / "mission_2.md",
    "mission_3": BASE_DIR / "docs" / "missions" / "mission_3.md",
    "mission_4": BASE_DIR / "docs" / "missions" / "mission_4.md",
    "mission_5": BASE_DIR / "docs" / "missions" / "mission_5.md",
    "mission_6": BASE_DIR / "docs" / "missions" / "mission_6.md",
    "mission_7": BASE_DIR / "docs" / "missions" / "mission_7.md",
}

MISSION_XP = {
    "mission_1": 100,
    "mission_2": 200,
    "mission_3": 300,
    "mission_4": 400,
    "mission_5": 500,
    "mission_6": 600,
    "mission_7": 1000,
}


def load_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else "Content not found."


def _find_first_index(text: str, markers: list[str], start: int = 0) -> int:
    indices = [text.find(marker, start) for marker in markers]
    valid = [idx for idx in indices if idx != -1]
    return min(valid) if valid else -1


def platform_prerequisites(markdown_text: str, platform: str) -> str:
    if platform == "mac":
        setup_start = _find_first_index(markdown_text, ["## Mac Setup", "# Mac Setup"])
        setup_end = _find_first_index(markdown_text, ["## Windows Setup", "# Windows Setup"], setup_start + 1)

        flutter_start = _find_first_index(markdown_text, ["### Install Flutter (Mac)"])
        flutter_end = _find_first_index(markdown_text, ["### Install Flutter (Windows)"], flutter_start + 1)
    else:
        setup_start = _find_first_index(markdown_text, ["## Windows Setup", "# Windows Setup"])
        setup_end = _find_first_index(markdown_text, ["## Stuck? Use these AI Prompts", "## Setup Checklist"], setup_start + 1)

        flutter_start = _find_first_index(markdown_text, ["### Install Flutter (Windows)"])
        flutter_end = _find_first_index(markdown_text, ["## ✅ Setup Checklist"], flutter_start + 1)

    if setup_start == -1:
        return markdown_text

    setup_section = markdown_text[setup_start:setup_end] if setup_end != -1 else markdown_text[setup_start:]

    flutter_section = ""
    if flutter_start != -1:
        flutter_section = (
            markdown_text[flutter_start:flutter_end]
            if flutter_end != -1
            else markdown_text[flutter_start:]
        )

    return setup_section + ("\n\n" + flutter_section if flutter_section else "")


def complete_mission(mission_key: str) -> None:
    if mission_key not in st.session_state.completed_missions:
        st.session_state.completed_missions.append(mission_key)
        st.session_state.stellar_points += MISSION_XP.get(mission_key, 0)

# Page configuration
st.set_page_config(
    page_title="Mission to Planet Caloria",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Mission map
MISSIONS = {
    "Prerequisites": "prerequisites",
    "Mission 1: Syntax": "mission_1",
    "Mission 2: Functions and Logic": "mission_2",
    "Mission 3: Lists and Loops": "mission_3",
    "Mission 4: What is an API?": "mission_4",
    "Mission 5: Flutter UI Basics": "mission_5",
    "Mission 6: Connecting the concepts": "mission_6",
    "Mission 7: Planet Caloria: Integration": "mission_7",
}

# Initialize session state
if "current_mission" not in st.session_state:
    st.session_state.current_mission = "prerequisites"
if "completed_missions" not in st.session_state:
    st.session_state.completed_missions = []
if "stellar_points" not in st.session_state:
    st.session_state.stellar_points = 0

# Sidebar
with st.sidebar:
    st.markdown("## Mission to Planet Caloria")
    st.caption("A mission-based learning platform for absolute beginners")
    st.divider()

    # Stellar points display
    st.metric("Stellar Points", st.session_state.stellar_points)
    st.divider()

    # Mission navigation
    st.subheader("Mission Map")
    for mission_name, mission_key in MISSIONS.items():
        is_completed = mission_key in st.session_state.completed_missions
        is_current = mission_key == st.session_state.current_mission
        
        if is_completed:
            label = f"✅ {mission_name}"
        elif is_current:
            label = f"👉 {mission_name}"
        else:
            label = mission_name

        if st.button(label, key=mission_key, use_container_width=True):
            st.session_state.current_mission = mission_key
            st.rerun()

    st.divider()
    # Code Vault button
    if st.button("Code Vault", use_container_width=True):
        st.session_state.current_mission = "vault"
        st.rerun()

# Show current mission
current = st.session_state.current_mission

# Backward compatibility if an old session still points to removed bonus mission
if current == "bonus":
    st.session_state.current_mission = "vault"
    st.rerun()

if current == "prerequisites":
    st.header("Prerequisites — Setup Your Ship")
    st.caption("Start here before Mission 1.")
    st.info("Use this page to complete your setup for Python, VS Code, Flutter")
    if st.button("What are all these? Check Code Vault", key="launchpad_vault_link"):
        st.session_state.current_mission = "vault"
        st.rerun()

    if "setup_platform" not in st.session_state:
        st.session_state.setup_platform = "mac"
    if "setup_done" not in st.session_state:
        st.session_state.setup_done = {"mac": False, "windows": False}

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mac Setup", use_container_width=True):
            st.session_state.setup_platform = "mac"
    with col2:
        if st.button("Windows Setup", use_container_width=True):
            st.session_state.setup_platform = "windows"

    prereq_content = load_markdown(PREREQUISITES_PATH)
    st.markdown(platform_prerequisites(prereq_content, st.session_state.setup_platform))
    
    current_platform = st.session_state.setup_platform
    platform_label = "Mac" if current_platform == "mac" else "Windows"

    if st.button(f"Mark {platform_label} Setup Complete", type="primary", use_container_width=True):
        st.session_state.setup_done[current_platform] = True
        st.toast("🎉 Congratulations on setting up your environment!")
        st.balloons()

    if any(st.session_state.setup_done.values()):
        st.success("🎉 Congratulations on setting up your environment! You are ready for Mission 1.")


elif current == "mission_1":
    st.header("Mission 1: Planet Syntax")
    st.caption("⭐ 100 Stellar Points | ⏱️20 minutes")
    st.progress(0.14, text="Mission 1 of 7")
    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs([
        "Learn",
        "Exercise",
        "Debug Help",
        "AI Prompt"
    ])

    with tab1:
        # Load content from docs/missions/mission_1.md
        st.markdown(load_markdown(MISSION_PATHS["mission_1"]))

    with tab2:
        st.subheader("Your Mission Exercise")
        st.info("Keep your Flutter app structure. Only add the variables inside `main()`.")
        
        st.markdown("### Step 1: Create/Open Your Project")
        st.code("flutter create calorie_tracker\ncd calorie_tracker\ncode .", language="bash")
        
        st.markdown("### Step 2: Open `lib/main.dart`")
        st.markdown("Find the `main()` function. It looks like this:")
        st.code("void main() {\n  runApp(const MyApp());\n}", language="dart")
        
        st.markdown("### Step 3: Add Your Variables (BEFORE `runApp(...)`)")
        st.info("Add your name and body weight. Use the variable types we learned: `String`, `int`, `double`, and `bool`.")
        st.markdown("**Do NOT delete `runApp(const MyApp());`** — just add these lines before it:")
        st.code("""void main() {
  String astronautName = "Your Name Here";
  int missionNumber = 1;
  double bodyWeight = 65.0;
  bool missionAccepted = true;

  print("Welcome, $astronautName!");
  print("Mission number: $missionNumber");
  print("Your weight: $bodyWeight kg");
  print("Mission accepted: $missionAccepted");

  runApp(const MyApp());
}""", language="dart")
        
        st.markdown("### Step 4: Run It")
        st.code("flutter run -d chrome", language="bash")
        
        st.markdown("###Mission Complete When:")
        st.markdown("- You see your printed messages in the **Terminal** (bottom of VS Code)")
        st.markdown("- The app runs without errors")
        
        if st.button("🏆 Mark Exercise Complete", use_container_width=True):
            st.success("Great work! Move to the next mission.")
            st.balloons()

    with tab3:
        st.subheader("Debugging Tips")
        st.write("When you see a red error, always read the **first line** only.")
        st.write("Most common errors in Mission 1:")

        with st.expander("Expected ';' after this"):
            st.error("Expected ';' after this")
            st.write("→ You forgot a semicolon at the end of a line")
            st.write("**Fix:** Add `;` at the end of the line mentioned")

        with st.expander("Undefined name 'variable'"):
            st.error("Undefined name")
            st.write("→ You used a variable before creating it, or misspelled it")
            st.write("**Fix:** Check spelling — Dart is case sensitive!")

        with st.expander("A value of type X can't be assigned to type Y"):
            st.error("A value of type 'String' can't be assigned to 'int'")
            st.write("→ Wrong data type — putting text in a number box")
            st.write("**Fix:** Make sure the value matches the type")

        with st.expander("Expected a declaration, but got backtick"):
            st.error("Expected a declaration, but got '`'")
            st.write("→ You copied backticks from the tutorial into your code")
            st.write("**Fix:** Delete the ``` lines — only copy the code inside!")

    with tab4:
        st.subheader("AI Debugging Prompt")
        st.write("Stuck? Copy this into your AI tool:")
        st.code(""""

    I am an absolute beginner learning Python for the first time. 
    Can you explain what the print() function does and show me 3 simple examples of using it? 
    Please use very simple language."

    I am getting an error in Dart: [Paste Error Here].

    1. Please explain the logic of this error using a real-world analogy (like a library, a kitchen, or a toolbox).

    2. Tell me what 'rule' of the Dart language I am breaking.

    3. Give me a hint to fix it, but do not write the corrected code for me. I want to type it out myself to learn.
        """)
        st.info("💡 Always try yourself first! Struggling is how you actually learn.")

elif current == "mission_2":
    st.header("Mission 2: Functions and Logic")
    st.caption("⭐ 200 Stellar Points | ⏱30 minutes")
    st.progress(0.28, text="Mission 2 of 7")
    st.markdown(load_markdown(MISSION_PATHS["mission_2"]))
    st.divider()
    if st.button("Mark Mission 2 Complete", type="primary", use_container_width=True):
        complete_mission("mission_2")
        st.success("+200 Stellar Points! Mission 2 complete.")
        st.balloons()

elif current == "mission_3":
    st.header("Mission 3: Variables and Data Types")
    st.caption("⭐ 300 Stellar Points | ⏱30 minutes")
    st.progress(0.42, text="Mission 3 of 7")
    st.markdown(load_markdown(MISSION_PATHS["mission_3"]))
    st.divider()
    if st.button("Mark Mission 3 Complete", type="primary", use_container_width=True):
        complete_mission("mission_3")
        st.success("+300 Stellar Points! Mission 3 complete.")
        st.balloons()

elif current == "mission_4":
    st.header("Mission 4: What is an API?")
    st.caption("⭐ 400 Stellar Points | ⏱40 minutes")
    st.progress(0.57, text="Mission 4 of 7")
    st.markdown(load_markdown(MISSION_PATHS["mission_4"]))
    st.divider()
    if st.button("Mark Mission 4 Complete", type="primary", use_container_width=True):
        complete_mission("mission_4")
        st.success("+400 Stellar Points! Mission 4 complete.")
        st.balloons()

elif current == "mission_5":
    st.header("Mission 5: Loops and Conditionals")
    st.caption("⭐ 500 Stellar Points | ⏱45 minutes")
    st.progress(0.71, text="Mission 5 of 7")
    st.markdown(load_markdown(MISSION_PATHS["mission_5"]))
    st.divider()
    if st.button("Mark Mission 5 Complete", type="primary", use_container_width=True):
        complete_mission("mission_5")
        st.success("+500 Stellar Points! Mission 5 complete.")
        st.balloons()

elif current == "mission_6":
    st.header("Mission 6: Classes and Objects")
    st.caption("⭐ 600 Stellar Points | ⏱40 minutes")
    st.progress(0.85, text="Mission 6 of 7")
    st.markdown(load_markdown(MISSION_PATHS["mission_6"]))
    st.divider()
    if st.button("Mark Mission 6 Complete", type="primary", use_container_width=True):
        complete_mission("mission_6")
        st.success("+600 Stellar Points! Mission 6 complete.")
        st.balloons()

elif current == "mission_7":
    st.header("Mission 7: APIs and Web Development")
    st.caption("⭐ 1000 Stellar Points | ⏱60 minutes")
    st.progress(1.0, text="Mission 7 of 7")
    st.markdown(load_markdown(MISSION_PATHS["mission_7"]))
    st.divider()
    if st.button("Mark Mission 7 Complete", type="primary", use_container_width=True):
        complete_mission("mission_7")
        st.success("+1000 Stellar Points! Mission 7 complete.")
        st.balloons()

elif current == "vault":
    st.markdown(load_markdown(VAULT_PATH))

