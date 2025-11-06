import os
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import Tool
from .rag.store import retriever
from .tools.reporting_tool import summarize_report

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

def _search_docs(q: str)->str:
    docs = retriever.get_relevant_documents(q)
    return "\n\n".join(d.page_content for d in docs[:6])

tools = [
    Tool(name="reporting_tool", description="Summarize CSV/Report semantics",
         func=summarize_report),
    Tool(name="rag_search", description="Search internal knowledge base",
         func=_search_docs),
]

def run_agent(message: str, context: dict):
    prompt = f"""You are Agent ONE analyzing enterprise reports.
Use tools if needed. Question: {message}"""
    # super lightweight “agent”: call RAG first, then LLM with context + tools summary
    rag = _search_docs(message)
    tool_hint = summarize_report(context.get("sample_report","")) if context.get("sample_report") else ""
    final = llm.invoke(f"{prompt}\n\nContext:\n{rag}\n{tool_hint}")
    trace = {"used_tools": ["rag_search"] + (["reporting_tool"] if tool_hint else [])}
    return final.content, trace
