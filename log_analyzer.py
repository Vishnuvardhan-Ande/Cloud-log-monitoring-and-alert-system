def analyze_logs(content):

    severity = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    lines = content.split("\n")

    for line in lines:
        if "INFO" in line:
            severity["INFO"] += 1
        elif "WARNING" in line:
            severity["WARNING"] += 1
        elif "ERROR" in line:
            severity["ERROR"] += 1
        elif "CRITICAL" in line:
            severity["CRITICAL"] += 1

    return severity