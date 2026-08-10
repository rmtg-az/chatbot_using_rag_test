from rag import create_vectorstore
from pathlib import Path

PDF_FILE = "140120260507517486.pdf"

def main() -> None:
    # Create a vector store from the target PDF.

    base_dir = Path(__file__).resolve().parent.parent
    pdf_path = base_dir / "data" / PDF_FILE

    create_vectorstore(pdf_path)

    print("Vector store created successfully.")

if __name__ == "__main__":
    main()