def rule_based(score, documents_complete, attendance, form_verified):
    if (score >= 70 and documents_complete
            and attendance >= 75 and form_verified):
        return "Review"
    else:
        return "Hold"


tests = [
    {
        "name": "Pass",
        "input": (82, True, 80, True),
        "expected": "Review",
        "reason": "All four conditions are satisfied."
    },
    {
        "name": "Attendance Failure",
        "input": (82, True, 70, True),
        "expected": "Hold",
        "reason": "Attendance is below 75%."
    },
    {
        "name": "Form Verification Failure",
        "input": (82, True, 80, False),
        "expected": "Hold",
        "reason": "The application form is not verified."
    },
    {
        "name": "Threshold Boundary",
        "input": (70, True, 75, True),
        "expected": "Review",
        "reason": "Score and attendance meet their minimum limits."
    }
]

for test in tests:
    score, documents, attendance, verified = test["input"]
    actual = rule_based(score, documents, attendance, verified)

    print("\nTest:", test["name"])
    print("Input:", test["input"])
    print("Expected:", test["expected"])
    print("Actual:", actual)
    print("Reason:", test["reason"])