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

