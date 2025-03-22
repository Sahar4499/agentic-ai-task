class Finder:
    def getData(self):
        return [
            "AI Agents",
            "Deep Learning",
            "Machine Learning",
            "Generative AI",
            "Computer Vision",
            "Transformers",
            "Natural Language Processing"
        ]

    def find(self, topics):
        for topic in topics:
            if "AI" in topic:
                print(topic)