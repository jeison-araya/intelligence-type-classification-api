"""
Utility functions
"""
import os
from dotenv import load_dotenv

load_dotenv()


def getenv(name: str) -> str:
    """
    Get environment variable

    Args:
        name(str): Name of the environment variable
    """
    value = os.getenv(name)

    if not value:
        raise ValueError(f'{name} environment variable is missing.')

    return value


def get_origins() -> list[str]:
    """
    Get origins allowed from environment variables
    """
    origins = getenv('ALLOW_ORIGINS')
    return origins.strip().split(',')
