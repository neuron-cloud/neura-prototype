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

## Status: v0.3

Synapse is a fully functional Python script deployed via Google Colab, currently returning correct structured flags based on a real dataset of consult blurbs.

To access the live Colab environment, contact the creator.

---

## Roadmap

- [ ] v0.4: Multi-flag return per consult
- [ ] v0.5: Streamlit interface (web-based demo)
- [ ] v1.0: Open-source public release with hospital-safe dataset

---

## License

This project is open for educational and demonstration purposes only.  
It may not be reproduced, modified, or used commercially without explicit permission.  
All rights reserved © 2025 Mychael Delgardo.
