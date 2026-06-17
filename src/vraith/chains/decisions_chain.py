from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from vraith.prompts import decisions_prompt
from vraith.utils.llm import get_llm

decisions_chain = (
        RunnablePassthrough() 
        | RunnableLambda(lambda x: {"text": x}) 
        | decisions_prompt 
        | get_llm() 
        | StrOutputParser()
    )