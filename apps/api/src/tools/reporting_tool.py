def summarize_report(x: str | None) -> str:
    if not x:
        return ""
    return "Report summary: " + (x[:300] + ("..." if len(x) > 300 else ""))
