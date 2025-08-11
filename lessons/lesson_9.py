# Regex excersizes
import re


def is_valid_email(email):
    pattern = r"^\w+@\w+\.[a-z]{2,}"
    return re.match(pattern, email) is not None


def extractPhonNumber(email):
    pattern = r'\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b'
    return pattern


def parse_csv_data(csv_string):
    rows = csv_string.strip().split('\n')
    data = []
    for row in rows:
        values = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', row)
        data.append(values)
    return csv_string, data  # returning both original text and parsed data


def extract_urls(text):
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    urls = re.findall(pattern, text)
    return text, urls  # returning both original text and extracted URLs


def run9():
    mail = "marom313gmail.com"
    mail2 = "test@openai.org"
    mail3 = "invalid.email.com"
    print(is_valid_email(mail3))
    csv_input = 'name,email\nJohn,john@example.com\nJane,jane@example.com'
    raw_csv, parsed_csv = parse_csv_data(csv_input)

    text = "Visit our site at https://example.com or http://test.org"
    raw_text, urls = extract_urls(text)

    print("Original CSV:", raw_csv)
    print("Parsed CSV:", parsed_csv)
    print("Original Text:", raw_text)
    print("Extracted URLs:", urls)
