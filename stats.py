#!/usr/bin/python
# Forecasting of corona virus deaths
# Notes:
# 1. Use python3
# 2. Install fbprophet pip3 install fbprophet
# 3. Install pandas pip3 install pandas
# 4. Run script python3 covid19-forecast.py
# 5. View the rendered and saved forecast image files
#
# Data Source Notes:
# COVID-19 Data Research repository from Johns Hopkins University
# Tableau publishes this data to Data World daily.
# URL: https://data.world/covid-19-data-resource-hub/covid-19-case-counts/workspace/file?filename=COVID-19+Cases.csv

# Facebook Prophet forecasting / time series predictions Library
from fbprophet import Prophet

# MATLAB like plotting library
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Python Data Analysis Library
import pandas as pd


def get_aggregate_covid_data_frame(df, case_type, country_region):
    # Returns a Covid-19 dataframe filtered by the specified
    # case type and country_region.

    # The SQL equivilant for this Pandas code is equivalent to:
    # SELECT date, sum(Cases)
    # WHERE Case_Type = [case_type]
    # AND Country_Region = [country_region]
    # GROUP BY date
    # ORDER BY date ASC
    df = df.copy()

    # Convert date column to an actual datetime data type for sorting
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data by case type and country
    df = df[(df.Case_Type == case_type) &
            (df.Country_Region == country_region)]

    # Group data by date and aggregate sum of cases
    df = df[['Date', 'Cases']].groupby(['Date'], as_index=False).sum()

    # Sort data by date ascending
    df = df.sort_values(by='Date')

    # Return the data frame
    return df


def forecast(df, forecast_output_filename, title, x_label, y_label):

    # changepoint_prior_scale / Adjusting trend flexibility:
    # If the trend changes are being overfit (too much flexibility) or underfit
    # (not enough flexibility),you can adjust the strength of the sparse prior
    # using the input argumENT Changepoint_prior_scale.
    # By default, this parameter is set to 0.05. Increasing it will make the
    # trend more flexible. Side effect of increasing this value is that it will
    # generally increase future trend uncertainty.

    # changepoint_range:
    # By default changepoints are only inferred for the first 80% of the time
    # series in order to have plenty of runway for projecting the trend forward
    # and to avoid overfitting fluctuations at the end of the time series.
    # This default works in many situations but not all, and can be change
    # using the changepoint_range argument.
    # For example, m = Prophet(changepoint_range=0.9) in Python
    # or m <- prophet(changepoint.range = 0.9) in R will place potential
    # changepoints in the first 90% of the time series.

    # seasonality_mode:
    # With seasonality_mode='multiplicative', holiday effects will also be
    # modeled as multiplicative. Any added seasonalities or extra regressors
    # will by default use whatever seasonality_mode is set to, but can be
    # overriden by specifying mode='additive' or mode='multiplicative' as
    # an argument when adding the seasonality or regressor.

    # Instantiate a new Prophet object with params best suited for daily
    # seasonalitty of COVID-19 virus case data.
    model = Prophet(
        changepoint_prior_scale=0.2,
        changepoint_range=0.95,
        yearly_seasonality=False,
        weekly_seasonality=True,  # Enable daily seasonality
        daily_seasonality=True,  # Enable daily seasonality
        seasonality_mode='additive',
    )

    # Rename the date and case_count columns to ds and y
    df = df.rename(columns={df.columns[0]: 'ds', df.columns[1]: 'y'})

    # We fit the model by instantiating a new Prophet object. Any settings to
    # the forecasting procedure are passed into the constructor. Then you call
    # its fit method and pass in the historical dataframe.
    # Fitting should take 1-5 seconds.
    model.fit(df)

    # Predictions are then made on a dataframe with a column ds containing the
    # dates for which a prediction is to be made. You can get a suitable
    # dataframe that extends into the future a specified number of days using
    # the helper method Prophet.make_future_dataframe. By default it will also
    # include the dates from the history, so we will see the model fit as well.
    future = model.make_future_dataframe(periods=365)

    # The predict method will assign each row in future a predicted value
    # which it names yhat. If you pass in historical dates, it will provide an
    # in-sample fit. The forecast object here is a new dataframe that includes
    # a column yhat with the forecast, as well as columns for components and
    # uncertainty intervals.
    forecast = model.predict(future)

    # Plot the forecast and save it to the specified output file name
    fig = model.plot(forecast)

    #Get the current Axes instance on the current figure
    ax = plt.gca()

    # Set graph title
    ax.set_title(title, size=18)

    # Set x and y axis labels
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    # Set plot line colors
    ax.get_lines()[0].set_color("black")
    ax.get_lines()[1].set_color("r")

    # Add logo badge to graph
    logo = plt.imread('badge.gif')
    ax.figure.figimage(logo, 300, 425, alpha=.75, zorder=1)

    # Disables exponent / scientific notation
    plt.ticklabel_format(style='plain', axis='y')

    # Automatically adjust subplot parameters to give specified padding.
    fig.tight_layout()

    # Save the figure
    fig.savefig(forecast_output_filename)

    # Return the model
    return model


