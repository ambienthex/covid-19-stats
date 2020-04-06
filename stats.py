#!/usr/bin/python

"""Return a Covid-19 dataframe filtered with specified criteria."""

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
# URL: https://data.world/covid-19-data-resource-hub/covid-19-case-counts/
# workspace/file?filename=COVID-19+Cases.csv

# Command Line Options
# -c or --country; Optionally specifies a country to perform stats against.
# -p or --province: Optionally specifies state or province to perform stats.
# -cl: Displays list of valid country names
# -pl: Displays list of valid provinces for the specified country(-c)
#   Example:
#     parser.add_argument('-c', '--country',
#
# Note; -pl only works with US at this time.
#
# Valid Country Names;
# All, Afghanistan, Albania, Algeria, Andorra, Angola, Antigua and Barbuda,
# Argentina, Armenia, Australia, Austria, Azerbaijan, Bahamas, Bahrain,
# Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bhutan, Bolivia,
# Bosnia and Herzegovina, Botswana, Brazil, Brunei, Bulgaria, Burkina Faso,
# Burma, Burundi, Cabo Verde, Cambodia, Cameroon, Canada,
# Central African Republic, Chad, Chile, China, Colombia, Congo (Brazzaville),
# Congo (Kinshasa), Costa Rica, Cote d'Ivoire, Croatia, Cruise Ship, Cuba,
# Cyprus, Czechia, Denmark, Djibouti, Dominica, Dominican Republic, Ecuador,
# Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Eswatini, Ethiopia,
# Fiji, Finland, France, Gabon, Gambia, Georgia, Germany, Ghana, Greece,
# Grenada, Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Holy See,
# Honduras, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland,
# Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya, 'Korea, South",
# Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon, Liberia, Libya,
# Liechtenstein, Lithuania, Luxembourg, Madagascar, Malaysia, Maldives,
# Mali, Malta, Mauritania, Mauritius, Mexico, Moldova, Monaco, Mongolia,
# Montenegro, Morocco, Mozambique, Namibia, Nepal, Netherlands,
# New Zealand, Nicaragua, Niger, Nigeria, North Macedonia, Norway, Oman,
# Pakistan, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland,
# Portugal, Qatar, Romania, Russia, Rwanda, Saint Kitts and Nevis, Saint Lucia,
# Saint Vincent and the Grenadines, San Marino, Saudi Arabia, Senegal, Serbia,
# Seychelles, Sierra Leone, Singapore, Slovakia, Slovenia, Somalia,
# South Africa, Spain, Sri Lanka, Sudan, Suriname, Sweden, Switzerland,
# Syria, Taiwan*, Tanzania, Thailand, Timor-Leste, Togo, Trinidad and Tobago,
# Tunisia, Turkey, US, Uganda, Ukraine, United Arab Emirates, United Kingdom
# Uruguay, Uzbekistan, Venezuela, Vietnam, West Bank and Gaza, Zambia, Zimbabwe
import sys

# Parser for command-line options
import argparse

# Facebook Prophet forecasting / time series predictions Library
from fbprophet import Prophet

# MATLAB like plotting library
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Python Data Analysis Library
import pandas as pd

# Python XML HTML parser
from bs4 import BeautifulSoup


def get_aggregate_covid_data_frame(df, case_type, sum_field,
                                   country_region=None,
                                   province_state=None):
    """Return a Covid-19 dataframe filtered with specified criteria.

    Case type can be Confirmed or Deaths
    Sum field can be Cases or Difference
    The SQL equivilant for this Pandas code is equivalent to:
    SELECT date, sum(Cases)
    WHERE Case_Type = [case_type]
    AND Country_Region = [country_region]
    GROUP BY date
    ORDER BY date ASC.
    """
    df = df.copy()

    # Convert date column to an actual datetime data type for sorting
    df['Date'] = pd.to_datetime(df['Date'])

    # Dynamically build query criteria
    criteria = '(Case_Type == "' + case_type + '")'

    if country_region.lower() != 'all':
        if (country_region):
            criteria += ' & (Country_Region == "' + country_region + '")'
        if (province_state):
            criteria += ' & (Province_State == "' + province_state + '")'

    # Get data frame with a query using the dynamic criteria
    df = df.query(criteria)

    # Group data by date and aggregate sum of cases
    df = df[['Date', sum_field]].groupby(['Date'], as_index=False).sum()

    # Sort data by date ascending
    df = df.sort_values(by='Date')

    # Return the data frame
    return df


def forecast(df, forecast_output_filename, title, x_label, y_label):
    """Return a Covid-19 dataframe filtered with specified criteria."""
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
        changepoint_prior_scale=0.25,
        changepoint_range=0.95,
        yearly_seasonality=False,
        weekly_seasonality=False,  # Enable daily seasonality
        daily_seasonality=True,  # Enable daily seasonality
        seasonality_mode='multiplicative',
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
    future = model.make_future_dataframe(periods=90,
                                         freq="D", include_history=True)

    # The predict method will assign each row in future a predicted value
    # which it names yhat. If you pass in historical dates, it will provide an
    # in-sample fit. The forecast object here is a new dataframe that includes
    # a column yhat with the forecast, as well as columns for components and
    # uncertainty intervals.
    forecast = model.predict(future)

    # Plot the forecast and save it to the specified output file name
    fig = model.plot(forecast)

    # Get the current Axes instance on the current figure
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
    return forecast


def output_plot(df, img_output_file, graph_kind, x_field, y_field,
                x_label, y_label, line_color, title):
    """Output a plot image using the specified data frame and args."""
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


def insert_dataframe_html_into_div(soup, df, div_id):
    """Insert dataframe HTML into DIV by id."""
    element = soup.find(id=div_id)
    element.append(BeautifulSoup(df.to_html(), 'html.parser'))


