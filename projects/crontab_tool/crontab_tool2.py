import re as R

from typing import Dict, List

NUM = {"minute": r"(?:[0-5]?\d)",  # 0-59
       "hour": r"(?:[01]?\d|2[0-3])",  # 0-23
       "day_of_month": r"(?:[1-9]|[12]\d|3[01])",  # 1-31
       "month": r"(?:[1-9]|1[0-2])",  # 1-12
       "day_of_week": r"(?:[0-6])",  # 0-6 (Sun=0 .. Sat=6)
       }
STEP_MAX = {
    "minute": 59, "hour": 23, "day_of_month": 31, "month": 12, "day_of_week": 6
}


def parse_cron_validator(msg: str) -> Dict[str, bool]:
    """
        Orchestrator:
          - Splits 'msg' into 5 tokens
          - Calls inner validators (defined below)
          - Returns {field_name: True/False, ...}
        """

    def _valid_number_in_range(num_pat: str, s: str) -> bool:
        return R.fullmatch(num_pat, s) is not None

    def _validate_item(field_name: str, token: str) -> bool:
        """
        Validate ONE item (no commas). Allowed shapes:
          - "*"
          - "<n>"
          - "<a>-<b>"
          - "*/<step>"
          - "<a>-<b>/<step>"
        Where numbers respect the field range. Also checks:
          - step >= 1
          - a <= b  (for ranges)
        """
        num_pat = NUM[field_name]
        step_max = STEP_MAX[field_name]

        # 1) lone star
        if token == "*":
            return True

        # 2) step forms
        m = R.fullmatch(rf"\*/({num_pat})", token)
        if m:
            step = int(m.group(1))
            return 1 <= step <= step_max

        m = R.fullmatch(rf"({num_pat})-({num_pat})/({num_pat})", token)
        if m:
            a, b, step = map(int, m.groups())
            return a <= b and 1 <= step <= step_max

        # 3) pure range
        m = R.fullmatch(rf"({num_pat})-({num_pat})", token)
        if m:
            a, b = map(int, m.groups())
            return a <= b

        # 4) single number
        if _valid_number_in_range(num_pat, token):
            return True

        return False

    def _validate_list(field_name: str, field_token: str) -> bool:
        """
        Validate a possibly comma-separated token. Rule:
          - '*' is allowed only alone (not mixed in lists).
          - Otherwise, each comma-part must be a valid item by _validate_item.
        """
        # '*' alone
        if field_token == "*":
            return True

        parts = field_token.split(",")
        # reject if '*' appears inside a list (e.g., "*,5")
        if any(p == "*" for p in parts):
            return False

        return all(_validate_item(field_name, p) for p in parts)

    def minute_valid(full_msg: str, field_token: str) -> bool:
        return _validate_list("minute", field_token)

    def hour_valid(full_msg: str, field_token: str) -> bool:
        return _validate_list("hour", field_token)

    def day_month_valid(full_msg: str, field_token: str) -> bool:
        return _validate_list("day_of_month", field_token)

    def month_valid(full_msg: str, field_token: str) -> bool:
        return _validate_list("month", field_token)

    def day_week_valid(full_msg: str, field_token: str) -> bool:
        return _validate_list("day_of_week", field_token)

    """-------- Orchestration ---------"""
    tokens = msg.split()
    if len(tokens) != 5:
        return {
            "minute": False,
            "hour": False,
            "day_of_month": False,
            "month": False,
            "day_of_week": False
        }

    minute, hour, day_of_month, month, day_of_week = tokens
    final_results = {
        "minute": minute_valid(msg, minute),
        "hour": hour_valid(msg, hour),
        "day_of_month": day_month_valid(msg, day_of_month),
        "month": month_valid(msg, month),
        "day_of_week": day_week_valid(msg, day_of_week),
    }
    return final_results


def runCronTab2():
    for s in [
        "*/5 9 * * 6",  # every 5 minutes during hour 9 on Saturday
        "0 0 1 * *",  # midnight on day 1 of every month
        "15 8-10 * * 1,3,5",  # 08:15..10:15 on Mon,Wed,Fri
        "61 * * * *",  # invalid minute
        "*/0 * * * *",
        "*/5 * * *",
        "*/5 * * * * *",
        "*/5 * * * mon",
        "60 * * * *",
        "* * 0 * *",
        "10-5 * * * *",
        "*,a,5 * * * *",
        "*/5 9-17 * * 1-5",
        "0,15,30,45 0,12 * 1,6 0,6",
    ]:
        print(s, "=>", parse_cron_validator(s), "\n\n")
