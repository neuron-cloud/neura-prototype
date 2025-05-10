# NEURA Blurb Risk Flagging Tool

def risk_flag(blurb):
    blurb_lower = blurb.lower()

    if "midline shift" in blurb_lower or "mls" in blurb_lower:
        return "⚠️ High-risk: Possible brain shift. Escalate."
    elif "cirrhosis" in blurb_lower or "coags" in blurb_lower:
        return "🔎 Flag: Coagulopathy risk—evaluate before intervention."
    elif "awake" in blurb_lower and "intact" in blurb_lower:
        return "✅ Currently stable—continue monitoring."
    else:
        return "⚠️ No known flags, but requires full manual review."

# Sample test run
blurb = """
63F with HCV-cirrhosis, recent burr hole evac, no prior imaging, SDH w/3mm MLS.
Na 130, coags wnl. Exam: wide awake and intact.
"""
print(risk_flag(blurb))