def output_graph_set_by_country(df, country, province=None):
    """Output graph set by country."""
    # Get aggregated COVID-19 data grouped by date and
    # summed by Deaths in the U.S. Running total.
    df_running_total_deaths = get_aggregate_covid_data_frame(df, 'Deaths',
                                                             'Cases', country,
                                                             province)

    # Get aggregated COVID-19 data grouped by date and
    # summed by Infections in the U.S. Running total.
    df_running_total_inf = get_aggregate_covid_data_frame(df, 'Confirmed',
                                                          'Cases', country,
                                                          province)

    # Get aggregated daily COVID-19 infection data grouped by date and
    # summed by Infections in the U.S
    df_daily_deaths = get_aggregate_covid_data_frame(df, 'Deaths',
                                                     'Difference', country,
                                                     province)

    # Get aggregated daily COVID-19 infection data grouped by date and
    # summed by Infections in the U.S.
    df_daily_inf = get_aggregate_covid_data_frame(df, 'Confirmed',
                                                      'Difference', country,
                                                      province)

    location = None
    if country.lower() == 'all':
        location = 'Global'
    else:
        location = province + ', ' + country if province else country

    # Output line graph of current death counts by date
    output_plot(df_running_total_deaths,
                'covid-19-deaths-running-total-line-graph.png',
                'line', 'Date', 'Cases', 'Date', 'Death Count', 'r',
                location + ' COVID-19 Running Total Death Count')

    # Output line graph of current infection counts by date
    output_plot(df_running_total_inf,
                'covid-19-infections-running-total-line-graph.png',
                'line', 'Date', 'Cases', 'Date', 'Infection Count', 'g',
                location + ' COVID-19 Running Total Infection Count')

    # Output line graph of current death counts by date
    output_plot(df_daily_deaths, 'covid-19-deaths-by-day-line-graph.png',
                'line', 'Date', 'Difference', 'Date', 'Death Count', 'r',
                location + ' COVID-19 Deaths per Day')

    # Output line graph of current infection counts by date
    output_plot(df_daily_inf, 'covid-19-infections-by-day-line-graph.png',
                'line', 'Date', 'Difference', 'Date', 'Infection Count', 'g',
                location + ' COVID-19 Infections per Day')

    # Forecast total deaths. No limiting factors defined.
    forecast(df_running_total_deaths, 'covid-19-total-death-forecast.png',
             location + ' COVID-19 Total Death Forecast', 'Date',
             'Total Deaths')

    # Forecast daily deaths. No limiting factors defined.
    forecast(df_daily_deaths, 'covid-19-daily-death-forecast.png',
             location + 'COVID-19 Daily Death Forecast', 'Date',
             'Daily Deaths')

    # Forecast total infections. No limiting factors defined
    forecast(df_running_total_inf, 'covid-19-total-infection-forecast.png',
             location + 'COVID-19 Total Infection Forecast',
             'Date', 'Total Infections')

    # Forecast daily infections. No limiting factors defined
    forecast(df_daily_inf, 'covid-19-daily-infection-forecast.png',
             location + 'COVID-19 Daily Infections Forecast', 'Date',
             'Daily Infections')

    df_combined = pd.concat([df_running_total_deaths,
                            df_daily_deaths,
                            df_running_total_inf,
                            df_daily_inf],
                            ignore_index=True, axis=1)

    df_combined = df_combined[[0, 1, 3, 5, 7]]
    df_combined.columns = df_combined.columns.astype(str)
    df_combined.columns = ['Date', 'Running Death Count', 'Daily Deaths',
                           'Running Infection Count', 'Daily Infections']
    df_combined.to_csv('stats-by-date.csv', index=False)

    soup = BeautifulSoup(open('covid-19-stats-html.template'), 'html.parser')
    insert_dataframe_html_into_div(soup, df_combined, 'data-frame')

    with open("covid-19-stats.htm", "w") as file:
        file.write(str(soup))


def get_countries(df):
    """Return data frame of unique countries."""
    df_countries = df['Country_Region'].unique()
    return sorted(df_countries)


def get_provinces_for_country(df, country):
    """Return data frame of unique countries."""
    criteria = '(Country_Region == "' + country + '")'

    # Get data frame with a query using the dynamic criteria
    df = df.query(criteria)
    df_provinces = df['Province_State'].unique()
    return sorted(df_provinces)


def main(argv):
    """Main function."""
    country = 'US'
    province = None

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--country',
                        help="sets country filter for COVID-19 reports. "
                        "Default if not specified is US. Use \"all\" for "
                        "global reports.")
    parser.add_argument('-p', '--province',
                        help="sets state or province for COVID-19 reports.")
    parser.add_argument('-cl', '--countrylist', action='store_true',
                        help="displays valid country names.")
    parser.add_argument('-pl', '--provincelist', action='store_true',
                        help="displays valid provinces or states for country.")
    args = parser.parse_args()

    # URL used to fetch COVID-19 case data in CSV format
    data_url = 'https://query.data.world/s/js7bdacf5rurkiql7nioreohprqtdx'
    # data_url = 'covid-case-data.csv'

    # Read CSV file from file name or URL
    df = pd.read_csv(data_url)

    if args.country:
        country = args.country

    if args.province:
        province = args.province

    if args.countrylist:
        print(get_countries(df))
        sys.exit()

    if args.provincelist:
        print(get_provinces_for_country(df, country))
        sys.exit()

    # Save raw COVID-19 data to a local CSV file for reference
    df.to_csv('covid-case-data.csv', index=False)

    # Output graph set by country
    output_graph_set_by_country(df, country, province)

if __name__ == "__main__":
    main(sys.argv[1:])
