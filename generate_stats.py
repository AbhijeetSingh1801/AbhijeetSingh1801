import requests
import os
import sys
from datetime import datetime
token = os.getenv("PAT_TOKEN")
if not token:
    print("Missing PAT_TOKEN env var", file=sys.stderr)
    sys.exit(1)

query = """
{
  user(login: "AbhijeetSingh1801") {
    contributionsCollection {
      contributionCalendar {
        totalContributions
      }
    }
  }
}
"""

headers = {"Authorization": f"Bearer {token}"}
response = requests.post(
    "https://api.github.com/graphql",
    json={"query": query},
    headers=headers,
)

result = response.json()
print("DEBUG:", result)  # 👈 add this

if "errors" in result:
    print("GraphQL returned errors:", result["errors"], file=sys.stderr)
    sys.exit(1)

try:
    total = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
except KeyError:
    print("Unexpected response format", result, file=sys.stderr)
    sys.exit(1)

print("Total contributions:", total)



# Always update a text file with the last run timestamp
with open("last_run.txt", "a") as f:
    f.write(f"Last run: {datetime.utcnow().isoformat()}Z\n")

