# Project: U.S. COVID-19 Virus Forecasting
This GIT repo contains a simple Python(3) script (stats.py) that can be used to forecast U.S. COVID-19 deaths and infections using case data from John Hopkins University. The stats.py script will pull the current John Hopkins COVID-19 CSV case data (updated daily at 9a.m.), transform and aggregate the data using Pandas, and generate a forecast using Facebook's Prophet library. Output is two forecast graphs for deaths and infections and two line graphs for deaths and infection counts. 

Keep in mind the forecast can change for better or worse as new case data is added day to day. Forecast will get better as more data is available and hope to see the forecast go the other way sooner rather than later. 

**Facebook's Prophet Documentation:** https://facebook.github.io/prophet/

**Pandas Documentation:** https://pandas.pydata.org/docs/

# Abstract:
**On March 15th, 2020**, the US Center for Disease Control and Prevention reported that between 160 and 214 million people could become infected with COVID-19 in the United States with 200,000 to 1.7 million deaths. They stated that the epidemic could last months or even over a year.

**Source**: https://www.independent.co.uk/news/world/americas/coronavirus-death-toll-worst-case-scenario-millions-dead-in-us-a9402276.html

Over a million U.S. deaths seemed too high and wanted to attempt a basic forecast of the death toll without the epidemiology factors I'm not familiar with to determine if those figures were media hyperbole or not. Tableau is publishing COVID-19 virus case data from John Hopkins University to Data world. The data is updated daily at 9:00am EST and can be found at https://data.world/covid-19-data-resource-hub/covid-19-case-counts/workspace/file?filename=COVID-19+Cases.csv

Python with the Pandas, Facebook Prophet library and the John Hopkins University COVID-19 case data was used to try to forecast the U.S. death toll and it was found to be in the range of 75,000 to 210,000 possible deaths as of March 30th. This can change day to day for better or worse and hopefully decrease soon as doctors and healthcare workers find treatments that work. Albeit still tragic, this seemed more reasonable than the previously forecasted 200,000 to 1.7 million  possible U.S. deaths reported by the US Center for Disease Control and Prevention and the media. I am more optimistic with a range of 50,000 - 100,000 possible deaths regardless of what the forecast shows as it doesn't account for things that will help or slow the situation. The death toll could be way less if doctors and nurses don't fall ill, hospitals are not overwhelmed and effective treatments are found. Any loss of life is tragic and hope for the best. Believe healthcare workers and medical professionals will adapt and overcome to win the battle against COVID-19.

**On March 29th**, Dr. Anthony Fauci, Director of NIAID(National Institute of Allergy and Infectious Diseases) announced that 100,000 to 200,000 Americans could die from the COVID-19 which contradicted the 200,000 to 1.7 million range provided by the US Center for Disease Control and Prevention.

**Source**: https://www.npr.org/sections/coronavirus-live-updates/2020/03/29/823517467/fauci-estimates-that-100-000-to-200-000-americans-could-die-from-the-coronavirus


A simple forecast using FB Prophet with the data from John Hopkins University seems to be about in line with Dr. Fauci's reported range of 100,000 to 200,000 possible U.S. COVID-19 deaths.

# Sample Facebook Prophet COVID-19 Death Forecast
Using Facebook Prophet and the John Hopkins Data Set, the forecast is nearly in line with Dr. Fauci's announcement of 100,000 to 200,000 possible U.S. deaths as of March 29th, 2020.
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/deaths.jpg)

# Death Count Graph as of March 31st, 2020
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/covid-19-deaths-line-graph.png)

# Infection Count Graph as of March 31st, 2020
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/covid-19-infections-line-graph.png)

**On March 31st**, Forecast jump... President Donald Trump and Dr. Deborah Birx, the coordinator of the White House coronavirus task force warned Americans to brace for a “hell of a bad two weeks” ahead as the White House projected there could be 100,000 to 240,000 deaths in the U.S. from the coronavirus pandemic even if current social distancing guidelines are maintained.


**Source**: https://apnews.com/6ed70e9db88b80439a087fdad8238009

This somewhat confirms they are doing linear regression on the aggregate sum of death counts by day. Here's the updated forecast using this code for March 31st. Again, this forecast is about inline still. 
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/covid-19-death-forecast-2020-03-31.png)


# Assumptions

