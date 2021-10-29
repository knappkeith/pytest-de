"""
Script to help with the validation of the SQL Scripts for Inspirato's
Migration off of Alteryx.

This Script requires python3.7 or higher

This script requires the following packages to be installed:
    pandas, xlrd, openpyxl

To start using this script:
    python {PATH_TO_THIS_SCRIPT} -h
"""
import argparse
import os
from inspect import cleandoc
from textwrap import indent
from typing import Optional

import pandas as pd
from pandas._testing import assert_frame_equal

DEFAULT_DROP_COLUMNS = ["RunDate", "CreatedAt", "UpdatedAt"]
DEFAULT_SQL_SHEET_NAME = "SQL"
DEFAULT_ALTX_SHEET_NAME = "ALTX"
SEC_BR_LEN = 80


class CustomArgParseFormatter(
        argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawDescriptionHelpFormatter):
    """Custom Class for Formatting argparse Formatter, allows multiple
    formatters to be used at once
    """
    pass


def does_file_exist(path: str) -> bool:
    """Return boolean if a file exists"""
    return os.path.isfile(os.path.expanduser(path))


def _build_error_str(err_num: int) -> str:
    """Build the error string to mimic the os library
    error string
    """
    return "[Errno {enum}] {edesc}: {{arg}}".format(
        enum=err_num,
        edesc=os.strerror(err_num))


def read_excel_dataframes(
        excel_path: str,
        sql_sheet: str = DEFAULT_SQL_SHEET_NAME,
        altx_sheet: str = DEFAULT_ALTX_SHEET_NAME) -> dict[str, pd.DataFrame]:
    """Read and return the two DataFrames from Excel Spread Sheet"""

    # Read all Excel sheets
    print(f"\nOpening Excel File: {excel_path}")
    all_sheets = pd.read_excel(excel_path, sheet_name=None)

    # Get SQL DataFrame
    if sql_sheet not in all_sheets:
        raise RuntimeError(
            f"SQL sheet named: '{sql_sheet}' not found in Excel File. "
            f"Sheet names Found: {', '.join(all_sheets.keys())}. "
            "Change Sheet Name or override with --sql_sheet_name option")
    print(f"Using Excel Sheet, '{sql_sheet}', for SQL Sheet.")
    sql = all_sheets[sql_sheet]

    # Get ALTX DataFrame
    if altx_sheet not in all_sheets:
        raise RuntimeError(
            f"SQL sheet named: '{sql_sheet}' not found in Excel File. "
            f"Sheet names Found: {', '.join(all_sheets.keys())}. "
            "Change Sheet Name or override with --altx_sheet_name option")
    print(f"Using Excel Sheet, '{altx_sheet}', for Alteryx Sheet.")
    altx = all_sheets[altx_sheet]

    return {"sql": sql, "altx": altx}


def read_csv_dataframe(file_path: str, name: str) -> pd.DataFrame:
    """Reads a File in as csv and returns Pandas DataFrame"""
    print(f"\nOpening CSV File: {file_path}, for {name} DataFrame")
    return pd.read_csv(file_path)


def compare_dfs(
        sql_df: pd.DataFrame,
        altx_df: pd.DataFrame,
        drop_columns_str: str,
        sort_columns_str: Optional[str] = None) -> None:
    """Compares two Panda DataFrames for validation of Alteryx Migration for
    Inspirato's Pass Engine
    """

    # Print stats of DataFrames before any work
    nl = "\n"
    print(f"{nl}{' SQL Info ':-^{SEC_BR_LEN}}")
    print(
        f"{nl}SQL DataFrame Dimensions: "
        f"{len(sql_df.columns)} columns, {len(sql_df.index)} rows")
    print("SQL Column Names:")
    print(indent(
        "".join([
            f"{col}, {nl if i % 5 == 4 else ''}"
            for i, col in enumerate(sql_df.columns)
        ]), "    ").rstrip().rstrip(","))
    print(f"{nl}{' Alteryx Info ':-^{SEC_BR_LEN}}")
    print(
        f"{nl}Alteryx DataFrame Dimensions: "
        f"{len(altx_df.columns)} columns, {len(altx_df.index)} rows")
    print("Alteryx Column Names:")
    print(indent(
        "".join([
            f"{col}, {nl if i % 5 == 4 else ''}"
            for i, col in enumerate(altx_df.columns)
        ]), "    ").rstrip().rstrip(","))

    # Determine Drop Columns
    drop_columns = [x.strip() for x in drop_columns_str.split(",")]

    # Drop Columns from SQL
    print(f"{nl}{' Dropping Columns ':-^{SEC_BR_LEN}}")
    print(
        f"{nl}Dropping Columns from SQL:{nl}    {', '.join(drop_columns)}{nl}")
    for column in drop_columns:
        if column not in sql_df.columns:
            print(
                "    WARNING: Unable to drop column: "
                f"'{column}' from SQL DataFrame")
        else:
            sql_df = sql_df.drop(columns=column)
            print(f"    Column: '{column}' dropped from SQL DataFrame")

    # Drop Columns from ALTX
    print(
        f"{nl}Dropping Columns from Alteryx:{nl}    "
        f"{', '.join(drop_columns)}{nl}")
    for column in drop_columns:
        if column not in altx_df.columns:
            print(
                "    WARNING: Unable to drop column: "
                f"'{column}' from Alteryx DataFrame")
        else:
            altx_df = altx_df.drop(columns=column)
            print(f"    Column: '{column}' dropped from Alteryx DataFrame")

    # Sort Columns
    if sort_columns_str is not None:
        sort_columns = [str(x).strip() for x in sort_columns_str.split(",")]
        print(f"{nl}{' Sort Columns ':-^{SEC_BR_LEN}}")
        sql_df.sort_values(by=sort_columns, inplace=True, ignore_index=True)
        print(f"{nl}    Sorted SQL DataFrame by: {', '.join(sort_columns)}")
        altx_df.sort_values(by=sort_columns, inplace=True, ignore_index=True)
        print(f"    Sorted Alteryx DataFrame by: {', '.join(sort_columns)}")

    # Test that All column Names match
    print(f"{nl}{' Start Comparisons ':-^{SEC_BR_LEN}}")
    assert len(sql_df.index) == len(altx_df.index), \
        "Number of Rows does not match"
    print("    PASSED - Row Counts Match")
    assert all(sql_df.columns == altx_df.columns), \
        "Not All column Names match."
    print("    PASSED - Column Names Match")

    # Test that the DataFrames Match Exactly
    assert_frame_equal(sql_df, altx_df, check_like=True)
    print("    PASSED - YAY!! The SQL and Alteryx DataFrames Match exactly!")
    print(f"{nl}{' End Comparisons ':-^{SEC_BR_LEN}}")


