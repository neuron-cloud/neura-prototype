# Synapse: Clinical Decision Reflection Prototype

**Synapse** is an AI-powered logic engine that assists in neurosurgical consult decision-making.  
It scans real clinical text for risk signals and cognitive bias markers, offering structured feedback to clinicians or trainees.

---

## Purpose

Synapse was born from the gaps in real-world clinical decision-making, especially in high-stakes, high-fatigue environments like neurosurgery.  
It doesn't replace judgment. It reflects it.

---
- Surface cognitive biases and risk signals
- Flag red flags from clinical vignettes
- Prompt structured reflection to prevent preventable harm

---

## Features

- Keyword-based risk flagging
- Negation-aware logic (e.g., “denies clonus” ≠ clonus)
- Exception filters (e.g,. “coags pending” ≠ coagulopathy)
- Basic logic-based classification for 6+ neurosurgical red flags
- Console output or script-based review
- Expanded abbreviation parsing and baseline detection logic
- Reflex parsing: Hoffman’s, clonus, DTR scale, Babinski
- Basic motor pattern recognition (e.g. 5/5/5/5/4 = motor deficit)
- Improved negation handling for terms like “denies saddle anesthesia”
- Introduced cranial nerve/motor parsing for slurred speech, facial droop, tongue deviation
- Added preliminary handling of baseline vs acute sensory findings

---

## Current Version: `v0.5.4`

### Core Functionalities
- **Abbreviation Expansion:** Fully customizable dictionary supporting over 150 medical terms
- **Negation Detection:** Handles direct, list-based, and contextual denial of symptoms
- **Physical Exam Parser:**
  - Orientation (Ox0–3)
  - Motor strength breakdown with weakness flags (bug pending fix)
  - Sensory deficits
  - Reflex abnormalities (Hoffman’s, clonus, Babinski)
  - Sphincter findings and saddle anesthesia
  - Cervical/thoracolumbar tenderness
- **Risk Flagging Engine:** Escalates flags across 7 domains (e.g. AMS, myelopathy, frailty, cancer, spine)

---

## 🚧 Bugs / In Progress
- Motor strength weakness flag not triggering (likely due to variable assignment bug in `extract_exam_components`)
- `intact except` clause triggers even when more specific flags (e.g. weakness) are found
- Currently hardcoded to `/content/demo_blurbs.txt` in Colab

---

## 📂 Demo Instructions
1. Place your `demo_blurbs.txt` file in the Colab `/content` directory.
2. Run Cells 1–7 in order. Output will appear under each consult.
3. Flags include:
   - ✅ Stable or normal findings
   - ⚠️ Warning signs
   - 🚨 Critical emergencies
   - 🧠 Cognitive or motor concerns

---

## Next Steps
- [ ] Fix `weakness` variable initialization bug in motor parsing
- [ ] Ensure flags trigger for all consults
- [ ] Move flag messages into structured dict for export
- [ ] Add `severity` tier to each flag (1–3)

---

## License

This project is open for educational and demonstration purposes only.  
It may not be reproduced, modified, or used commercially without explicit permission.  
All rights reserved © 2025 Mychael Delgardo.
