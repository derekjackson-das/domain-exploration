import pandas as pd


def find_from_sd(sd, data, check=['subdomain1', 'subdomain2', 'subdomain3', 'subdomain4', 'subdomain5', 'subdomain6',
                                  'bottom_dom_trunc']):
    # search the domains in 'data' for a string match.
    """
    Search a list of columns (check) in a dataframe (data) columns a string (sd) match.

    sd = string to look for a match in the subdomain columns.
    data = pandas dataframe
    check = list of column names. default value is ['subdomain1', 'subdomain2', 'subdomain3', 'subdomain4', 'subdomain5', 'subdomain6', 'bottom_dom_trunc']
    """
    df = pd.DataFrame([], columns=data.columns)

    try:
        for i in check:
            test = data[data[i] == sd].shape[0]
            if test != 0:
                df = df.append(data[data[i] == sd], ignore_index=True)
    except KeyError as err:
        return print(f'KeyError: bad column name. {err}')

    if df.shape[0] == 0:
        return print("No matches found")

    return df


def show_rows(x="off", length=None):
    """
    quickly toggle row display on or off (I never can remember the pandas method and arguments.)
    default is to turn max rows off.
    set pass "on" to expand the row setting, add a number to limit to set max # of columns.
    x = string. Use "on" to set dataframe row numbers. default to off. All other values reset the row option.
    length = integer. Sets the number of rows to display. default is None.
    """
    if x == "on":
        pd.set_option("display.max_rows", length)
    else:
        pd.reset_option("display.max_rows")


def search(term, df, col=["all"]):
    """
    Search selected columns of a dataframe for a string (e.g. subdomain)
    term = string to search for
    df = pandas dataframe to search
    col = array of the column(s) to search in (column must contain strings)
    The search iterates through all the columns one row at a time looking for a match and returns a dataframe with all the matched rows
    """
    temp_df = pd.DataFrame([], columns=df.columns)
    if col[0] == "all":
        check = df.columns
    else:
        check = col

    r = df.shape[0]
    skipped_rows = False
    e = ""
    for c in check:
        for i in range(0, r):
            try:
                str_index = df.loc[i, c].find(term)
                if str_index != -1:
                    temp_df = temp_df.append(df.loc[i], ignore_index=True)
            except AttributeError as Error:
                skipped_rows = True
                e = Error

    if skipped_rows:
        print(
            f'Skipped Rows: Rows in {c} column. Some cells do not contain string object and cannot be searched. {e}')

    return temp_df
