import streamlit as st

st.set_page_config(
    page_title="AI Lab Error Detective",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 AI Lab Error Detective")
st.write("Understand common C programming errors, one hint at a time.")

error_message = st.text_area(
    "Paste your C compiler error or describe the problem:",
    placeholder="Example: error: 'x' undeclared"
)

hints = {
    "Syntax": (
        "Check semicolons, brackets, braces, and statement structure.",
        "Is there a missing semicolon or unmatched brace near the reported line?"
    ),
    "Declaration / Type": (
        "Check variable declarations and whether the types match.",
        "Was this variable declared before you used it? Is its spelling consistent?"
    ),
    "Pointer / Memory": (
        "Check pointer initialization and whether the memory is valid.",
        "Could the pointer be NULL or point to memory that is no longer valid?"
    ),
    "Array / Index": (
        "Check array bounds and loop limits.",
        "Can your index become negative or reach the array length?"
    ),
    "Logic": (
        "Trace conditions and variable values to locate the incorrect result.",
        "What value did you expect, and what is the first step where the result differs?"
    )
}

if st.button("Detect error"):
    if len(error_message.strip()) < 5:
        st.warning("Please enter a longer error message or problem description.")
    else:
        msg = error_message.lower()

        if any(word in msg for word in [
            "semicolon", "expected ';'", "syntax error",
            "expected expression", "expected '}'"
        ]):
            category = "Syntax"
        elif any(word in msg for word in [
            "undeclared", "unknown identifier", "incompatible type",
            "conflicting types", "not declared"
        ]):
            category = "Declaration / Type"
        elif any(word in msg for word in [
            "segmentation fault", "null pointer", "invalid memory",
            "dereference", "use after free"
        ]):
            category = "Pointer / Memory"
        elif any(word in msg for word in [
            "out of bounds", "array index", "array subscript",
            "index out of range"
        ]):
            category = "Array / Index"
        elif any(word in msg for word in [
            "wrong answer", "incorrect output", "infinite loop",
            "wrong result", "logical error"
        ]):
            category = "Logic"
        else:
            category = None

        if category is None:
            st.info(
                "I'm not sure which category fits. "
                "Please share the exact compiler message and relevant C code."
            )
        else:
            explanation, hint = hints[category]
            st.subheader("Likely diagnosis")
            st.write("**Category:**", category)
            st.write("**Explanation:**", explanation)
            st.write("**Your debugging hint:**", hint)

st.caption(
    "Learning prototype: suggestions are based on common error patterns. "
    "Always verify the diagnosis against your code."
)
