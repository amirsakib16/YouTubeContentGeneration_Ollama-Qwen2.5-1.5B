from core.llm import LocalLLM
class StrategistAgent:
    def __init__(self):
        self.llm = LocalLLM()
    def run(self, trends):
        prompt = f"""
        You are a YouTube content strategist.

        Based on these trending topics:
        {trends}

        Generate:
        1. Viral video ideas
        2. Shorts ideas
        3. Audience targeting
        4. Hook ideas
        5. Thumbnail concepts
        """

        return self.llm.generate(prompt)