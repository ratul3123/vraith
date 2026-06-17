from langchain_core.prompts import ChatPromptTemplate

questions_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "From the audio/video transcript, extract all unresolved questions "
            "or topics needing follow-up. Format as a numbered list. "
            "If none found say 'No open questions found.'"),
        ("human", "{text}"),
    ])