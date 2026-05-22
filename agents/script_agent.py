from core.llm import LocalLLM
class ScriptAgent:
    def __init__(self):
        self.llm = LocalLLM()
    def run(self, content_idea):
        prompt = f"""
        Create:
        1. YouTube title
        2. Description
        3. Viral captions
        4. Shorts script
        5. Long video script
        6. CTA

        Topic:
        {content_idea}
        """
        
        return self.llm.generate(prompt)