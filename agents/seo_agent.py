from core.llm import LocalLLM
class SEOAgent:
    def __init__(self):
        self.llm = LocalLLM()
    def run(self, topic):
        prompt = f"""
        Generate:
        1. SEO optimized hashtags
        2. YouTube tags
        3. Search keywords
        4. Trending metadata

        Topic:
        {topic}
        """

        return self.llm.generate(prompt)