Thought I could use the infection case data with the death case data somehow in generating a forecast of possible deaths, but it's been reported that the infection data is almost meaningless to epidemiologists and incomplete. Death seems to be the only absolute in the data. It appears Dr. Fauci's estimate was possibly generated with adaptive linear regression on the aggregated daily death counts, so forecasting on the daily aggregated death counts alone to see how it compares and it's in the range. They may have done something more complicated. Who knows.

**On March 3rd, 2020**, Steve Goodman, a professor of epidemiology at Stanford University, said, “The infection numbers are almost meaningless. There is a huge reservoir of people who have mild cases, and would not likely seek testing. The rate of increase in positive results reflect a mixed-up combination of increased testing rates and spread of the virus."

**Source**: https://www.bloomberg.com/opinion/articles/2020-03-28/confirmed-coronavirus-cases-is-an-almost-meaningless-metric

Even though this forecast is in the range of 100,000 to 200,000 possible deaths and in line with Dr. Faucis forecast range, I'm slightly more optimistic with a range of 50,000 - 100,000 possible deaths regardless of what the forecast shows. This forecast doesn't account for things that will help or slow the situation(e.g. positive changes, behavior changes, effective social distancing and effective treatments that may emerge). The death toll could be way less if doctors and nurses don't fall ill, hospitals are not overwhelmed and effective treatments are found. Any loss of life is tragic and hope for the best. Believe healthcare workers and medical professionals will adapt and overcome to win the battle against COVID-19.


# Implementation
1. Pull the current John Hopkins data.

2. Aggregate cases by date with a sum on death count to get the number of deaths per day.

3. Was going to try implementing raw linear regression (Y = a + bX) in code, but Facebook's Prophet forecasting library makes it easy and automatically handles model curve fitting using machine learning. Will use Python, Pandas for fetching and querying the data and Facebook Prophet to handle the forecast and rendering of forecast graphs.


# John Hopkins Case Data CSV Definition

| COLUMN NAME       | TYPE     | DESCRIPTION                                                                                                                        |
|-------------------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| Case_Type         | string   |  Confirmed Cases and total deaths. Values: "Confirmed" or "Deaths")                                                                |
| Cases             | integeer | Point in time snapshot of to-date totals (i.e., Mar 22 is inclusive of all prior dates)                                            |
| Difference        | integer  |                                                                                                                                    |
| Date              | date     | Jan 23, 2020 - Present                                                                                                             |
| Country_Region    | string   | Provided for all countries                                                                                                         |
| Province_State    | string   | Provided for Australia, Canada, China, Denmark, France, Netherlands, United Kingdom, United States                                 |
| Admin2            | string   | US only - County name                                                                                                              |
| Combined_Key      | string   | US only - Combination of Admin 2, State_Province, and Country_Region                                                               |
| FIPS              | integer  | US only - 5-digit Federal Information Processing Standard                                                                          |
| Lat               | double   | Latitude                                                                                                                           |
| Long              | double   | Longitude                                                                                                                          |
| Prep_Flow_Runtime | date     | Date when the ETL job ran                                                                                                          |
| Table_Names       | string   | The Table Name is used to delineate the specific Johns Hopkins datasets that were used. Values: "Time Series" or  "Daily Summary". |

# Sample CSV records from John Hopkins' Data COVID-19 Cases Dataset
|           |       |            |           |                |                |        |              |      |         |                    |                   |             | 
|-----------|-------|------------|-----------|----------------|----------------|--------|--------------|------|---------|--------------------|-------------------|-------------| 
| Case_Type | Cases | Difference | Date      | Country_Region | Province_State | Admin2 | Combined_Key | FIPS | Lat     | Long               | Prep_Flow_Runtime | Table_Names | 
| Confirmed | 0.0   | 0.0        | 2/8/2020  | US             | North Dakota   |        |              |      | 47.5289 | -99.78399999999999 | 3/29/2020         | Time Series | 
| Deaths    | 0.0   | 0.0        | 3/16/2020 | US             | Wisconsin      |        |              |      | 43.0186 | -92.3814           | 3/29/2020         | Time Series | 
| Confirmed | 6.0   | 2.0        | 3/10/2020 | US             | Kentucky       |        |              |      | 37.6681 | -85.6435           | 3/29/2020         | Time Series | 
| Deaths    | 0.0   | 0.0        | 1/26/2020 | US             | Minnesota      |        |              |      | 43.9952 | -93.9002           | 3/29/2020         | Time Series | 
| Deaths    | 0.0   | 0.0        | 3/5/2020  | US             | Hawaii         |        |              |      | 21.0943 | -157.8584          | 3/29/2020         | Time Series | 
| Deaths    | 0.0   | 0.0        | 3/19/2020 | US             | Utah           |        |              |      | 40.15   | -112.0953          | 3/29/2020         | Time Series | 
| Confirmed | 0.0   | 0.0        | 2/26/2020 | US             | New Hampshire  |        |              |      | 42.9931 | -71.82600000000001 | 3/29/2020         | Time Series | 
| Confirmed | 0.0   | 0.0        | 2/11/2020 | US             | Louisiana      |        |              |      | 29.6499 | -91.8678           | 3/29/2020         | Time Series | 
| Confirmed | 12.0  | 3.0        | 3/12/2020 | US             | Maryland       |        |              |      | 38.7849 | -77.2405           | 3/29/2020         | Time Series | 


