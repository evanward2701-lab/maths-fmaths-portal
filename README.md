# maths-fmaths-portal

# CCEA A-Level Maths & Further Maths Interactive Learning Portal

## 🎯 Project Vision & Overview
Welcome to the repository for a fully interactive, maximally optimized **A-Level Maths and Further Maths** learning portal. 

This platform is designed to be **completely dummy-proof**. It must allow a student who has never studied A-Level Mathematics or Further Mathematics to learn from absolute scratch, navigate intuitively, and build their knowledge on a daily basis.

**CRITICAL DIRECTIVE:** The final structure of this portal must strictly follow the **CCEA Exam Board Specification**. 

---

## 🤖 AI Assistant Master Instructions
**IMPORTANT: If you are an AI Assistant (e.g., Cursor, Windsurf, Copilot) reading this repository to help write code, structure folders, or migrate content, you MUST strictly adhere to the following guidelines.**

### 1. The Source of Truth vs. Existing Content
*   **The Source of Truth (CCEA Specs):** The absolute structural blueprint for this portal is defined by the CCEA Specification maps located in the repository evidence files. You must use these to build the "shell" (the site structure, navigation, unit/chapter organization).
*   **The Existing Content (Edexcel):** The legacy lessons, SVGs, TikZ, Mermaid diagrams, and HTML widgets currently in the repository are structured around the Edexcel specification. They are located at the following local pathways:
    *   **Maths:** `/Users/evanward/Documents/GitHub/maths-fmaths-portal/maths-portal copy 2/source/Maths`
    *   **Further Maths:** `/Users/evanward/Documents/GitHub/maths-fmaths-portal/maths-portal copy 2/source/Further Maths`

### 2. The Content Migration Strategy (Iterative Execution)
You must migrate content from the legacy Edexcel folders into the new CCEA shell **carefully, one chapter or unit at a time**. Do not attempt bulk migrations of the entire codebase at once. Wait for human approval before moving to the next unit.

**The Workflow:**
1. Read the required CCEA learning outcomes for a specific target chapter.
2. Build the empty structural shell for that CCEA chapter.
3. Search the provided Edexcel source pathways for matching lesson content and visual assets.
4. Import, adapt, and rewrite the content to fit the CCEA shell perfectly. 
5. Ensure the resulting Standard Lessons are fully comprehensive, highly detailed, dummy-proof, and seamlessly integrate the original visual assets to assist with understanding.

### 3. The "Enrichment" Rule for Off-Spec Content
Because the source material is Edexcel-based, you will inevitably encounter topics, subtopics, or examples that are **not** on the CCEA specification.
*   **Rule: DO NOT DELETE THIS CONTENT.**
*   Instead, place any non-CCEA topics into a clearly separated **"Enrichment"** section within that unit. This ensures the main learning path remains 100% CCEA-compliant while preserving advanced, out-of-spec material for curious students.

### 4. Required Portal Features per Topic
When building out a topic, the following sections MUST be created:

1.  **Standard Lessons:** The core learning material. Step-by-step, fully comprehensive tutorials with heavy integration of interactive widgets and visual assets.
2.  **Practice / Exam Questions:** Create a completely separate, dedicated section/routing structure for exam preparation. Currently, this will serve as a **placeholder shell**. The human user will manually copy and paste Past Paper questions and solutions into this section at a later date. Do not auto-generate fake exam questions.
3.  **Flashcards Hub:** Create a dedicated section optimized for active recall and repetition. Automatically extract key formulas, definitions, and useful revision information from the lesson to populate this area.
4.  **Additional Learning Tools:** Proactively suggest, design, and implement any other beneficial learning tools (e.g., progress trackers, formula cheat sheets, interactive calculators, glossary popups) that enhance the dummy-proof learning experience.

---

## 📂 Project Tracking & Directories
*   **`COMPLETED_PHASES.md`**: Tracking document for project phases. Update this as we complete phases.
*   **`directory_structure.md`**: Overview of how files are currently ordered in the legacy system.
*   **CCEA Specs**: Use the attached specification map documents as the ultimate guide.

---

**Note to AI:** When you begin a new session, acknowledge you have read these instructions from the `README.md` and ask the user which unit or phase they would like to begin with today.