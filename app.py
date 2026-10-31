import streamlit as st
import pickle
from pathlib import Path

st.set_page_config(
    page_title="AI Lab Error Detective",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 AI Lab Error Detective")
st.caption("A beginner-friendly C programming debugging assistant")

st.info(
    "Paste a C compiler error or describe your program's problem. "
    "The assistant suggests a likely category and a debugging hint."
)

model_path = Path(__file__).parent / "error_model.pkl"

hints = {
    "Syntax Error": (
        "The code may not follow C's grammar.",
        "Check semicolons, brackets, braces, and parentheses."
    ),
    "Declaration/Type Error": (
        "A variable or data type may be undeclared or incompatible.",
        "Check variable spelling, declarations, and data types."
    ),
    "Pointer/Memory Error": (
        "The problem may involve invalid pointer or memory use.",
        "Check pointer initialization, memory access, and allocation."
    ),
    "Array/Index Error": (
        "The code may access an invalid array position.",
        "Check array bounds and loop starting and ending values."
    ),
    "Logic Error": (
        "The program may run but produce an unexpected result.",
        "Trace the variables and conditions using a small example."
    ),
}

if not model_path.exists():
    st.error("The trained model is missing. Run train_model.py first.")
    st.stop()

try:
    with model_path.open("rb") as file:
        model = pickle.load(file)
except Exception as error:
    st.error(f"Could not load the trained model: {error}")
    st.stop()

problem = st.text_area(
    "Enter your C error message or problem",
    placeholder="Example: error: 'total' undeclared",
    height=130
)

if st.button("🔎 Analyse error", type="primary"):
    cleaned_problem = problem.strip()
    lower_problem = cleaned_problem.lower()

    if not cleaned_problem:
        st.warning("Please enter an error message first.")

    elif len(cleaned_problem) < 12:
        st.warning(
            "I need a little more information. "
            "Paste the exact compiler error or a short code snippet."
        )

    elif lower_problem in {
        "it doesn't work",
        "it does not work",
        "my code is wrong",
        "help me"
    }:
        st.info(
            "Could you share the exact compiler message, "
            "the relevant C code, and what output you expected?"
        )

    else:
        try:
            category = model.predict([cleaned_problem])[0]

            st.subheader("Likely diagnosis")
            st.write(f"**Category:** {category}")

            if category in hints:
                explanation, hint = hints[category]

                st.write("**What it might mean**")
                st.write(explanation)

                st.write("**Your debugging hint**")
                st.success(hint)

                st.write("**Question to investigate**")
                st.write(
                    "What part of your code could cause this symptom?"
                )
            else:
                st.warning(
                    "The model returned an unfamiliar category. "
                    "Please check your training labels."
                )

            st.caption(
                "This is a small prototype. Predictions may be incorrect, "
                "especially for unfamiliar or ambiguous inputs. "
                "Always verify against your compiler and code."
            )

        except Exception as error:
            st.error(f"Prediction failed: {error}")

st.divider()
st.caption("AI Lab Error Detective | Learning through debugging")