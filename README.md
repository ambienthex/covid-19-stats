# Project: U.S. COVID-19 Virus Forecasting

# Abstract:
The US Center for Disease Control and Prevention data reported that between 160 and 214 million people could become infected in the United States with 200,000 to 1.7 million deaths. They stated that the epidemic could last months or even over a year.

Source: https://www.independent.co.uk/news/world/americas/coronavirus-death-toll-worst-case-scenario-millions-dead-in-us-a9402276.html

A million deaths seemed a little high to me and wanted to try forecasting the death toll to see if that was hyperbole or not. Found that Tableau is publishing COVID-19 virus data from John Hopkins to Data world. The data is updated daily at 9:00am EST and can be found at https://data.world/covid-19-data-resource-hub/covid-19-case-counts/workspace/file?filename=COVID-19+Cases.csv.

Used Python with the Pandas and Facebook Prophet data to forecast the death toll in the U.S. and found it to be in the range of 75,000 to 210,000 with a forecast line down the middle at around 140,000. This can change day to day as more deaths are confirmed and hopefully decrease as doctors and healthcare workers find treatments that work. That seemed more reasonable albiet still tragic.

On March 29th, Fauci announced That 100,000 To 200,000 Americans Could Die From The Coronavirus. A forecast using FB Prophet with the John Hopkins seems to be inline. 

Source: https://www.npr.org/sections/coronavirus-live-updates/2020/03/29/823517467/fauci-estimates-that-100-000-to-200-000-americans-could-die-from-the-coronavirus

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

# Queries
Using the data definiton above, we want to be able to filter records to group by date and sum case counts for deaths and infections seperately. 

### SQL for Death Aggregate by Date
SELECT date, sum(Cases)
WHERE Case_Type = 'Deaths'
AND Country_Region = 'US'
AND Table_Names = 'Time Series'
GROUP BY date
ORDER BY date ASC

### Pandas for Death Aggregate by Date
    # Convert date column to an actual datetime data type for sorting
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data by case type and country
    df = df[(df.Case_Type == 'Deaths') &
            (df.Country_Region == 'US') &
            (df.Table_Names == 'Time Series')]

    # Group data by date and aggregate sum of cases
    df = df[['Date', 'Cases']].groupby(['Date'], as_index=False).sum()

    # Sort data by date ascending
    df = df.sort_values(by='Date')
    
### SQL for Infections Aggregate by Date
SELECT date, sum(Cases)
WHERE Case_Type = 'Confirmed'
AND Country_Region = 'US'
AND Table_Names = 'Time Series'
GROUP BY date
ORDER BY date ASC

### Pandas for Infection Aggregate by Date
    # Convert date column to an actual datetime data type for sorting
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data by case type and country
    df = df[(df.Case_Type == 'Confirmed') &
            (df.Country_Region == 'US') &
            (df.Table_Names == 'Time Series')]

    # Group data by date and aggregate sum of cases
    df = df[['Date', 'Cases']].groupby(['Date'], as_index=False).sum()

    # Sort data by date ascending
    df = df.sort_values(by='Date')


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
If the trend changes are being overfit (too much flexibility) or underfit (not enough flexibility),you can adjust the strength of the sparse prior using the input argumENT Changepoint_prior_scale. By default, this parameter is set to 0.05. Increasing it will make the trend more flexible. Side effect of increasing this value is that it will generally increase future trend uncertainty.

### changepoint_range:
By default changepoints are only inferred for the first 80% of the time series in order to have plenty of runway for projecting the trend forward and to avoid overfitting fluctuations at the end of the time series. This default works in many situations but not all, and can be change using the changepoint_range argument. For example, m = Prophet(changepoint_range=0.9) in Python or m <- prophet(changepoint.range = 0.9) in R will place potential changepoints in the first 90% of the time series.

### seasonality_mode:
With seasonality_mode='multiplicative', holiday effects will also be modeled as multiplicative. Any added seasonalities or extra regressors will by default use whatever seasonality_mode is set to, but can be overriden by specifying mode='additive' or mode='multiplicative' as an argument when adding the seasonality or regressor.


### Setting date data type for pandas
Date will sort alphanumerically if you don't explicity set the data type
example: df['Date'] = pd.to_datetime(df['Date'])
