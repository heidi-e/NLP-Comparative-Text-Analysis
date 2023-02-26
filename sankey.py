import pandas as pd
import plotly.graph_objs as go

# Conor Doyle, DS3500 HW 1


def _code_mapping(df, src, targ):
    """ create the labels for the nodes of the sankey, and place them into a df
    """
    # Get distinct labels
    labels = sorted(list(set(list(df[src]) + list(df[targ]))))

    # Get integer codes
    codes = list(range(len(labels)))

    # Create label to code mapping
    lc_map = dict(zip(labels, codes))

    # Substitute names for codes in dataframe
    df = df.replace({src: lc_map, targ: lc_map})

    return df, labels


def filter_df(df, col1, col2):
    """filter the provided df so it is suitable for make_sankey.
        col1 and col2 are the columns to be grouped by"""

    # group by the designated columns and aggregate
    aggregate_df = df.groupby([col1, col2])['artist_num'].sum().reset_index()

    # filter out groups less than 26
    aggregate_df.artist_num = aggregate_df.artist_num.astype(int)
    filtered_df = aggregate_df.loc[aggregate_df["artist_num"] > 25]

    # make sure everything is string format
    filtered_df = filtered_df.applymap(str)

    return filtered_df


def make_sankey(df, src, targ, cols=[], vals=None, **kwargs):
    """ function to create sankey plot
    df - filtered data frame to use
    src - sankey source node
    targ - sankey targ node
    cols - list to make multi-layer sankey (add in extra columns)
    vals - can optionally change line values
    """
    # filter the provided dataframe
    filtered_df = filter_df(df, src, targ)
    # check for the multi-layer sankey
    if len(cols) > 0:
        # create a list of the columns to concat together
        col_list = [src, targ] + cols
        # loop through the list provided, and concat all into one DF
        for i in range(2, len(col_list)):
            # create a temporary df to concat with the previous
            combining_df = filter_df(df, col_list[i - 1], col_list[i])
            # set the columns
            combining_df.columns = [src, targ, "artist_num"]
            # concat
            filtered_df = pd.concat([filtered_df, combining_df], axis=0)

        # recursion with concated df
        make_sankey(filtered_df, src, targ)
    else:
        # adjust values if not provided
        if vals:
            values = filtered_df[vals]
        else:
            values = [1] * len(filtered_df)

        # arrange nodes
        filtered_df, labels = _code_mapping(filtered_df, src, targ)
        link = {'source': filtered_df[src], 'target': filtered_df[targ], 'value': values}
        pad = kwargs.get('pad', 50)

        # arrange labels and plot
        node = {'label': labels, 'pad': pad}
        sk = go.Sankey(link=link, node=node)
        fig = go.Figure(sk)
        fig.show()
