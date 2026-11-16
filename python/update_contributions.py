import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone 
from pathlib import Path

GITHUB_API_URL = "https://api.github.com/graphql"
GITHUB_USERNAME = "sergiorg03"

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent / "data" / "github-contributions.json"
)

def get_contributions(token: str)-> dict:
    """Consulta las contribuciones de GitHub de los últimos 12 meses."""

    now = datetime.now(timezone.utc)
    start_date = now - timedelta(days=365)

    query = """
        query($username: String!, $from: Datetime!, $to: Datetime!) {
            user(login: $username) {
                contributionsCollection(from: $from, to: $to) {
                    contributionCalendar {
                        totalContributions
                        weeks {
                            contributionDays {
                                date
                                contributionCount
                                weekday
                            }
                        }
                    }
                }
            }
        }    
    """

    variables = {
        "username": GITHUB_USERNAME,
        "from": start_date.isoformat(),
        "to": now.isoformat(),
    }

    payload = json.dumps({
        "query": query,
        "variables": variables,
    }).encode("utf-8")

    request = urllib.request.Request(
        GITHUB_API_URL, 
        data=payload, 
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))

    if "errors" in result:
        raise RuntimeError(
            f"Error de GitHub GraphQL: {result['errors']}"
        )

    user = result.get("data", {}).get("user")

    if user is None:
        raise RuntimeError(
            f"No se encontró el usuario {GITHUB_USERNAME}"
        )

    calendar = (
        user["contributionsCollection"]["contributionCalendar"]
    )

    return {
        "username": GITHUB_USERNAME,
        "totalContributions": calendar["totalContributions"],
        "generatedAt": now.isoformat(),
        "weeks": calendar["weeks"],
    }


def main():
    token = os.getenv("GH_TOKEN")

    if not token:
        raise RuntimeError(
            "No se ha encontrado la variable de entorno GH_TOKEN"
        )

    data = get_contributions(token)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(
        f"Contribuciones obtenidas: "
        f"{data['totalContributions']}"
    )
    print(f"JSON generado en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()