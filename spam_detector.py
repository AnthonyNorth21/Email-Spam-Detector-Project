import re

class SpamDetector:
    def __init__(self, spam_keywords=None, weights=None):
        # Default spam keywords and equal weights if none provided
        self.spam_keywords = spam_keywords or [
            "free", "winner", "cash", "prize", "guaranteed", "offer", "limited time", "act now",
            "click here", "buy direct", "exclusive deal", "money back", "save big", "special promotion",
            "unsecured credit", "credit card offer", "debt relief", "earn money", "free access",
            "free membership", "free quote", "free trial", "instant", "lowest price",
            "online biz opportunity", "risk-free", "win big", "make money", "million dollars",
            "unsecured loan"
        ]
        # Assign weights for keywords (default = 1)
        self.weights = weights or {keyword: 1 for keyword in self.spam_keywords}

    def calculate_spam_score(self, email_message):
        email_lower = email_message.lower()
        spam_score = 0
        found_keywords = {}

        for keyword in self.spam_keywords:
            # Find all occurrences of the keyword
            matches = re.findall(r'\b' + re.escape(keyword) + r'\b', email_lower)
            count = len(matches)
            if count > 0:
                weight = self.weights.get(keyword, 1)
                spam_score += weight * count
                found_keywords[keyword] = count
        
        return spam_score, found_keywords

    def rate_spam_likelihood(self, spam_score):
        # You can adjust thresholds as needed
        if spam_score >= 20:
            return "Very High"
        elif spam_score >= 10:
            return "High"
        elif spam_score >= 5:
            return "Moderate"
        else:
            return "Low"

    def analyze_email(self, email_message):
        score, keywords = self.calculate_spam_score(email_message)
        likelihood = self.rate_spam_likelihood(score)
        return {
            "score": score,
            "likelihood": likelihood,
            "keywords": keywords
        }


def main():
    detector = SpamDetector()

    email_message = input("Enter the email message: ")

    result = detector.analyze_email(email_message)

    print(f"\nSpam Score: {result['score']}")
    print(f"Likelihood of Spam: {result['likelihood']}")
    if result['keywords']:
        print("Keywords/Phrases detected with counts:")
        for keyword, count in result['keywords'].items():
            print(f" - '{keyword}': {count} time(s)")
    else:
        print("No spam keywords detected.")

if __name__ == "__main__":
    main()
