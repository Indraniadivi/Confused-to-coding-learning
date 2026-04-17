# Beginner-Centered Mission Platform for Mobile App Learning

## 1. Introduction
Many non-coders can follow isolated coding tutorials but still struggle to independently build a working application. In practice, the main barriers are: (1) fragmented learning content, (2) setup friction in early stages, and (3) weak transfer from syntax-level exercises to system-level understanding. This project addresses those barriers with a beginner-centered learning platform that combines guided missions, a concrete app artifact, and structured AI prompting support.

The platform is implemented as a mission flow in Streamlit and a companion Flutter calorie-tracker application. Learners progress from setup and basic syntax to API usage and integrated app behavior. The goal is not only to help learners run code, but also to help them explain what the code is doing.

**Research Question:**  
Can a learning platform, designed from a beginner's perspective, that explains basic concepts, provides structured mission-based exercises, and guided AI prompts, enable students to build and understand a working mobile application?

To answer this question, the project defines four objectives:
1. Build a complete mission sequence with explicit beginner scaffolding.
2. Deliver a working learner-facing mobile application artifact.
3. Integrate AI prompts as guided support for explanation and debugging.
4. Gather initial evaluation evidence through tests and learner-focused instruments.

The contributions are: a technical artifact (mission platform + app prototype), a reusable instructional structure (mission-based sequencing with checkpoints), and early empirical evidence on implementation readiness and current limitations.

## 2. Background
### 2.1 Beginner Learning Challenges in Programming
New Programmers typically face high intrinsic load from syntax plus high extraneous load from tooling complexity. Cognitive Load Theory motivates instructional designs that stage complexity and reduce unnecessary setup effort [1].

### 2.2 Mission-Based and Gamified Learning
Gamified progression and milestone framing are widely used to improve persistence and engagement in learning systems [2]. In this project, “missions” are used as a pacing mechanism: each mission introduces a bounded concept group and immediately ties it to implementation tasks.

### 2.3 Cross-Platform App Construction for Beginners
Flutter is a practical beginner-friendly target because one codebase supports web and mobile deployment [3]. This project prioritizes a Chrome-first run path during instruction to reduce early environment friction and improve first-run success.

### 2.4 Nutrition API Integration Trade-Offs
The app’s food-logging functionality requires external nutrition APIs. A prior project analysis compared Spoonacular and Nutritionix, with trade-offs between onboarding simplicity (Spoonacular) and natural-language endpoint richness (Nutritionix) [4][5]. The current platform using Spoonacular for initial learner integration because first successful API calls are easier for beginners.

### 2.5 AI-Assisted Learning and Guardrails
LLM-based assistance can accelerate beginner understanding when the learner is prompted to verify and reason about outputs rather than copy blindly [6]. Therefore, this platform uses constrained AI prompting templates for explanation and debugging, not unrestricted answer generation.

**Gap addressed by this work:** many resources either teach isolated syntax or provide finished template projects. This platform targets the middle ground: guided construction of a working app while building conceptual understanding through mission sequencing and reflective AI scaffolding.

## 3. Approach, Methods, and Tools
### 3.1 System Architecture
The system has three layers:
1. **Learning Layer (Streamlit):** prerequisites, mission map, progress state, debug tips, and prompt scaffolds.
2. **Application Layer (Flutter):** learner app for target calculation and food logging.
3. **Evaluation Layer:** unit tests, artifact checks, and pre/post survey instrument.

### 3.2 Mission Flow and Pedagogical Structure
The Streamlit platform includes prerequisites, seven missions plus code vault. The sequence gradually increases complexity from basic variables/functions to app integration with API data. Each mission includes:
- learning objectives,
- implementation task(s),
- troubleshooting support,
- completion feedback.

This structure is intended to reduce learner overwhelm while creating visible progress.

### 3.3 AI Prompt Integration (Updated Scope)
AI guidance is integrated directly inside mission flow (e.g., “Debug Help” and “AI Prompt” tabs).  

### 3.4 Toolchain and Implementation Choices
- **Learning UI:** Streamlit in Python (`app.py`).
- **Mobile/Web app artifact:** Flutter + Dart (`calorie_tracker/lib/main.dart`, `calorie_tracker/lib/food_log_screen.dart`).
- **Computation baseline module:** Python calorie logic (`src/calorie_logic.py`).
- **Testing:** Python `unittest` (`tests/test_calorie_logic.py`).
- **External data source:** Spoonacular API for nutrition lookup.

