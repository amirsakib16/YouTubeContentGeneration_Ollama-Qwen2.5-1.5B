import ollama
class LocalLLM:
    def __init__(self, model="qwen2.5:1.5b"):
        self.model = model
    def generate(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]