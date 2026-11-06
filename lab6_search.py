from sklearn.feature_extraction.text import TfidfVectorizer

class Retriever:
    def __init__(self, records):
        self.records = records
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(
            [r["text"] for r in records]
        )

    def search(self, query, k=3):
        if not query.strip():
            return []

        q = self.vectorizer.transform([query])
        scores = (q @ self.matrix.T).toarray()[0]

        order = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        return [
            (self.records[i], float(scores[i]))
            for i in order[:k]
        ]