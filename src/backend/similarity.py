from sentence_transformers import SentenceTransformer


class Similarity:

    def __init__(self, path_model: str):
        self.model: SentenceTransformer = SentenceTransformer(path_model)

    def test(self) -> str:
        sentences = [
            "That is a happy person",
            "That is a happy dog",
            "That is a very happy person",
            "Today is a sunny day",
        ]
        embeddings = self.model.encode(sentences)

        similarities = self.model.similarity(embeddings, embeddings)
        return str(similarities)