# Queries
Using the data definiton above, we want to be able to filter records to group by date and sum case counts for deaths and infections seperately. 

### SQL for Death Sum Aggregate by Date
SELECT date, sum(Cases)
WHERE Case_Type = 'Deaths'
AND Country_Region = 'US'
GROUP BY date
ORDER BY date ASC

### Pandas for Death Sum Aggregate by Date
```python
    # Convert date column to an actual datetime data type for sorting
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data by case type and country
    df = df[(df.Case_Type == 'Deaths') &
            (df.Country_Region == 'US')]

    # Group data by date and aggregate sum of cases
    df = df[['Date', 'Cases']].groupby(['Date'], as_index=False).sum()

    # Sort data by date ascending
    df = df.sort_values(by='Date')
```

### SQL for Infections Sum Aggregate by Date
SELECT date, sum(Cases)
WHERE Case_Type = 'Confirmed'
AND Country_Region = 'US'
GROUP BY date
ORDER BY date ASC

### Pandas for Infection Sum Aggregate by Date
```python
    # Convert date column to an actual datetime data type for sorting
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data by case type and country
    df = df[(df.Case_Type == 'Confirmed') &
            (df.Country_Region == 'US')]

    # Group data by date and aggregate sum of cases
    df = df[['Date', 'Cases']].groupby(['Date'], as_index=False).sum()

    # Sort data by date ascending
    df = df.sort_values(by='Date')
```

### Death Query Validation and Data Issue Notes!
<span style="color:red;"> Death sum is a daily running total and not the number of deaths reported for each day. Dataset has two ("Daily Summary" and "Time Series" datasets) inline indicated by the Table_Names field value ("Daily Summary" or "Time Series"),  but these counts align with what the media is reporting without filtering on Time Series or Daily Summary. Noticed that the Time Series subset has a date range of 2020-01-22 to 2020-03-22 and the Daily Summary subset has a date range of 2020-03-23 to 2020-03-30. That's a little whacky, but the stats look right doing an aggregate across both sub sets.  Validated my aggregates to what is being reported by the media and lines up count and date wise. Will research more later, but probably just a data format change. Not sure. See the data validation below.

Also, On March 24, John Hopkins University stopped providing data on recovered cases due to a lack of confidence in the data. This means that they were no longer able to differentiate between active and recovered cases in the total case data, so they have removed those values from the dataset. This is a permanent change. Maybe because people are recovering and then falling ill again. Who knows, but it would be nice to be able to have access to this data.
</span>

### Results without filtering on Time Series or Daily Summary data subset filtering
SELECT Date, sum(Cases)
FROM covid_19_cases
WHERE Case_Type = 'Deaths'
AND Country_Region = 'US'
GROUP BY Date
ORDER BY Date ASC

|            |      | 
|------------|------| 
| Date       | sum  | 
| 2020-03-01 | 1    | 
| 2020-03-02 | 6    | 
| 2020-03-03 | 7    | 
| 2020-03-04 | 11   | 
| 2020-03-05 | 12   | 
| 2020-03-06 | 14   | 
| 2020-03-07 | 17   | 
| 2020-03-08 | 21   | 
| 2020-03-09 | 22   | 
| 2020-03-10 | 28   | 
| 2020-03-11 | 36   | 
| 2020-03-12 | 40   | 
| 2020-03-13 | 47   | 
| 2020-03-14 | 54   | 
| 2020-03-15 | 63   | 
| 2020-03-16 | 85   | 
| 2020-03-17 | 108  | 
| 2020-03-18 | 118  | 
| 2020-03-19 | 200  | 
| 2020-03-20 | 244  | 
| 2020-03-21 | 307  | 
| 2020-03-22 | 416  | 
| 2020-03-23 | 551  | 
| 2020-03-24 | 705  | 
| 2020-03-25 | 941  | 
| 2020-03-26 | 1208 | 
| 2020-03-27 | 1578 | 
| **2020-03-28** | **2023** | 
| 2020-03-29 | 2464 |
| 2020-03-30 | 2975 |

