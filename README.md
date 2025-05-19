# Synapse: Clinical Decision Reflection Prototype

Synapse: Real-Time Clinical Risk Flagging Engine
Synapse is an intelligent NLP-based decision support engine designed to parse unstructured clinical text and extract high-risk neurological exam findings in real-time. Built from the ground up for neurosurgical consults, Synapse identifies subtle red flags—including motor weakness patterns, altered mental status, pathological reflexes, sensory deficits, cauda equina features, and spine instability—with human-like nuance and contextual reasoning.

---

## Purpose

Synapse was born from the gaps in real-world clinical decision-making, especially in high-stakes, high-fatigue environments like neurosurgery.  
It doesn't replace judgment. It reflects it.

---
- Surface cognitive biases and risk signals
- Flag red flags from clinical vignettes
- Prompt structured reflection to prevent preventable harm
  
🔧 Use Cases
- Triage augmentation for neurosurgical consult services
- EMR decision support
- NLP-enhanced risk analysis pipelines
- Academic research on neurological NLP

---

## Core Features (v0.6)

- Motor Strength Parsing: Accurately detects weakness in upper/lower extremities using 5-point motor scales (e.g., RUE 5/5/5/4-/4), even with inconsistent formatting.
- Abbreviation Expansion: Expands over 200+ medical shorthand terms for clarity and downstream parsing.
- Advanced Negation Detection: Context-aware negation engine handles multi-symptom denials (e.g. "denies weakness, numbness, saddle anesthesia").
- Baseline Filtering: Filters out chronic findings or known deficits to reduce false positives.
- Physical Exam Extraction: Automatically isolates neurological exam content from full consult blurbs.
- Risk Stratification: Flags findings based on severity: 🚨 Critical, ⚠️ High-Risk, 🦴 Focal Deficit, 🧠 Cognitive, 🔍 Monitor, ✅ Stable.

📥 Input
Raw consult blurbs or EMR notes (.txt file format recommended, delimited by ___).

'Exam - wide awake, intact except mildly slurred speech, Lt droop, Rt tongue deviation, subtle lt drift, LUE 4+/5'

📤 Output
Structured and prioritized clinical flags with severity-tiered emojis.

'🦴 Weakness noted in LEFT EXTREMITY (drift)  
🔍 Finding: mildly slurred speech  
🔍 Finding: left droop  
🔍 Finding: right tongue deviation  
🔍 Finding: subtle left drift  
🔍 Finding: left upper extremity 4+/5'

---

## License

This project is open for educational and demonstration purposes only.  
It may not be reproduced, modified, or used commercially without explicit permission.  
All rights reserved © 2025 Mychael Delgardo.
