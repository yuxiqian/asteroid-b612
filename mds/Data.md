# Data Analysis
## Data Origin
The major data source is the `MCM_NFLIS_Data.xlsx` file. It contains all incidents involved with narcotic analgesics and heroin occurring since 2010 to 2017. The first phase of problem requires focusing on this part of data, temporarily leaving the social-economical dataset aside.
## Main Factors
There’s some data factor in this sheet particularly attracting, which helps a lot in figuring out the drug crisis spreading amount the northeast U.S.
* Substance
	The main substances of all incidents were provided, hence we may separately analyze them to validate the model.
* Case Count
	Many drugs involved in all these incidents, but they’re not equally significant. The reports’ count recording the troubles they made can be a convincing factor to determine how influential one drug is.
* County Location
	The specific county name in OH, KY, WV, VA and PA are provided in detail. Thanks to [Simple Maps Corp.][1]’s great work and generous contribution, we could get accurate longitude and latitude to locate a single county. That would be a great help in visualizing our analysis.
## Parsing
There are several important factors that affects the modeling procedure. To clarify the argument parsing procedure, here’s a brief table about the variables that we’re aware of:
* Case History
	There’re accurate data recording how many cases involving with drugs occurred in each county since 2010 until 2017.
* Geography Location
	Not only grabbing the location of each county, but each county’s 3 nearest county neighbors’ case history is also recorded to build a “spreading” model.
* Population Density
	Each year’s population of every county is also provided in the “extra data pack”. Combining them with the geography dataset, we can get the approximate density level of each county, which would be very helpful in solving Problem 2.
## Error Handling
Thanks to the high quality database, there’s no much obstacle finding out informations above. But it should be noticed that some names of counties are shared by two different states (for example, Adams County in Ohio and Adams County in Pennsylvania). To avoid conflicting analyzing result, both state name and county name should be used to identify a county. Hence the county data can be ensured unique.

[1]:	https://simplemaps.com "Simple Maps Corp."