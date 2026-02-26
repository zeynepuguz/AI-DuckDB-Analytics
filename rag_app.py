import os
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import CondensePlusContextChatEngine


def main() -> None:
    # 1) Load environment variables (.env)
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Put it in .env as OPENAI_API_KEY=...")

    # 2) Configure LLM + Embeddings
    Settings.llm = OpenAI(model="gpt-4o", api_key=api_key)
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

    # 3) Load documents (only .txt files from ./data)
    documents = SimpleDirectoryReader("data", required_exts=[".txt"]).load_data()
    if not documents:
        raise ValueError("No .txt documents found in ./data (add notes.txt etc.)")

    # 4) Build in-memory vector index
    index = VectorStoreIndex.from_documents(documents)

    # 5) Memory + Chat Engine (keeps conversation history)
    memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
    chat_engine = CondensePlusContextChatEngine.from_defaults(
        retriever=index.as_retriever(similarity_top_k=3),
        memory=memory,
        llm=Settings.llm,
    )

    # (Optional) quick smoke test
    test_q = "What is this project about?"
    test_resp = chat_engine.chat(test_q)
    print("\nTest Answer:\n")
    print(test_resp.response)

    # 6) Interactive chat loop
    print("\nRAG chat ready. Ask a question (type 'exit' to quit).")

    while True:
        q = input("\n> ").strip()
        if q.lower() in {"exit", "quit"}:
            break

        resp = chat_engine.chat(q)

        print("\nAnswer:\n")
        print(resp.response)

        # 7) Show sources
        print("\nSources:")
        if getattr(resp, "source_nodes", None):
            for i, node in enumerate(resp.source_nodes, start=1):
                meta = node.node.metadata or {}
                file_name = (
                    meta.get("file_name")
                    or meta.get("filename")
                    or meta.get("file_path")
                    or "unknown"
                )
                score = getattr(node, "score", None)

                text = node.node.get_text()
                snippet = " ".join(text.split())[:200]

                if score is not None:
                    print(f"{i}) {file_name} (score={score:.3f})")
                else:
                    print(f"{i}) {file_name}")

                print(f"   snippet: {snippet}...\n")
        else:
            print("No sources returned.\n")


if __name__ == "__main__":
    main()