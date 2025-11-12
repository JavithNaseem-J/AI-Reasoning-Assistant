from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

class EvaluatorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0)
        self.template = PromptTemplate(
            input_variables=["summary"],
            template=(
                "Evaluate the following answer for factual accuracy and completeness. "
                "Return a confidence score (0–1) and short feedback.\n\nAnswer:\n{summary}"
            )
        )

    def evaluate(self, summary):
        result = self.llm.predict(self.template.format(summary=summary))
        return result
