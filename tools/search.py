def search_logs(log_text, keyword):
    return [line for line in log_text.split("\n") if keyword.lower() in line.lower()]