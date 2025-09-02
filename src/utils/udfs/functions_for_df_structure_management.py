from typing import List
from pyspark.sql import DataFrame
from pyspark.sql.types import StringType
from pyspark.sql.functions import col, regexp_replace, sum
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

def cast_columns_to_float(dataframe_to_cast: DataFrame, exclude_columns: List[str] = []) -> DataFrame:
    """
    Casts all string columns in the DataFrame to float, except those specified in exclude_columns.

    Args:
        dataframe_to_cast (DataFrame): Input DataFrame with string columns.
        exclude_columns (List[str]): List of column names to exclude from casting.

    Returns:
        DataFrame: DataFrame with string columns cast to float, excluding specified columns.
    """
    for column in dataframe_to_cast.columns:
        dataframe_to_cast = dataframe_to_cast.withColumn(column, regexp_replace(col(column), ',', '.'))

    string_columns = [field.name for field in dataframe_to_cast.schema.fields if field.dataType == StringType()]
    string_columns = [col for col in string_columns if col not in exclude_columns]

    for column in string_columns:
        dataframe_to_cast = dataframe_to_cast.withColumn(column, col(column).cast("double"))

    return dataframe_to_cast

def rename_columns_with_df_name(df_to_rename: DataFrame, df_name: str, exclusion_list: List[str] = []) -> DataFrame:
    """
    Renames columns in the DataFrame by appending the DataFrame name, except those specified in exclusion_list.

    Args:
        df_to_rename (DataFrame): Input DataFrame with columns to rename.
        df_name (str): Name to append to each column.
        exclusion_list (List[str]): List of column names to exclude from renaming.

    Returns:
        DataFrame: DataFrame with columns renamed by appending the DataFrame name, excluding specified columns.
    """
    for col in df_to_rename.columns:
        if col not in exclusion_list:
            df_to_rename = df_to_rename.withColumnRenamed(col, f"{col}{df_name}")

    return df_to_rename

def count_nulls(df: DataFrame) -> DataFrame:
    """
    Counts the number of null values in each column of the DataFrame.

    Args:
        df (DataFrame): Input DataFrame to count nulls in.

    Returns:
        DataFrame: DataFrame with a single row containing the count of nulls for each column.
    """
    null_counts = df.select([sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])

    return null_counts

def fill_nulls(df: DataFrame, exclude_columns: List[str] = []) -> DataFrame:
    """
    Fills null values with 0 in columns not in the exclusion list.

    Args:
        df (DataFrame): Input DataFrame to count nulls in.
        exclude_columns (List[str]): List of column names to exclude from operations.

    Returns:
        DataFrame: DataFrame with nulls filled with 0 in non-excluded columns.
    """
    for column in df.columns:
        if column not in exclude_columns:
            df = df.fillna({column: 0})

    return df