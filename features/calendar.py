from datetime import datetime, date
import numpy as np
import pandas as pd
import holidays

def calendar_denmark(start: str = (pd.Timestamp.now().year - 2), end: str = (pd.Timestamp.now().year + 1)) -> pd.DataFrame:
    """
    Fetches calendar for Denmark.

    Parameters:
    - start (str): Define a start year. Default current year minus 2 years.
    - end (str): Define a end year. Default current year and 1 year ahead.

    Returns:
    - pd.DataFrame: DataFrame with calendar for Denmark.
    """

    # Define the start and end dates
    start_date = start
    end_date = str(end) + '-12-31'

    # Generate the date range
    date_range = pd.date_range(start=str(start_date), end=str(end_date), freq='D')

    # Convert the date range to a DataFrame
    calendar_df = pd.DataFrame({'date': date_range})

    # Add features to the calendar dataframe
    calendar_df['date'] = pd.to_datetime(calendar_df['date'])
    calendar_df['dayofweek'] = calendar_df['date'].dt.dayofweek
    calendar_df['day'] = calendar_df['date'].dt.day
    calendar_df['month'] = calendar_df['date'].dt.month
    calendar_df['year'] = calendar_df['date'].dt.year

    # Select country
    dk_holidays = holidays.Denmark()

    # Initialize lists to store data
    data = []

    # Iterate over each date in the date range
    for date in calendar_df['date']:
        # Check if it's a holiday
        if date in dk_holidays:
            is_workday = 0  # Not a workday
        # Check if it's a weekend (Saturday or Sunday)
        elif date.dayofweek >= 5:
            is_workday = 0  # Not a workday
        else:
            is_workday = 1  # Workday

        # Append data to list
        data.append({'date': date, 'workday': is_workday})

    # Create DataFrame
    workday_df = pd.DataFrame(data)

    # Merge workday information into the calendar DataFrame
    calendar_df = pd.merge(calendar_df, workday_df, on='date', how='left')

    return calendar_df