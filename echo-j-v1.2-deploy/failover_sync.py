import os
import datetime

def write_to_local(content: str):
    now = datetime.datetime.utcnow().isoformat()
    filename = f"memory/shared/echo_j_backup_{now}.md"
    with open(filename, "w") as f:
        f.write(content)
    print(f"[Failover] Written to local file: {filename}")
