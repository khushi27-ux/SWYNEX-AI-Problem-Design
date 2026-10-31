import streamlit as st

st.set_page_config(
    page_title="AI Lab Error Detective",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 AI Lab Error Detective")
st.write(
    "An intelligent debugging assistant that helps "
    "beginners understand common C programming errors."
)

# 1. Error knowledge base
ERROR_PATTERNS = {
    "Syntax": [
        "semicolon", "expected ';'", "syntax error",
        "expected expression", "expected '}'",
        "expected ';' before"
    ],
    "Declaration / Type": [
        "undeclared", "unknown identifier",
        "incompatible type", "conflicting types",
        "not declared", "implicit declaration"
    ],
    "Pointer / Memory": [
        "segmentation fault", "null pointer",
        "invalid memory", "dereference",
        "use after free", "double free"
    ],
    "Array / Index": [
        "out of bounds", "array index",
        "array subscript", "index out of range",
        "subscript out of range"
    ],
    "Logic": [
        "wrong answer", "incorrect output",
        "infinite loop", "wrong result",
        "logical error", "unexpected output"
    ]
}

HINTS = {
    "Syntax": (
        "A possible syntax error was detected.",
        "Check semicolons, brackets, braces and statement structure.",
        "Is there a missing semicolon or unmatched brace?"
    ),
    "Declaration / Type": (
        "A declaration or data type problem was detected.",
        "Check variable declarations, spelling and data types.",
        "Was the variable declared before it was used?"
    ),
    "Pointer / Memory": (
        "A possible pointer or memory problem was detected.",
        "Check pointer initialization and memory validity.",
        "Could the pointer be NULL or refer to freed memory?"
    ),
    "Array / Index": (
        "A possible array indexing problem was detected.",
        "Check array boundaries and loop conditions.",
        "Can the index exceed the valid array range?"
    ),
    "Logic": (
        "A possible logical error was detected.",
        "Trace the conditions and values used in your program.",
        "At which step does the actual output differ from the expected output?"
    )
}


# 2. Intelligent classification
def detect_error(message):

    message = message.lower()

    scores = {}

    for category, keywords in ERROR_PATTERNS.items():

        matches = [
            word for word in keywords
            if word in message
        ]

        if matches:
            scores[category] = len(matches)

    if not scores:
        return None, 0, []

    best_category = max(scores, key=scores.get)

    # Avoid pretending that an ambiguous result is certain
    if len(scores) > 1 and scores[best_category] == max(
        scores.values()
    ):
        return None, 0, []

    match_count = scores[best_category]

    # Heuristic match score, not statistical probability
    confidence = min(95, 65 + (match_count - 1) * 10)

    matched_keywords = [
        word for word in ERROR_PATTERNS[best_category]
        if word in message
    ]

    return best_category, confidence, matched_keywords


# 3. Evaluation dataset
TEST_CASES = [
    ("error: expected ';' before return", "Syntax"),
    ("syntax error near expected expression", "Syntax"),
    ("error: x undeclared", "Declaration / Type"),
    ("unknown identifier total", "Declaration / Type"),
    ("segmentation fault", "Pointer / Memory"),
    ("invalid memory access", "Pointer / Memory"),
    ("array index out of bounds", "Array / Index"),
    ("array subscript is out of range", "Array / Index"),
    ("wrong answer in output", "Logic"),
    ("infinite loop detected", "Logic")
]


# 4. Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a feature",
    ["Error Detective", "Evaluation Dashboard"]
)


if page == "Error Detective":

    st.header("Find your programming error")

    error_message = st.text_area(
        "Paste your C compiler error or describe the problem:",
        placeholder="Example: error: 'x' undeclared"
    )

    if st.button("Detect Error", type="primary"):

        try:

            if len(error_message.strip()) < 5:

                st.warning(
                    "Please enter a longer error message."
                )

            else:

                category, confidence, matched = detect_error(
                    error_message
                )

                if category is None:

                    st.info(
                        "Unable to identify a clear category. "
                        "Please provide the exact compiler error "
                        "and relevant C code."
                    )

                else:

                    explanation, suggestion, question = HINTS[
                        category
                    ]

                    st.subheader("Diagnosis Results")

                    st.success(f"Category: {category}")

                    st.write("**Explanation:**", explanation)

                    st.write(
                        "**Debugging suggestion:**",
                        suggestion
                    )

                    st.write(
                        "**Think about:**",
                        question
                    )

                    st.progress(confidence / 100)

                    st.write(
                        f"Rule-based match score: {confidence}%"
                    )

                    st.caption(
                        "Matched patterns: "
                        + ", ".join(matched)
                    )

        except Exception as e:

            st.error(
                "An unexpected error occurred. "
                "Please try again."
            )


elif page == "Evaluation Dashboard":

    st.header("System Evaluation")

    st.write(
        "Test the error detector against known examples "
        "to measure its performance."
    )

    correct = 0
    results = []

    for message, expected in TEST_CASES:

        predicted, confidence, matched = detect_error(message)

        passed = predicted == expected

        if passed:
            correct += 1

        results.append({
            "Input": message,
            "Expected": expected,
            "Predicted": predicted or "Unknown",
            "Result": "Pass" if passed else "Fail"
        })

    total = len(TEST_CASES)

    accuracy = (correct / total) * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Tests", total)
    col2.metric("Correct", correct)
    col3.metric("Accuracy", f"{accuracy:.1f}%")

    st.progress(accuracy / 100)

    st.subheader("Test Results")

    st.dataframe(
        results,
        use_container_width=True
    )

    if accuracy == 100:

        st.success("All evaluation examples passed.")

    else:

        st.warning(
            "Some examples failed. Review the classification rules."
        )


# 5. User feedback
st.divider()

st.subheader("Was this tool helpful?")

feedback = st.radio(
    "Your feedback",
    ["Helpful", "Partially helpful", "Not helpful"],
    horizontal=True
)

if st.button("Submit Feedback"):

    st.success("Thank you! Your feedback has been recorded "
               "for this session.")


st.caption(
    "AI Lab Error Detective | SWYNEX AI Internship | "
    "Educational prototype. Always verify suggestions "
    "against your actual C program."
)