NPR: March 28, 202010:49 AM ET - More Than 2,000 Americans Have Now Died From The Coronavirus
**Source:** https://www.npr.org/sections/coronavirus-live-updates/2020/03/28/823106901/confirmed-cases-of-coronavirus-crest-600-000-worldwide

### Results with just the Time Series Data Subset of Data

SELECT Date, sum(Cases)
FROM covid_19_cases
WHERE Case_Type = 'Deaths'
AND Country_Region = 'US'
AND Table_Names = 'Time Series'
GROUP BY Date
ORDER BY Date ASC

|            |     | 
|------------|-----| 
| Date       | sum | 
| 2020-01-22 | 0   | 
| 2020-01-23 | 0   | 
| 2020-01-24 | 0   | 
| 2020-01-25 | 0   | 
| 2020-01-26 | 0   | 
| 2020-01-27 | 0   | 
| 2020-01-28 | 0   | 
| 2020-01-29 | 0   | 
| 2020-01-30 | 0   | 
| 2020-01-31 | 0   | 
| 2020-02-01 | 0   | 
| 2020-02-02 | 0   | 
| 2020-02-03 | 0   | 
| 2020-02-04 | 0   | 
| 2020-02-05 | 0   | 
| 2020-02-06 | 0   | 
| 2020-02-07 | 0   | 
| 2020-02-08 | 0   | 
| 2020-02-09 | 0   | 
| 2020-02-10 | 0   | 
| 2020-02-11 | 0   | 
| 2020-02-12 | 0   | 
| 2020-02-13 | 0   | 
| 2020-02-14 | 0   | 
| 2020-02-15 | 0   | 
| 2020-02-16 | 0   | 
| 2020-02-17 | 0   | 
| 2020-02-18 | 0   | 
| 2020-02-19 | 0   | 
| 2020-02-20 | 0   | 
| 2020-02-21 | 0   | 
| 2020-02-22 | 0   | 
| 2020-02-23 | 0   | 
| 2020-02-24 | 0   | 
| 2020-02-25 | 0   | 
| 2020-02-26 | 0   | 
| 2020-02-27 | 0   | 
| 2020-02-28 | 0   | 
| 2020-02-29 | 1   | 
| 2020-03-01 | 1   | 
| 2020-03-02 | 6   | 
| 2020-03-03 | 7   | 
| 2020-03-04 | 11  | 
| 2020-03-05 | 12  | 
| 2020-03-06 | 14  | 
| 2020-03-07 | 17  | 
| 2020-03-08 | 21  | 
| 2020-03-09 | 22  | 
| 2020-03-10 | 28  | 
| 2020-03-11 | 36  | 
| 2020-03-12 | 40  | 
| 2020-03-13 | 47  | 
| 2020-03-14 | 54  | 
| 2020-03-15 | 63  | 
| 2020-03-16 | 85  | 
| 2020-03-17 | 108 | 
| 2020-03-18 | 118 | 
| 2020-03-19 | 200 | 
| 2020-03-20 | 244 | 
| 2020-03-21 | 307 | 
| 2020-03-22 | 416 | 



### Results with just the Daily Summary Subset of Data
SELECT Date, sum(Cases)
FROM covid_19_cases
WHERE Case_Type = 'Deaths'
AND Country_Region = 'US'
AND Table_Names = 'Daily Summary'
GROUP BY Date
ORDER BY Date ASC

|            |      | 
|------------|------| 
| Date       | sum  | 
| 2020-03-23 | 551  | 
| 2020-03-24 | 705  | 
| 2020-03-25 | 941  | 
| 2020-03-26 | 1208 | 
| 2020-03-27 | 1578 | 
| 2020-03-28 | 2023 | 
| 2020-03-29 | 2464 | 
| 2020-03-30 | 2975 | 


# Facebook Prophet Configuration

Found that these settings match the predictions by Dr. Fauci best. 

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
    
