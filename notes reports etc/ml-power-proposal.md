# Energy Forecasting Project for Intro to Machine Learning Spring 2024

We are interested in forecasting energy consumption within the US. Our initial approach will be to model consumption at the state and potentially sectoral level using electricity and weather time series data. While we have not determined an exact policy question to answer, potential options include identifying situations that require additional energy infrastructure, are at risk of energy shortages, and are at risk of energy price spikes.

## US Energy Information Administration

The [US Energy Information Administration (EIA)](https://www.eia.gov/) publishes US power and electricity data by power source (eg electricity broken down by generation source, primary use of natural gas, primary use of petroleum oil) by month and state going back over 2 decades. Sparser data is available going back as far as 1970. Furthermore, powerplant-specific data is data in many cases going back as far as 2001. While we have not settled on a specific set of time series to to use to construct our dataset, we are tentatively considering using the following:

[Form EIA-923](https://www.eia.gov/electricity/data/eia923/) collects detailed monthly and annual electric power data on electricity generation, fuel consumption, fossil fuel stocks, and receipts at the power plant level. The data series goes back to 2001

Forms EIA-861M and EIA-826 collect monthly electricity sales data at the state-sector level. A summary of the more recent data is available [here](https://www.eia.gov/electricity/data/eia861m/xls/sales_revenue.xlsx).

The EIA offers a number of other datasets, including [renewable energy production](https://www.eia.gov/renewable/data.php), [net metering, which is related to EIA-861M](https://www.eia.gov/electricity/data/eia861m/#netmeter), and [others](https://www.eia.gov/totalenergy/data/monthly/index.php).

## Weather (via NOAA)

The [National Oceanic and Atmospheric Administration (NOAA)](https://www.noaa.gov/) offers a number of datasets that can be used to construct a weather time series.

The files are available for bulk download [here](https://www.ncei.noaa.gov/pub/data/cirs/climdiv/).