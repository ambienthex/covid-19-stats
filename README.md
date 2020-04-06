# Project: U.S. COVID-19 Virus Forecasting
This GIT repo contains a simple Python(3) script (stats.py) that can be used to forecast COVID-19 deaths and infections by country and state using case data from John Hopkins University. Various forecast and stats graphs for deaths and infections are generated. The stats.py script pulls the current John Hopkins COVID-19 CSV case data, transforms and sum aggregates daily death counts grouping by date using Pandas, and generate a forecast using Facebook's Prophet library. Data is updated daily at 9a.m. 

Keep in mind the forecast can change for better or worse as new case data is added day to day. Forecast will get better as more data is available and hope to see the forecast go the other way sooner rather than later. May have to tweak the  changepoint_prior_scale and changepoint_range for more accurate forecasts depending on country specified. 

# Outputs for a specified country
1. Open covid-19-stats.htm after running script to see all stats below. 
2. Total death count graph.
3. Daily death count graph. 
4. Total infection count graph.
5. Daily infection count graph.
6. Total death count forecast graph. 
7. Daily death count forecast graph.
8. Total infection count forecast graph.
9. Daily infection count forecast graph. 
10. Downloaded stats; covid-case-data.csv
11. stats-by-date.csv (Date,Running Death Count,Daily Deaths,Running Infection Count,Daily Infections).

# Setup, Execution and Output
1. git clone git@github.com:ambienthex/covid-19-stats.git
2. cd covid-19-stats
3. pip3 install pystan
4. pip3 install pandas
5. pip3 install fbprophet
6. pip3 insttall beautifulsoup4
7. python3 stats.py for U.S. data or python3 stats.py -c "Italy"
9. After running the stats.py script, can launch "covid-19-stats.htm" in a browser to see all the graphs together.
10. Raw case data is also written to the "covid-case-data.csv" file which is overwritten on each run.
11. Filter by country using the -c option (e.g. python3 stats.py -c "US"). Can filter by a U.S. state with (e.g. python3 stats.py -c "US" -p "New York"). Province filter only works for U.S. data.
12. Helper command line option available to list all valid Country names: python3 stats.py -cl

Facebook Prophet can be a pain to setup sometime. Refer to Facebook Prophet's documentation if you run into issues:
https://facebook.github.io/prophet/docs/installation.html

**Facebook's Prophet Documentation:** https://facebook.github.io/prophet/

**Pandas Documentation:** https://pandas.pydata.org/docs/


# Sample Graphs

## Running Total Italy. Death Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-deaths-running-total-line-graph.png)

## Daily Italy Death Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-deaths-by-day-line-graph.png)

## Running Total Italy Infection Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-infections-running-total-line-graph.png)

## Daily Italy Infection Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-infections-by-day-line-graph.png)

## Facebook Prophet COVID-19 Italy Daily Death Forecast
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-daily-death-forecast.png)

## Facebook Prophet COVID-19 Italy Total Death Forecast
Forecast is currently off in never never land past May with limited data and no limiting factors. Italy is on a daily death count decline as of early April.
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-total-death-forecast.png)

## Facebook Prophet COVID-19 Italy Total Infection Forecast
Forecast is currently off in never never land past May with limited data and no limiting factors. 
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-total-infection-forecast.png)

## Facebook Prophet COVID-19 Italy Daily Infection Forecast
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/italy-covid-19-daily-infection-forecast.png)

## Running Total U.S. Death Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-deaths-running-total-line-graph.png)

## Daily U.S. Death Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-deaths-by-day-line-graph.png)

## Running Total U.S. Infection Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-infections-running-total-line-graph.png)

## Daily U.S.Infection Count Graph
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-infections-by-day-line-graph.png)

## Facebook Prophet COVID-19 U.S. Total Death Forecast
Forecast is currently off in never never land past May with limited data and no limiting factors.  Slope could be much less steep when daily death counts start to drop in May.
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-total-death-forecast.png)

## Facebook Prophet COVID-19 U.S. Daily Death Forecast
Forecast is currently off in never never land past May with limited data and no limiting factors. Forecast could start a downward trend when daily infection counts start to drop in May.
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-daily-death-forecast.png)

## Facebook Prophet COVID-19 U.S. Total Infection Forecast
Forecast is currently off in never never land past May with limited data and no limiting factors. Slope could be much less steep when daily infection counts start to drop in May.
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-total-infection-forecast.png)

## Facebook Prophet COVID-19 U.S. Daily Infection Forecast
Forecast is currently off in never never land past May with limited data and no limiting factors.  Forecast could start a downward trend when daily infection counts start to drop in May.
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-daily-infection-forecast.png)


```sql
SELECT date, sum(Cases) deaths
FROM covid_19_cases
Where case_type = 'Deaths'
AND date = '2020-04-01'
group by date
order by date
RESULT: 46,806 COVID deaths.
```

**Note**: Cases are cumulative / additive. This is the correct query to get the global total death count in the John Hopkins dataset.  Included the link to the raw data if you want to try it yourself and review. Read the documentation on the dataset and this is correct.


# Abstract:
**On March 15th, 2020**, the US Center for Disease Control and Prevention reported that between 160 and 214 million people could become infected with COVID-19 in the United States with 200,000 to 1.7 million deaths. They stated that the epidemic could last months or even over a year.

**Source**: https://www.independent.co.uk/news/world/americas/coronavirus-death-toll-worst-case-scenario-millions-dead-in-us-a9402276.html

