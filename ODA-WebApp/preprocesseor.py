import pandas as pd
df = pd.read_csv('/home/abdollatif/Desktop/ODA/athlete_events.csv')
df_region = pd.read_csv('/home/abdollatif/Desktop/ODA/noc_regions.csv')

def preprocess(df, region_df):

    df = df[df['Season'] == 'Summer']

    df = df.merge(region_df,on = 'NOC', how='left')

    df.drop_duplicates(inplace = True)

    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis = 1)

    return df