### 3.5 Evaluation Design
The current evaluation combines:
- artifact verification (can learner run and navigate system components),
- automated logic testing for nutritional calculations,
- pre/post learner survey instrument for confidence and concept understanding (`docs/survey.md`).

At this stage, evaluation evidence includes completed engineering validation and completed survey collection, with remaining work focused on incorporating reviewer feedback into the final interpretation and presentation.

## 4. Results
### 4.1 Implemented Artifacts
The repository currently contains:
- a functioning Streamlit mission interface with prerequisites, mission navigation, and concept vault,
- seven mission documents covering beginner-to-integration progression,
- a Flutter calorie-tracker prototype with profile input, target calculation, food search, and food log interactions,
- embedded AI prompt support inside mission workflow.

### 4.2 Testing Outcomes (Current Snapshot)
Unit testing of calorie logic was executed with Python `unittest`. Current output:
- 14 tests run,
- 14 passed,
- 0 failed.

This indicates that the current nutrition-logic baseline is stable for the tested scenarios.

### 4.3 Survey Outcomes (Completed)
The pre/post survey process has been completed for the planned participants. Results show improved learner confidence and clearer concept-level understanding (for example, variables, APIs, and frontend/backend roles), along with actionable qualitative feedback on sections that still need clarity improvements.

### 4.4 Objective-by-Objective Status
**Objective 1 (mission sequence):** Achieved at implementation level (prerequisites + missions + guidance tabs).  
**Objective 2 (working app artifact):** Achieved for core workflow and data integration path.  
**Objective 3 (guided AI support):** Achieved through integrated prompt scaffolds (not a separate bonus mission).  
**Objective 4 (evaluation evidence):** Achieved at draft stage (all automated tests passing and survey completed), with additional refinement in progress based on received feedback.

### 4.5 Evidence Toward Research Question
The implemented system demonstrates that beginners can be guided through construction of a working app artifact, and completed survey evidence indicates gains in confidence and concept understanding. Current remaining work is not data collection, but improving sections identified in reviewer feedback.

## 5. Discussion
The project’s strongest outcome is coherence: concept teaching, implementation tasks, and artifact behavior are aligned in a single workflow. Learners do not only read explanations; they actively perform setup, coding, debugging, and app execution tasks in sequence.

The integrated AI prompt strategy is also a design strength. By framing prompts as explanation and hint requests, the platform encourages reflective debugging instead of direct answer dependence. This directly supports the “build and understand” emphasis of the research question.

However, the current draft still has limitations:
1. **Writing quality and clarity:** several sections need tightening based on reviewer feedback.
2. **Result presentation depth:** survey findings should be presented with clearer tables/figures in the final version.
3. **Generalizability:** evidence currently reflects a small-scale project context; broader cohort validation is still needed.

Based on current evidence, the research question is **supported** for this project scope: the platform supports app construction and improved conceptual engagement for beginner learners, while still leaving room for stronger future validation at larger scale.

## 6. Conclusions
This project built a beginner-centered mission platform that combines instructional flow (Streamlit), a concrete app artifact (Flutter calorie tracker), and embedded AI prompt scaffolding. The system is technically functional and provides a structured path for novice learners to move from basic concepts to integrated application behavior.

The current evidence supports the conclusion that this design can help beginners build a working mobile app and improve conceptual reasoning during debugging and implementation. The next steps are to address received feedback by refining analysis presentation, tightening discussion language, and strengthening comparative framing against non-mission learning approaches.

## References
[1] J. Sweller. 1988. Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285.

[2] S. Deterding, D. Dixon, R. Khaled, and L. Nacke. 2011. From game design elements to gamefulness: Defining gamification. In *MindTrek 2011*.

[3] Flutter Documentation. 2026. Flutter development resources. https://docs.flutter.dev/

[4] Spoonacular API Documentation. 2026. https://spoonacular.com/food-api/docs

[5] Nutritionix Developer Documentation. 2026. https://developer.nutritionix.com/

[6] K. Kasneci et al. 2023. ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences*, 103.

## AI Usage Statement
GitHub Copilot and ChatGPT were used to help revise prose clarity, organization, and section flow. AI was not used to generate the research question, fabricate results, or invent analysis outcomes. All claims were checked against repository artifacts, test outputs, and project documentation before inclusion.
