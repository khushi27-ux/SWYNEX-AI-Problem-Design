from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
from pathlib import Path

# Small starter dataset for our prototype.
# We'll expand and improve it after the first test.
examples = [
    ("expected ; before printf", "Syntax Error"),
    ("missing semicolon at end of statement", "Syntax Error"),
    ("expected } at end of input", "Syntax Error"),
    ("missing closing parenthesis", "Syntax Error"),
    ("undeclared variable total", "Declaration/Type Error"),
    ("variable x was not declared", "Declaration/Type Error"),
    ("incompatible types when assigning", "Declaration/Type Error"),
    ("unknown type name Student", "Declaration/Type Error"),
    ("dereferencing a null pointer", "Pointer/Memory Error"),
    ("segmentation fault after using pointer", "Pointer/Memory Error"),
    ("invalid memory access through pointer", "Pointer/Memory Error"),
    ("free called twice on same pointer", "Pointer/Memory Error"),
    ("array index out of bounds", "Array/Index Error"),
    ("accessing element at index 10 in array of size 5", "Array/Index Error"),
    ("loop reads beyond array length", "Array/Index Error"),
    ("wrong array index in loop", "Array/Index Error"),
    ("program runs but calculates wrong sum", "Logic Error"),
    ("loop executes one extra time", "Logic Error"),
    ("condition is reversed and result is wrong", "Logic Error"),
    ("program output is incorrect despite compiling", "Logic Error"),
]

texts = [text for text, label in examples]
labels = [label for text, label in examples]

X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels,
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Evaluation on a tiny held-out starter set:")
print(classification_report(y_test, predictions, zero_division=0))

# Save the trained model locally.
output_path = Path("error_model.pkl")
with output_path.open("wb") as file:
    pickle.dump(model, file)

print(f"\nModel saved to: {output_path.resolve()}")
print("This is a starter prototype, not a validated production model.")