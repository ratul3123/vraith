from vraith.chains.action_items_chain import action_items_chain
from vraith.chains.decisions_chain import decisions_chain
from vraith.chains.questions_chain import questions_chain

def extract_action_items(transcript: str) -> str:
    return action_items_chain.invoke(transcript)

def extract_decisions(transcript: str) -> str:
    return decisions_chain.invoke(transcript)

def extract_questions(transcript: str) -> str:
    return questions_chain.invoke(transcript)