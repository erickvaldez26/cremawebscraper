import logging
from pathlib import Path

LOG_PATH = Path("data/logs")
LOG_PATH.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
  filename=LOG_PATH / "scraper.log",
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)