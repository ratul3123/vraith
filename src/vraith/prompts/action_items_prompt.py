from langchain_core.prompts import ChatPromptTemplate

action_items_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "You are an expert audio/video analyst. From the audio/video transcript, "
            "extract all action items. For each provide:\n"
            "- Task description\n"
            "- Owner (who is responsible)\n"
            "- Deadline (if mentioned, else write 'Not specified')\n\n"
            "Format as a numbered list. If none found say 'No action items found.'"),
        ("human", "{text}"),
    ])