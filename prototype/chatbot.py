from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.retrievers import BaseRetriever


EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
FAISS_DIR = "faiss_index"
LLM_MODEL = "gemini-2.5-flash"


def create_prompt(context: str, question: str) -> str:

    prompt = f"""
    あなたは企業分析に詳しい金融アナリストです。
    以下のコンテキストのみを根拠に回答してください。
    表形式のデータは列見出しと行見出しの対応を確認してください。
    分からない場合のみ「記載がありません」と回答してください。

    {context}

    質問:
    {question}
    """
    return prompt


def ask_question(question:str,
                 retriever:BaseRetriever,
                 llm:ChatGoogleGenerativeAI
                 ) -> str:

    docs = retriever.invoke(question)

    """ Debug: Display retrieved chunks
        for i, doc in enumerate(docs):
            print(f"===== {i} =====")
            print(doc.page_content) """

    context = "\n".join(
        doc.page_content for doc in docs
    )

    prompt = create_prompt(
        context,
        question
    )

    response = llm.invoke(prompt)

    return response.content


def main() -> None:
    """Run the RAG chatbot."""

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.load_local(
        FAISS_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL
    )

    while True:

        question = input("Question: ")

        if question.lower() == "q":
            print("chatbot finished")
            break

        answer = ask_question(
            question,
            retriever,
            llm
        )
        
        print(answer)

if __name__ == "__main__":
    main()