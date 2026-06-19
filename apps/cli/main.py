from vraith.pipelines.video_analysis_pipeline import run_pipeline
from vraith.services.rag.rag_engine import ask_questions

def main():
    source = input("Enter YouTube URL or local file path: ").strip()
    language = input("Language (english/banglish): ").strip() or "english"
    
    result = run_pipeline(source, language)

    print("\n" + "=" * 50)
    print(f"📌 TITLE: {result['title']}")
    print(f"\n📋 SUMMARY:\n{result['summary']}")
    print(f"\n✅ ACTION ITEMS:\n{result['action_items']}")
    print(f"\n🔑 KEY DECISIONS:\n{result['key_decisions']}")
    print(f"\n❓ OPEN QUESTIONS:\n{result['open_questions']}")
    print("=" * 60)

    print("\n💬 Chat with your video context (type 'exit', 'quit' or 'q' to break)\n")
    rag_chain = result["rag_chain"]
    
    while True:
        question = input("You: ").strip()
        if question.lower() in ["exit", "quit", "q"]:
            print("Session terminated!")
            break
        if not question:
            continue
            
        answer = ask_questions(rag_chain, question)
        print(f"\nAssistant:\n{answer}\n")

if __name__ == "__main__":
    main()