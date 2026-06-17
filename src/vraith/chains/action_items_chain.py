from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from vraith.prompts import action_items_prompt
from vraith.utils.llm import get_llm

action_items_chain = (
        RunnablePassthrough() 
        | RunnableLambda(lambda x: {"text": x}) 
        | action_items_prompt 
        | get_llm() 
        | StrOutputParser()
    )