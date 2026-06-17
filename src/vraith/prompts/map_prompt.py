from langchain_core.prompts import ChatPromptTemplate

map_prompt = ChatPromptTemplate.from_messages([
        ("system", "Summarize this portion of a audio/video transcript concisely."),
        ("human", "{text}"),
    ])