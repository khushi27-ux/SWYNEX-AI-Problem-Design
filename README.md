# SWYNEX-AI-Problem-Design
SWYNEX – AI Problem Design

Project Title: AI Lab Error Detective

1. Problem Statement

Beginner engineering students often struggle to understand C programming errors and identify the cause of a problem. Compiler messages can be confusing, especially for students who are learning programming fundamentals.

AI Lab Error Detective is a proposed AI solution that classifies common beginner C programming errors and provides a short, actionable debugging hint to help students learn how to solve problems independently.

2. Target User

- First- and second-year engineering students learning C programming.
- Beginners who need help understanding compiler errors and common coding mistakes.

3. Data Source

The proposed system will use a small labelled dataset of approximately 100–150 examples of common C programming errors.

Each example will contain:

- Error message or short description
- Error category
- Brief explanation
- Suggested debugging hint
- Source or reference, where applicable

Examples will be created and verified using common C programming mistakes, compiler documentation, and reputable learning resources.

4. AI Approach

The initial version will use text classification to categorize error descriptions into five categories:

1. Syntax errors
2. Declaration and type errors
3. Pointer and memory errors
4. Array and index errors
5. Logic errors

A simple baseline such as TF-IDF with Logistic Regression can be explored. The predicted category will be connected to a reviewed collection of debugging hints.

If the input is unclear or the model is uncertain, the system should ask for more information rather than provide an unreliable answer.

5. Constraints

- The initial dataset will cover only common beginner C programming errors.
- Some error messages may have multiple possible causes.
- Incorrect hints could mislead students, so the explanations must be reviewed.
- The system should encourage learning instead of providing complete assignment solutions.
- Personal information and private student code should not be collected unnecessarily.
- The system must acknowledge uncertainty and its limitations.

6. Evaluation Approach

The proposed system will be evaluated using unseen test examples.

The evaluation will include:

- Classification accuracy: Percentage of error examples assigned to the correct category.
- Macro F1-score: Measures classification performance across all error categories.
- Hint usefulness: Human review of whether the debugging hints are relevant and actionable.
- Uncertainty handling: Tests whether the system requests clarification for ambiguous inputs.

7. Success Criteria

Initial proposed targets are:

- At least 80% classification accuracy on a held-out test set.
- An average hint usefulness rating of at least 4 out of 5 from reviewers.
- Appropriate clarification requests when inputs are ambiguous.

These are target values, not achieved results. Actual performance will be reported only after implementation and testing.

8. Expected Outcome

The proposed solution aims to help beginner programmers understand common C errors, identify what to investigate next, and develop independent debugging skills.

9. Current Project Status

This repository documents the AI problem definition, proposed data requirements, constraints, approach, and evaluation plan for the SWYNEX AI Problem Design task. Implementation and experimental evaluation are future steps.

---

Task: AI Problem Design
Organization: SWYNEX Technologies
Domain: Artificial Intelligence and Machine Learning