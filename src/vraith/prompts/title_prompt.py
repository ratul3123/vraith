from langchain_core.prompts import ChatPromptTemplate

title_prompt = ChatPromptTemplate.from_messages([
        ("system", "Based on the audio/video transcript, generate a short professional audio/video title (max 8 words). Only return the title, nothing else."),
        ("human", "{text}"),
    ])