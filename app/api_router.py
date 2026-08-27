from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from pdf_save import save_pdf
from rag import create_vectorstore
from chatbot import ask_question, load_chatbot
from json_save import save_chat_log

import logging


logger = logging.getLogger(__name__)

router = APIRouter()


class UploadResponse(BaseModel):
    message: str

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str


@router.post(
    "/upload",
    response_model=UploadResponse
)
def upload_pdf(file: UploadFile = File(...)) -> UploadResponse:

    logger.info("PDFアップロード開始")

    try:  

        pdf_path = save_pdf(file)

        create_vectorstore(pdf_path)

        logger.info("PDFアップロード処理終了")

        return UploadResponse(
            message="PDFの登録が完了しました"
        )
    
    except ValueError as e:
        logger.warning(f"入力エラー: {e}")
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except RuntimeError as e:
        logger.exception("PDF登録処理に失敗しました")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    except Exception:
        logger.exception("予期しないエラーが発生しました")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    
@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest) -> ChatResponse:

    logger.info("チャット処理開始")

    try:

        retriever, llm = load_chatbot()

        answer = ask_question(
            request.question,
            retriever,
            llm
        )

        save_chat_log(
            request.question,
            answer
        )

        logger.info("チャット処理終了")

        return ChatResponse(
            answer=answer
        )

    except RuntimeError as e:
        logger.exception("チャット処理に失敗しました")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    except Exception:
        logger.exception("予期しないエラーが発生しました")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )