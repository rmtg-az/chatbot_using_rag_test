from fastapi import UploadFile
from pathlib import Path
import logging

UPLOAD_DIR = Path("pdf_save")
UPLOAD_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)

def save_pdf(file: UploadFile) -> Path:

    if file.content_type != "application/pdf":
        logger.warning(
            "PDF以外のファイルがアップロードされました: filename=%s content_type=%s",
            file.filename,
            file.content_type,
        )
        raise ValueError("PDFファイルをアップロードしてください。")
        
    logger.info("PDF保存開始: %s", file.filename)

    try:

        file_path = UPLOAD_DIR / file.filename

        with file_path.open("wb") as f:
            f.write(file.file.read())

        logger.info("PDF保存終了: %s", file_path)
        
        return file_path
    
    except OSError as e:
        logger.exception("PDFファイルの保存に失敗しました")
        raise RuntimeError(f"PDF保存エラー：{e}")