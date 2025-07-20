class PasswordChecker:
    def check_strength(self, password):
        if len(password) < 6:
            return "Weak: Too short"
        if password.isalpha() or password.isdigit():
            return "Moderate: Add numbers & symbols"
        return "Strong password"
