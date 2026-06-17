from langchain_core.prompts import ChatPromptTemplate

combine_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert audio/video summarizer. Combine these partial summaries into one final professional audio/video summary in bullet points."),
        ("human", "{text}"),
    ])