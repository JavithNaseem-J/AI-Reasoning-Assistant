from agents.retriever_agent import RetrieverAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.summarizer_agent import SummarizerAgent
from agents.evaluator_agent import EvaluatorAgent

class RAGPipeline:
    def __init__(self):
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.summarizer = SummarizerAgent()
        self.evaluator = EvaluatorAgent()

    def run(self, query):
        context = self.retriever.retrieve(query)
        analysis = self.analyzer.analyze(query, context)
        summary = self.summarizer.summarize(analysis)
        evaluation = self.evaluator.evaluate(summary)
        return {
            "query": query,
            "summary": summary,
            "analysis": analysis,
            "evaluation": evaluation
        }
