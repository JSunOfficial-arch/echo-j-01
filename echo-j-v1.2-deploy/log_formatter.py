def format_log(message, reasoning=None):
    from datetime import datetime
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    log = f"# Echo-J Log — {now}\n\n"
    log += f"## Message\n{message}\n\n"
    if reasoning:
        log += f"## Reasoning\n{reasoning}\n"
    return log
