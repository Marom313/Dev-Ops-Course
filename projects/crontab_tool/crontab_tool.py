import argparse
from typing import Dict, List, Set, Tuple

# this will define the ranges of the values.
FIELD_RANGES_SCHEMA: Dict[str, tuple[int, int]] = {
    "minute": (0, 59),
    "hour": (0, 23),
    "day_of_month": (1, 31),
    "month": (1, 12),
    "day_of_week": (0, 6),
}


def parse_field(token: str, lo: int, hi: int) -> Tuple[Set[int], List[str]]:
    # errors data structure
    errors: List[str] = []

    def add_number(n_str: str, bag: Set[int]):
        if not n_str.isdigit():
            errors.append(f"number {n_str} is not a digit")
            return
        n = int(n_str)
        if not (n >= lo and n <= hi):
            errors.append(f"number {n_str} is out of range")
            return
        bag.add(n)

    #     "*" -> full range
    if token == "*":
        return set(range(lo, hi + 1)), errors

    values: Set[int] = set()
    parts = token.split(",")

    for part in parts:
        # step syntax
        if "/" in part:
            left, step_str = part.split("/", 1)
            if not step_str.isdigit():
                errors.append(f"Invalid step: {step_str}")
                continue
            step = int(step_str)
            if step <= 0:
                errors.append("Step must be > 0")
                continue
            if left == "*":
                start, end = lo, hi
            elif "-" in left:
                a, b = left.split("-", 1)
                if not (a.isdigit() and b.isdigit()):
                    errors.append(f"Invalid range in step: {left}")
                    continue
                start, end = int(a), int(b)
                if start > end:
                    errors.append(f"Range start > end: {left}")
                    continue
                if start < lo or end > hi:
                    errors.append(f"Range {start}-{end} out of [{lo}..{hi}]")
                    continue
            else:
                errors.append(f"Invalid stepped pattern: {part}")
                continue

            for n in range(start, end + 1, step):
                if lo <= n <= hi:
                    values.add(n)
                else:
                    errors.append(f"Value {n} out of [{lo}..{hi}]")
            # range syntax
        elif "-" in part:
            a, b = part.split("-", 1)
            if not (a.isdigit() and b.isdigit()):
                errors.append(f"Invalid range: {part}")
                continue
            start, end = int(a), int(b)
            if start > end:
                errors.append(f"Range start > end: {part}")
                continue
            if start < lo or end > hi:
                errors.append(f"Range {start}-{end} out of [{lo}..{hi}]")
                continue
            for n in range(start, end + 1):
                values.add(n)

            # single number
        else:
            add_number(part, values)

    return values, errors


def print_cron(s: str, dic: Dict) -> None:
    def prin_false(B: bool):
        print("\n\n")
        print("Validation: ", B)
        print("Error: Not valid dictionary.")
        print("\n\n")

    valid = dic["valid"]
    errors: List[str] = dic["errors"]
    if not valid:
        return prin_false(valid)
    else:
        print("User input: ", s)
        print("Validation: ", valid)
        print("Errors: ", errors) if errors else print("Errrs: No errors.")
        print("Minutes: ", dic['fields']['minute']) if len(dic['fields']['minute']) > 1 else print("Minute: ",
                                                                                                   dic['fields'][
                                                                                                       'minute'])
        print("Hours: ", dic['fields']['hour']) if len(dic['fields']['hour']) > 1 else print("Hour: ",
                                                                                             dic['fields']['hour'])
        print("Days in a month: ", dic['fields']['day_of_month']) if len(dic['fields']['day_of_month']) > 1 else print(
            "Day in a month: ", dic['fields']['day_of_month'])
        print("Months: ", dic['fields']['month']) if len(dic['fields']['month']) > 1 else print("Month: ",
                                                                                                dic['fields']['month'][
                                                                                                    0])
        print("Days in a week: ", dic['fields']['day_of_week']) if len(dic['fields']['day_of_week']) > 1 else print(
            "Day in the week: ", dic['fields']['day_of_week'])


def parse_cron(expr: str) -> Dict:
    errors: List[str] = []
    tokens = expr.split()
    if len(tokens) != 5:
        return {"valid": False, "errors": [f"Expected 5 fields, got {len(tokens)}"]}

    names = ["minute", "hour", "day_of_month", "month", "day_of_week"]
    fields: Dict[str, Set[int]] = {}

    for name, token in zip(names, tokens):
        lo, hi = FIELD_RANGES_SCHEMA[name]
        vals, errs = parse_field(token, lo, hi)
        if errs:
            # pin errors to the field for clarity
            errors.extend([f"{name}: {e}" for e in errs])
        else:
            fields[name] = vals

    if errors:
        return {"valid": False, "errors": errors}

    return print_cron(expr, {"valid": True, "errors": [], "fields": fields})


def runCronTab():
    for s in [
        # "*/5 9 * * 6",  # every 5 minutes during hour 9 on Saturday
        # "0 0 1 * *",  # midnight on day 1 of every month
        # "15 8-10 * * 1,3,5",  # 08:15..10:15 on Mon,Wed,Fri
        # "61 * * * *",  # invalid minute
        # "*/0 * * * *",
        # "*/5 * * *",
        # "*/5 * * * * *",
        "*/5 * * * mon",
        # "60 * * * *",
        # "* * 0 * *",
        # "10-5 * * * *",
        # "*,a,5 * * * *",
        # "*/5 9-17 * * 1-5",
        # "0,15,30,45 0,12 * 1,6 0,6",
    ]:
        res = parse_cron(s)
        print_cron(s, res)  # <-- always print the result
        print("-" * 40)