Over a million U.S. deaths seemed too high and wanted to attempt a basic forecast of the death toll without the epidemiology factors I'm not familiar with to determine if those figures were media hyperbole or not. Tableau is publishing COVID-19 virus case data from John Hopkins University to Data world. The data is updated daily at 9:00am EST and can be found at https://data.world/covid-19-data-resource-hub/covid-19-case-counts/workspace/file?filename=COVID-19+Cases.csv

Python with the Pandas, Facebook Prophet library and the John Hopkins University COVID-19 case data was used to try to forecast the U.S. death toll and it was found to be in the range of 75,000 to 210,000 possible deaths as of March 30th. This can change day to day for better or worse and hopefully decrease soon as doctors and healthcare workers find treatments that work. Albeit still tragic, this seemed more reasonable than the previously forecasted 200,000 to 1.7 million  possible U.S. deaths reported by the US Center for Disease Control and Prevention and the media. I am more optimistic with a range of 50,000 - 100,000 possible deaths regardless of what the forecast shows as it doesn't account for things that will help or slow the situation. The death toll could be way less if doctors and nurses don't fall ill, hospitals are not overwhelmed and effective treatments are found. Any loss of life is tragic and hope for the best. Believe healthcare workers and medical professionals will adapt and overcome to win the battle against COVID-19.

**On March 29th**, Dr. Anthony Fauci, Director of NIAID(National Institute of Allergy and Infectious Diseases) announced that 100,000 to 200,000 Americans could die from the COVID-19 which contradicted the 200,000 to 1.7 million range provided by the US Center for Disease Control and Prevention.

**Source**: https://www.npr.org/sections/coronavirus-live-updates/2020/03/29/823517467/fauci-estimates-that-100-000-to-200-000-americans-could-die-from-the-coronavirus

Using Facebook Prophet and the John Hopkins Data Set, here's the forecast for March 29th:
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-death-forecast-2020-03-29.jpg)

**On March 31st**, Forecast jump... President Donald Trump and Dr. Deborah Birx, the coordinator of the White House coronavirus task force warned Americans to brace for a “hell of a bad two weeks” ahead as the White House projected there could be 100,000 to 240,000 deaths in the U.S. from the coronavirus pandemic even if current social distancing guidelines are maintained.

**Source**: https://apnews.com/6ed70e9db88b80439a087fdad8238009

**April 2nd, 2020**
World Health Organization (WHO) estimates that the flu kills 290,000 to 650,000 people per year globally. We are into month four of a global Corona virus crisis and have 46,806 deaths globally. Could get worse, but something for comparison so far.  Death count may be lower than forecasted with the extreme measures taken to control the virus. Regardless of what the forecasts show, I'm feeling a bit more optimistic about the death count being lower than forecasted  These are the official numbers and not my assumption. 

**April 2nd, 2020**
Experts, Trump’s advisers doubt White House’s 240,000 coronavirus deaths estimate. Jeffrey Shaman, a Columbia University epidemiologist whose models were cited by the White House, said his own work on the pandemic doesn't go far enough into the future to make predictions akin to the White House fatality forecast. "I think we can come in under 100,000 deaths. I do," Shaman said. "The jury is not yet in on this.".

**Source**: https://www.msn.com/en-us/news/us/experts-trumps-advisers-doubt-white-houses-240000-coronavirus-deaths-estimate/ar-BB1263eT

**April 5, 2020**
Bill Gates said the United States will see far fewer than the White House forecast of between 100,000 and 240,000 coronavirus-related deaths if U.S. citizens stay home.
**Source**: https://www.cnbc.com/2020/04/05/bill-gates-coronavirus-pandemic-a-nightmare-scenario.html


Using Facebook Prophet and the John Hopkins Data Set, here's the forecast on March 31st:
![image](https://raw.githubusercontent.com/ambienthex/covid-19-stats/master/git-images/covid-19-death-forecast-2020-03-31.png)


# Assumptions

Thought I could use the infection case data with the death case data somehow in generating a forecast of possible deaths, but it's been reported that the infection data is almost meaningless to epidemiologists and incomplete. Death seems to be the only absolute in the data. It appears Dr. Fauci's estimate was possibly generated withregression (Bayesian-influenced generalized additive model, a regression of smooth terms) forecast on the aggregate sum of daily death counts grouped by date, so giving it a go with Facebook Prophet to see how it compares and it's in the range. They may have done something different. Who knows, but it nearly matches official forecasts that are changing day to day.

**On March 3rd, 2020**, Steve Goodman, a professor of epidemiology at Stanford University, said, “The infection numbers are almost meaningless. There is a huge reservoir of people who have mild cases, and would not likely seek testing. The rate of increase in positive results reflect a mixed-up combination of increased testing rates and spread of the virus."

**Source**: https://www.bloomberg.com/opinion/articles/2020-03-28/confirmed-coronavirus-cases-is-an-almost-meaningless-metric

Regardless what the forecasts show, I'm slightly more optimistic with a range of 50,000 - 100,000 possible deaths. Forecast doesn't account for things that will help or slow the situation(e.g. positive changes, behavior changes, effective social distancing and effective treatments that may emerge). The death toll could be way less if doctors and nurses don't fall ill, hospitals are not overwhelmed and effective treatments are found. Any loss of life is tragic and hope for the best. Believe healthcare workers and medical professionals will adapt and overcome to win the battle against COVID-19.


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
