import pandas as pd
import os


def combine_action_data_with_main(main: pd.DataFrame) -> pd.DataFrame:
    '''
    Creates new column in main 'actions_taken'
    Loops through all files in the file_path directory
    and assigns any email each file the value of its file name
    where it can be found in the main
    '''

    file_path = "../data/raw/action_data"

    main["actions_taken"] = None
    main["actions_taken"] = main["actions_taken"].astype(float)

    for file_name in os.listdir(file_path):
        try:
            action_count = int(file_name.split("-")[0])
            df = pd.read_csv(file_path+file_name)
            main.loc[main['email'].isin(df["email"]), "actions_taken"] = action_count
        except Exception as e:
            print(f"File '{file_name}' in action data directory ({file_path}) likely does not follow naming scheme '<count of actions taken>-actions' and has been overlooked Error:{e}")

    return main
