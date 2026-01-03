import json
from datetime import date
import logging

logger = logging.getLogger(__name__)


def load_data():
    file_path = f"./data/Yt_data_{date.today()}.json"
    try:
        logger.info(f"processing file: YT_data_{date.today()}")
        with open(file_path, 'r', encoding='utf-8') as raw_data:
            data = json.load(raw_data)
        return data
    except FileNotFoundError:
        logger.error(f"file {file_path} not found")
        raise
    except json.decoder.JSONDecodeError:
        logger.error(f"file {file_path} not valid JSON")
        raise
