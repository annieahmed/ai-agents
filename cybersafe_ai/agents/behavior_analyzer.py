class BehaviorAnalyzer:
    def analyze(self, habit):
        risky_keywords = ["same password", "click links", "no antivirus"]
        for keyword in risky_keywords:
            if keyword in habit.lower():
                return "⚠️ Risky habit. Consider changing behavior."
        return "✅ Safe habit"
