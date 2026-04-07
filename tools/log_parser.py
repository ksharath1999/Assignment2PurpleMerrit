import re

def extract_errors(log_text):
    return re.findall(r"ZeroDivisionError.*", log_text)