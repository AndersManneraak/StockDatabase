import os
import pandas as pd
import json
import csv

class DataHandler:
    def __init__(self, output_directory=None):
        self.output_directory = output_directory


    def set_output_dir(self,new_dir):
        self.output_directory = new_dir
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            
    def get_current_dir(self):
        return self.output_directory

    def save_data_to_csv(self, data, file_name):
        """
        Saves the given data as a CSV file with the specified file name.

        :param data: The data to save, can be a pandas DataFrame or a JSON object.
        :param file_name: The name of the CSV file.
        """
        if isinstance(data, pd.DataFrame):
            csv_path = os.path.join(self.output_directory, f"{file_name}.csv")
            data.to_csv(csv_path, index=False)
        elif isinstance(data, dict):
            csv_path = os.path.join(self.output_directory, f"{file_name}.csv")
            df = pd.DataFrame.from_dict(data)
            df.to_csv(csv_path, index=False)
        else:
            raise TypeError("The provided data must be a pandas DataFrame or a JSON object.")

        print(f"Data saved to: {csv_path}")
    
    def json_to_df(self,json_data):
        if json_data != None:
            df_data = json.load(json_data)
            df = pd.DataFrame(df_data)
            return df
        else:
            return pd.DataFrame()
        
    def df_list_to_file(self,df_list_file,filepath, action='a',indexparam=False):
        with open(filepath,'w') as f:
            df_list_file[0].to_csv(f,index=indexparam,line_terminator='\n')
        if len(df_list_file) > 1:
            with open(filepath,action) as f:
                for x in range(1,len(df_list_file)):
                    df_list_file[x].to_csv(f,header=False,index=indexparam,line_terminator='\n')

    def filter_list_without_substring(self,input_list, substring):
        filtered_list = [item for item in input_list if substring not in item]
        return filtered_list

    def read_csv_to_list(self,file_path):
        if not os.path.exists(file_path):
            return []
        result = []
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                result.append(row[0])
        return result if result else []
# Usage example