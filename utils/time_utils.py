from datetime import timedelta

def format_duration(td):
    total_minutes = int(td.total_seconds() // 60)

    d, rem_min = divmod(total_minutes, 1440)
    h, m = divmod(rem_min, 60)

    return " ".join(
        f"{v}{k}" for v, k in [(d, "d"), (h, "h"), (m, "m")] if v
    ) or "0m"