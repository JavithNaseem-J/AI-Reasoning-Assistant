from langchain.prompts import PromptTemplate

# Base reasoning prompt
reasoning_prompt = PromptTemplate(
    input_variables=["context", "query"],
    template=(
        "You are an AI reasoning assistant. "
        "Given the context below, reason carefully and logically step by step to answer the query.\n\n"
        "Context:\n{context}\n\nQuery:\n{query}\n\nReasoning:"
    )
)

# Summarization prompt
summary_prompt = PromptTemplate(
    input_variables=["analysis"],
    template="Summarize the following reasoning into a clear, concise answer:\n{analysis}\n\nFinal Answer:"
)

# Evaluation prompt
evaluation_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Evaluate the factual correctness of this answer and return a confidence score (0-1):\n{summary}"
)
