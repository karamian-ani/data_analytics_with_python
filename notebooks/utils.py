import pandas as pd
import numpy as np
import plotly.express as px


def my_bar_plot(df:pd.DataFrame,
                x_col:str,
                y_col:float,
                flag:bool =True)-> px.bar:
    
    df_agg = (
    df.groupby(x_col, as_index=False)[y_col]
             .sum()
    )   

    if flag:
        flag_region = df_agg.loc[df_agg[y_col].idxmax(), x_col]
        df_agg["highlight"] = np.where(
            df_agg[x_col] == flag_region,
            f"Highest {y_col.capitalize()}",
            f"Other {y_col.capitalize()}"
        )
        colorizer = {
            f"Highest {y_col.capitalize()}": "#3B6EAD",
            f"Other {y_col.capitalize()}": "#D9D9D9"
        }
    else:
        flag_region = df_agg.loc[df_agg[y_col].idxmin(), x_col]
        df_agg["highlight"] = np.where(
            df_agg[x_col] == flag_region,
            f"Lowest {y_col.capitalize()}",
            f"Other {y_col.capitalize()}"
        )
        colorizer = {
            f"Lowest {y_col.capitalize()}": "#3B6EAD",
            f"Other {y_col.capitalize()}": "#D9D9D9"
        }

    fig = px.bar(
    df_agg,
    x=x_col,
    y=y_col,
    color="highlight",

    title=f'Total {y_col.capitalize()} by {x_col.capitalize()}',
    color_discrete_map=colorizer
    )

    fig.update_traces(textposition="outside")
    

    fig.update_layout(
        xaxis_title=x_col.capitalize(),
        yaxis_title=y_col.capitalize(),
        legend_title="",
        
        
        
    )

        
    
    return fig

def csv_downloader(URL: str, name: str, path: str):
    """
    Download a CSV file from a URL, save it locally, and return it as a DataFrame.

    Parameters
    ----------
    URL : str
        CSV file URL.
    name : str
        Output file name.
    path : str
        Directory where the file will be saved.

    Returns
    -------
    pandas.DataFrame
        Downloaded CSV data.
    """
    df = pd.read_csv(URL)
    df.to_csv(f"{path}/{name}", index=False)
    print(f'{name} have been successfully saved in {path}')
    print(f"The size of the data {df.shape}")
    return df