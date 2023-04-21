import random

# Define a list of security events
security_events = [
  "Unauthorized access detected on the network",
  "Suspicious activity reported on the server",
  "Phishing attack detected in employee emails",
  "Ransomware attack attempted on the system",
  "Sensitive data breach discovered in the database",
  "Vulnerability found in a critical software component",
  "Denial of service attack launched on the website",
  "Malware infection detected on the endpoint devices",
  "Social engineering attempt reported by an employee",
  "Physical security breach reported at the office premises"
]

# Define a list of potential impact levels
impact_levels = [
  "Low",
  "Medium",
  "High",
  "Critical"
]

# Generate a random security insight
def generate_insight():
  event = random.choice(security_events)
  impact = random.choice(impact_levels)
  return f"{event} with {impact} impact level."

# Example usage
print(generate_insight())
