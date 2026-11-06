from lab6_search import Retriever

FAQ = [
    {
        "question": "How can I check my attendance?",
        "answer": "You can check your attendance in the student portal.",
        "source": "student_guide.txt"
    },
    {
        "question": "Where can I check my fee details?",
        "answer": "You can check your fee details in the student portal.",
        "source": "fee_guide.txt"
    }
]

records = [
    {"text": item["question"] + " " + item["answer"]}
    for item in FAQ
]

engine = Retriever(records)

def reply(query):
    if not query.strip():
        return "Please enter a question."

    for item in FAQ:
        if query.lower().strip() == item["question"].lower():
            return item["answer"] + " [Source: " + item["source"] + "]"

    results = engine.search(query)

    if results and results[0][1] > 0.5:
        return "Did you mean: " + results[0][0]["text"] + "?"

    return "Sorry, no matching FAQ was found."

print("Welcome to the FAQ Chatbot!")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    print("Bot:", reply(question))