### changepoint_prior_scale / Adjusting trend flexibility:
If the trend changes are being overfit (too much flexibility) or underfit (not enough flexibility), you can adjust the strength of the sparse prior using the input argument Changepoint_prior_scale. By default, this parameter is set to 0.05. Increasing it will make the trend more flexible. Side effect of increasing this value is that it will generally increase future trend uncertainty.

### changepoint_range:
By default changepoints are only inferred for the first 80% of the time series in order to have plenty of runway for projecting the trend forward and to avoid overfitting fluctuations at the end of the time series. This default works in many situations but not all, and can be change using the changepoint_range argument. For example, m = Prophet(changepoint_range=0.9) in Python or m <- prophet(changepoint.range = 0.9) in R will place potential changepoints in the first 90% of the time series.

### seasonality_mode:
With seasonality_mode='multiplicative', holiday effects will also be modeled as multiplicative. Any added seasonalities or extra regressors will by default use whatever seasonality_mode is set to, but can be overriden by specifying mode='additive' or mode='multiplicative' as an argument when adding the seasonality or regressor.


### Setting date data type in Pandas
Date will sort alphanumerically if you don't explicity set the data type to Date.
**Example:** df['Date'] = pd.to_datetime(df['Date'])

## Python Code

```python
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


def forecast(df, forecast_output_filename, forecast_component_output_filename):

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
    future = model.make_future_dataframe(periods=360)

    # The predict method will assign each row in future a predicted value
    # which it names yhat. If you pass in historical dates, it will provide an
    # in-sample fit. The forecast object here is a new dataframe that includes
    # a column yhat with the forecast, as well as columns for components and
    # uncertainty intervals.
    forecast = model.predict(future)

    # Plot the forecast and save it to the specified output file name
    model.plot(forecast).savefig(forecast_output_filename)

    # Plot the forecast components (seasonality graphs) and
    # save to specified output file name
    model.plot_components(forecast).savefig(forecast_component_output_filename)

    # Return the model
    return model


def main():
    # URL used to fetch COVID-19 case data in CSV format
    data_url = 'https://query.data.world/s/js7bdacf5rurkiql7nioreohprqtdx'

    # Read CSV file from file name or URL
    df = pd.read_csv(data_url)

    # Save raw COVID-19 data to a local CSV file for reference
    df.to_csv('covid-case-data.csv', index=False)

    # Get aggregated COVID-19 data grouped by date and
    # summed by Deaths in the U.S.
    df_deaths = get_aggregate_covid_data_frame(df, 'Deaths', 'US')

    # Generate the FB Prophet forecast for deaths and output forecast images
    forecast(df_deaths, 'deaths.png', 'deaths-components.png')

    # Get aggregated COVID-19 data grouped by date and
    # summed by Infections in the U.S.
    df_conf = get_aggregate_covid_data_frame(df, 'Confirmed', 'US')

    # Generate the FB Prophet forecast for deaths and output forecast images
    forecast(df_conf, 'infections.png', 'infection-components.png')

# Invoke main function
main()


```

# Setup, Execution and Output
1. git clone git@github.com:ambienthex/covid-19-stats.git
2. cd covid-19-stats
3. pip3 install pystan
4. pip3 install pandas
5. pip3 install fbprophet
6. python3 stats.py
7. Output is four image files (deaths.png, death-components.png, infections.png and infections-components.png).

Facebook Prophet can be a pain to setup sometime. Refer to Facebook Prophet's documentation if you run into issues:
https://facebook.github.io/prophet/docs/installation.html

Pandas Documentation:
https://pandas.pydata.org/docs/

# Sample Output as of March 30th, 2020 data:

## Death Forecast
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/covid-19-death-forecast.png)

## Infection Forecast
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/covid-19-infection-forecast.png)

# Conclusion
This Python generated forecast seems to be in line with the official forecast of 100,000 to 200,000 U.S. possible deaths. Take this all with a grain of salt as I have no experience with epidemiology or any medical field. It does appear that the official death toll forecast was based on a forecast using adaptive linear regression on the daily death counts. Hoping the numbers will be much less. 

Regardless of what this forecast shows, I'm slightly more optimistic with a range of 50,000 - 100,000 possible deaths if doctors and nurses don't fall ill, hospitals are not overwhelmed and effective treatments are found. The death toll could be way less. Believe healthcare workers and medical professionals will adapt and overcome to win the battle against COVID-19. Any loss of life is tragic and hope for the best. Stay safe, wash your hands and feel free to use and distribute this code however you wish. 