def output_plot(df, img_output_file, graph_kind, x_field, y_field,
                x_label, y_label, line_color, title):

    # Set figure plot size
    plt.rcParams["figure.figsize"] = [10, 5]

    # Output a plot / graph with the specified data frame and output and params
    fig = df.plot(kind=graph_kind, x=x_field, y=y_field,
                  grid=True, color=line_color)

    # Set graph title
    plt.title(title)

    # Set x and y axis labels
    fig.set_xlabel(x_label)
    fig.set_ylabel(y_label)

    # Update legend color and title
    red_patch = mpatches.Patch(label=y_label, color=line_color)
    plt.legend(handles=[red_patch])
    plt.legend(facecolor="white")
    plt.legend().get_texts()[0].set_text(y_label)
    # Disables exponent / scientific notation
    plt.ticklabel_format(style='plain', axis='y')

    # Automatically adjust subplot parameters to give specified padding.
    plt.tight_layout()

    # Save the figure
    plt.savefig(img_output_file)


def main():
    # URL used to fetch COVID-19 case data in CSV format
    data_url = 'https://query.data.world/s/js7bdacf5rurkiql7nioreohprqtdx'
    #data_url = 'covid-case-data.csv'

    # Read CSV file from file name or URL
    df = pd.read_csv(data_url)

    # Save raw COVID-19 data to a local CSV file for reference
    df.to_csv('covid-case-data.csv', index=False)

    # Get aggregated COVID-19 data grouped by date and
    # summed by Deaths in the U.S.
    df_deaths = get_aggregate_covid_data_frame(df, 'Deaths', 'US')

    # Get aggregated COVID-19 data grouped by date and
    # summed by Infections in the U.S.
    df_inf = get_aggregate_covid_data_frame(df, 'Confirmed', 'US')

    # Output line graph of current death counts by date
    output_plot(df_deaths, 'covid-19-deaths-line-graph.png', 'line',
                'Date', 'Cases', 'Date', 'Death Count', 'r',
                'U.S. COVID-19 Death Count')

    # Output line graph of current infection counts by date
    output_plot(df_inf, 'covid-19-infections-line-graph.png', 'line',
                'Date', 'Cases', 'Date', 'Infection Count', 'g',
                'U.S. COVID-19 Infection Count')

    # Generate the FB Prophet forecast for deaths and output forecast images
    forecast(df_deaths, 'covid-19-death-forecast.png',
             'U.S. Covid-19 Death Forecast', 'Date', 'Deaths')

    # Generate the FB Prophet forecast for deaths and output forecast images
    forecast(df_inf, 'covid-19-infection-forecast.png',
             'U.S. Covid-19 Infection Forecast', 'Date', 'Infections')


# Invoke main function
main()
