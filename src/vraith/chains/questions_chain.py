from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from vraith.prompts import questions_prompt
from vraith.utils.llm import get_llm

questions_chain = (
        RunnablePassthrough() 
        | RunnableLambda(lambda x: {"text": x}) 
        | questions_prompt 
        | get_llm() 
        | StrOutputParser()
    )