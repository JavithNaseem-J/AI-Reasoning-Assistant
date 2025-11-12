from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class SummarizerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.5)
        self.template = PromptTemplate(
            input_variables=["analysis"],
            template="Summarize the reasoning below into a clear, concise answer:\n{analysis}\n\nFinal Answer:"
        )

    def summarize(self, analysis):
        return self.llm.predict(self.template.format(analysis=analysis))
