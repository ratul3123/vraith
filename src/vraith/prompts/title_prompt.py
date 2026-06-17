from langchain_core.prompts import ChatPromptTemplate

title_prompt = ChatPromptTemplate.from_messages([
        ("system", "Based on the meeting transcript, generate a short professional meeting title (max 8 words). Only return the title, nothing else."),
        ("human", "{text}"),
    ])