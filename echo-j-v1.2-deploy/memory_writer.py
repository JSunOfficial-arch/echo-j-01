import os
import datetime

def write_to_github(content: str, filename="log.md"):
    token = os.getenv("GITHUB_TOKEN")
    repo = "JSunOfficial-arch/echo-j-01"
    api_url = f"https://api.github.com/repos/{repo}/contents/{filename}"
    import base64, requests

    now = datetime.datetime.utcnow().isoformat()
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 先取得 SHA（若檔案已存在）
    sha = None
    resp = requests.get(api_url, headers=headers)
    if resp.status_code == 200:
        sha = resp.json()["sha"]

    payload = {
        "message": f"Echo-J log update {now}",
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main"
    }
    if sha:
        payload["sha"] = sha

    r = requests.put(api_url, headers=headers, json=payload)
    print(f"GitHub update status: {r.status_code}")
