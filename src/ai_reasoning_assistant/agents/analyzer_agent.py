import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

class AnalyzerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.3)
        self.template = PromptTemplate(
            input_variables=["context", "query"],
            template=(
                "You are an analytical reasoning agent. "
                "Given the context below, reason step-by-step to answer the query.\n\n"
                "Context:\n{context}\n\n"
                "Query:\n{query}\n\n"
                "Answer with reasoning:\n"
            )
        )

    def analyze(self, query, context):
        prompt = self.template.format(context=context, query=query)
        return self.llm.predict(prompt)