def parse_the_command_line() -> argparse.Namespace:
    """Parses the command line arguments and returns argparse.Namespace Object
    """

    # Build Arg Parser
    parser = argparse.ArgumentParser(
        description=indent(cleandoc(__doc__), "    "),
        formatter_class=CustomArgParseFormatter
    )

    # Mutually Exclusive group for excel or csv
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-e", "--excel_path",
        type=str,
        help="Path to the Excel file for Validation")
    group.add_argument(
        "-c", "--csv_paths",
        nargs=2,
        type=str,
        help="Paths to the CSV files for Validation, [SQL] [Alteryx]")

    # Drop Columns
    parser.add_argument(
        "-d", "--drop_columns",
        type=str,
        help="List of column names to drop Before Comparison",
        default=", ".join(DEFAULT_DROP_COLUMNS))

    # Custom Sheet Names for Excel
    parser.add_argument(
        "--sql_sheet_name",
        type=str,
        help="Sheet name to use for SQL data.",
        default=DEFAULT_SQL_SHEET_NAME
    )
    parser.add_argument(
        "--altx_sheet_name",
        type=str,
        help="Sheet name to use for Alteryx data.",
        default=DEFAULT_ALTX_SHEET_NAME
    )

    # Sort Column(s)
    parser.add_argument(
        "-s", "--sort_column",
        type=str,
        help="Column Name(s) to sort DataFrames before comparing")

    # Parse it and return
    return parser.parse_args()


def main():
    """Main method for Alteryx -> SQL Validation Tool"""

    # Get the command line args
    args = parse_the_command_line()

    # Excel File
    excel_path = args.excel_path
    if excel_path is not None:

        # Make sure file exists
        if not does_file_exist(args.excel_path):
            raise OSError(_build_error_str(2).format(arg=excel_path))

        # Check File Extension
        file_ext = os.path.splitext(excel_path)[-1]
        allowed_ext = [".xlsx", ".xls", ".xlsm"]
        if file_ext not in allowed_ext:
            raise RuntimeError(
                f"File extension, {file_ext}, "
                f"not permitted must be {' or '.join(allowed_ext)}")

        # Read Data Frames
        print()
        print(f"{' Read Excel DataFrames ':=^{SEC_BR_LEN}}")
        dfs = read_excel_dataframes(
            excel_path=excel_path,
            sql_sheet=args.sql_sheet_name,
            altx_sheet=args.altx_sheet_name)
        sql_df = dfs["sql"]
        altx_df = dfs["altx"]
    else:
        # CSV Files
        csv_paths = args.csv_paths
        files_not_exist = [x for x in csv_paths if not does_file_exist(x)]
        if len(files_not_exist) > 0:
            raise OSError(
                _build_error_str(2).format(arg=", ".join(files_not_exist)))

        # Read the files
        print()
        print(f"{' Read CSV DataFrames ':=^{SEC_BR_LEN}}")
        sql_df = read_csv_dataframe(csv_paths[0], "SQL")
        altx_df = read_csv_dataframe(csv_paths[1], "Alteryx")

    # Compare the dataframes
    print()
    print(f"{' Compare DataFrames ':=^{SEC_BR_LEN}}")
    try:
        compare_dfs(
            sql_df, altx_df,
            drop_columns_str=args.drop_columns,
            sort_columns_str=args.sort_column)
        print(f"{' Compare SUCCESSFUL!!! ':=^{SEC_BR_LEN}}")
    except Exception:
        print(f"{' Compare FAILED!!! ':=^{SEC_BR_LEN}}")
        raise


if __name__ == "__main__":
    main()
