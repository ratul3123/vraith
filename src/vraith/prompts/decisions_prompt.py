from langchain_core.prompts import ChatPromptTemplate

decisions_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "You are an expert audio/video analyst. From the audio/video transcript, "
            "extract all key decisions made. Format as a numbered list. "
            "If none found say 'No key decisions found.'"),
        ("human", "{text}"),
    ])