
# SpamDetector

A simple Python-based tool to detect and rate the likelihood of spam in an email message using keyword matching and a weighted scoring system.

## Features

* Detects common spam-related keywords and phrases in email content
* Calculates a weighted spam score based on keyword frequency
* Provides a rating of spam likelihood: Low, Moderate, High, or Very High
* Outputs a list of matched keywords and how often each appears
* Easily extendable with custom keyword lists and weights

## How It Works

* A default list of spam keywords is defined (can be customized)
* Each keyword can be assigned a weight (default is 1)
* The input email is converted to lowercase and scanned for keyword matches
* The spam score is calculated as the sum of matched keywords multiplied by their weights
* The total score is then used to assign a likelihood rating

### Spam Likelihood Levels

* Very High: score ≥ 20
* High: score ≥ 10
* Moderate: score ≥ 5
* Low: score < 5

## Sample Interaction

Enter the email message:
Congratulations! You are a winner. Act now for your free prize. Click here to claim your cash.

Spam Score: 7
Likelihood of Spam: Moderate
Keywords/Phrases detected with counts:

* 'free': 1 time(s)
* 'winner': 1 time(s)
* 'prize': 1 time(s)
* 'act now': 1 time(s)
* 'click here': 1 time(s)
* 'cash': 1 time(s)

## Code Overview

**SpamDetector class**

****init**(self, spam\_keywords=None, weights=None)**
Initializes with a default set of spam keywords and assigns a default weight of 1 to each if no custom weights are provided.

**calculate\_spam\_score(self, email\_message)**
Scans the email message for keyword matches and calculates the spam score based on keyword frequency and assigned weights.

**rate\_spam\_likelihood(self, spam\_score)**
Rates the email’s likelihood of being spam based on the spam score.

**analyze\_email(self, email\_message)**
Runs the full analysis pipeline: calculates score, determines likelihood, and returns keyword match data.

**main()**
Prompts the user for an email message, analyzes it, and prints the results to the console.

