from crewai import Agent, Task, Crew
from agents.retriever_agent import RetrieverAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.summarizer_agent import SummarizerAgent
from agents.evaluator_agent import EvaluatorAgent

class OrchestratorAgent:
    def __init__(self):
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.summarizer = SummarizerAgent()
        self.evaluator = EvaluatorAgent()

    def run_pipeline(self, query):
        context = self.retriever.retrieve(query)
        reasoning = self.analyzer.analyze(query, context)
        summary = self.summarizer.summarize(reasoning)
        eval_feedback = self.evaluator.evaluate(summary)

        return {
            "query": query,
            "summary": summary,
            "reasoning": reasoning,
            "evaluation": eval_feedback
        }
