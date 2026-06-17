from langchain_core.output_parsers import StrOutputParser
from vraith.prompts import map_prompt
from vraith.utils.llm import get_llm

map_chain = map_prompt | get_llm() | StrOutputParser()