from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from vraith.prompts import combine_prompt
from vraith.utils.llm import get_llm

combined_chain = (
        RunnablePassthrough() 
        | RunnableLambda(lambda x: {"text": x}) 
        | combine_prompt 
        | get_llm() 
        | StrOutputParser()
    )