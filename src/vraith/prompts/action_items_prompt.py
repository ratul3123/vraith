from langchain_core.prompts import ChatPromptTemplate

action_items_prompt = ChatPromptTemplate.from_messages([
        ("system", 
            "You are an expert meeting analyst. From the meeting transcript, "
            "extract all action items. For each provide:\n"
            "- Task description\n"
            "- Owner (who is responsible)\n"
            "- Deadline (if mentioned, else write 'Not specified')\n\n"
            "Format as a numbered list. If none found say 'No action items found.'"),
        ("human", "{text}"),
    ])