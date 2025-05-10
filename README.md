# Synapse: Clinical Decision Reflection Prototype

NEURA is a prototype AI tool built to assist in neurosurgical consult decision-making.  
It analyzes real clinical text to flag risk patterns such as:

- Midline shift
- Coagulopathy indicators
- Myelopathy signs
- Frailty or cognitive decline
- Neurological exam findings

---

### Core Objectives:
- Surface cognitive biases and risk signals
- Flag red flags from clinical vignettes
- Prompt structured reflection to prevent preventable harm
  
---

## Where NEURA Lives

The current working prototype is live in [Google Colab](https://colab.research.google.com).  

To access the live Colab environment, contact the creator.

---

## Status

NEURA v0.3 includes:
- Phrase-level filtering (“coags pending” ≠ coagulopathy)
- Negation handling (“denies clonus” ≠ clonus present)
- Basic clinical heuristics based on exam interpretation

Next: deploy to Streamlit or cloud API

---

## License

This project is open for educational and demonstration purposes only.  
It may not be reproduced, modified, or used commercially without explicit permission.  
All rights reserved © 2025 Mychael Delgardo.
