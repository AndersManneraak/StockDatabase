from add_cast import reformat_column_names, reformat_sql_select_list

#legg til kolonneliste som skal formateres
input = "columnName1, columnName2, columnName3, dateree"

first = reformat_column_names(input)
print(first)
second = reformat_sql_select_list(first)
print(second)