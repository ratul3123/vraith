from langchain_core.prompts import ChatPromptTemplate

combine_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert meeting summarizer. Combine these partial summaries into one final professional meeting summary in bullet points."),
        ("human", "{text}"),
    ])