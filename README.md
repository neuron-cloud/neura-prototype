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

---

## Status: v0.5

New Features:
	•	Expanded abbreviation parsing and baseline detection logic
	•	Reflex parsing: Hoffman’s, clonus, DTR scale, Babinski
	•	Basic motor pattern recognition (e.g. 5/5/5/5/4 = motor deficit)
	•	Improved negation handling for terms like “denies saddle anesthesia”
	•	Introduced cranial nerve/motor parsing for slurred speech, facial droop, tongue deviation
	•	Added preliminary handling of baseline vs acute sensory findings

Known Bugs:
	•	Stable neuro flags still firing when deficits are present
	•	Missing some structured output on known deficits (e.g., clonus not flagging in all contexts)
	•	“Intact except” and “baseline” logic still needs refinement

Next Priorities:
	•	Overhaul risk_flag() for stricter conditional logic
	•	Implement plan suggestion engine
	•	Begin streamlining integration for real-time input


---

## License

This project is open for educational and demonstration purposes only.  
It may not be reproduced, modified, or used commercially without explicit permission.  
All rights reserved © 2025 Mychael Delgardo.
