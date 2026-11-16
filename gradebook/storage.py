import json, logging
from pathlib import Path

DEFAULT_PATH = "data/gradebook.json"
logger = logging.getLogger(__name__)

def load_data(path=DEFAULT_PATH):
    try:
        with open(path) as f:
            data = json.load(f)
        logger.info("Data loaded from %s", path)
        return data
    except FileNotFoundError:
        logger.info("File not found, starting empty")
        return{"students": [], "courses": [], "enrollments": []}
    except json.JSONDecodeError:
        logger.error("Corrupted JSON file in %s", path)
        print("The data file is damaged ")
        raise

def save_data(data, path= DEFAULT_PATH):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path,"w") as f:
        json.dump(data, f, indent=2)
    logger.info("Data saved to %s", path)
