import requests
import os

username = "AbhijeetSingh1801"
token = os.environ.get("PAT_TOKEN")

# Fetch contributions (GraphQL API)
query = """
{
  user(login: "%s") {
    contributionsCollection {
      contributionCalendar {
        totalContributions
      }
    }
  }
}
""" % username

response = requests.post(
    "https://api.github.com/graphql",
    json={"query": query},
    headers={"Authorization": f"bearer {token}"}
)

data = response.json()
total = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

# Write a very simple SVG
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="80">
  <rect width="100%" height="100%" fill="white"/>
  <text x="10" y="40" font-size="20" fill="black">
    Contributions: {total}
  </text>
</svg>"""

with open("stats.svg", "w") as f:
    f.write(svg)
