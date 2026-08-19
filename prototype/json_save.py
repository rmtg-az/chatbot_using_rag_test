from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)

OUTPUT_DIR = Path("output_json")
OUTPUT_DIR.mkdir(exist_ok=True)

def save_chat_log(question: str, answer: str) -> None:

    output_path = OUTPUT_DIR / "result.json"
    
    logger.info("JSON保存開始: %s", output_path)

    data = {
        "question": question,
        "answer": answer
    }

    try:     

        if output_path.exists():
            with output_path.open("r", encoding="utf-8") as f:
                logs = json.load(f)

            if isinstance(logs, dict):
                logs = [logs]

        else:
            logs = []

        logs.append(data)

        with output_path.open("w",encoding="utf-8") as f:
            json.dump(
                logs,
                f,
                ensure_ascii=False,
                indent=2
            )

        logger.info("JSON保存終了: %s", output_path)

    except (OSError, json.JSONDecodeError) as e:
        logger.exception("JSONファイルの保存に失敗しました")
        raise RuntimeError(f"JSON保存エラー：{e}")