from typing import List
import unicodedata
import re

def normalize_column_name(column_name: str) -> str:
    """
    Normalizes column names by removing non-alphanumeric characters, replacing accented letters with their ASCII equivalents, and capitalizing each word.

    Args:
        column_name (str): Column name to normalize.

    Returns:
        str: Normalized column name.
    """

    normalized = unicodedata.normalize('NFKD', column_name).encode('ASCII', 'ignore').decode('ASCII')
    normalized_column_name = re.sub(r'[^a-zA-Z0-9 ]', ' ', normalized)
    words = normalized_column_name.split()
    
    return ''.join(word.capitalize() for word in words)

def normalize_file_name(file_name: str) -> str:
    """
    Normalizes file names by replacing hyphens with underscores.

    Args:
        file_name (str): File name to normalize.

    Returns:
        str: Normalized file name.
    """
    file_name = file_name.replace('-', '_')
    file_name = file_name.replace('.csv', '')

    return file_name