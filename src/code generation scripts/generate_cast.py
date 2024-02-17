from add_cast import reformat_column_names
from reformat_cast_to_contain_quote import reformat_sql_select_list

input = "columnName1, columnName2, columnName3"

first = reformat_column_names(input)
print(first)
second = reformat_sql_select_list(first)
print(second)