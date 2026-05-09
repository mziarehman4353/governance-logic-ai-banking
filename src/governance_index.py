
def classify_governance(row):

    if row["tech_ratio"] > 0.6:
        return "Technocratic"

    elif row["ethical_ratio"] > 0.3:
        return "Ethical"

    else:
        return "Hybrid"
