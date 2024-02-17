import re


def reformat_column_names(input_column_names):
    # Splitting the input string by commas to get individual column names
    column_names = input_column_names.split(", ")

    reformatted_columns = []

    for column_name in column_names:
        # Applying the desired formatting to each column name
        reformatted_column = f'cast({column_name} as number) as {column_name}'
        reformatted_columns.append(reformatted_column)

    # Combining the reformatted column names back into a comma-separated list
    reformatted_column_names_list = ", ".join(reformatted_columns)

    return reformatted_column_names_list




def reformat_sql_select_list(input_sql_list):
    # Regular expression to match the pattern: cast(columnName as type) as ColumnName
    pattern = re.compile(r'cast\((.*?) as (.*?)\) as (\w+)', re.IGNORECASE)

    # Find all matches in the input string
    matches = pattern.findall(input_sql_list.replace('\n', ' '))

    reformatted_statements = []

    for match in matches:
        column_name, column_type, alias = match

        # Function to check if the string contains both uppercase and lowercase characters
        def contains_both_cases(s):
            return any(c.islower() for c in s) and any(c.isupper() for c in s)

        # Function to convert CamelCase alias to snake_case
        def camel_to_snake(name):
            return ''.join(['_'+c.lower() if c.isupper() else c for c in name]).lstrip('_')

        # Converting only the alias to snake_case if it contains both uppercase and lowercase characters
        if contains_both_cases(alias):
            alias_snake_case = camel_to_snake(alias)
        else:
            alias_snake_case = alias

        # Assembling the reformatted SQL statement
        reformatted_sql = f'cast("{column_name}" as {column_type}) as {alias_snake_case}'
        reformatted_statements.append(reformatted_sql)

    # Combining the reformatted statements back into a comma-separated list
    reformatted_sql_list = ", ".join(reformatted_statements)

    return reformatted_sql_list
