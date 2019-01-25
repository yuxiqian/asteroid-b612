# Data Analysis
## Data Origin
The major data source is the `MCM_NFLIS_Data.xlsx` file. It contains all incidents involved with narcotic analgesics and heroin occurring since 2010 to 2017. Hopefully it can figure out the drug crisis spreading amount the northeast U.S.
## Obvious Factors
Some Factors are provided directly and can be grabbed at the first time.
* Substances of Drugs
	The main substances of all incidents were provided, hence we may separately analyze them to validate the model.
* Case Count
	Many drugs involved in all these incidents, but they are not equally significant. The reported count recording the troubles they made can be a convincing factor to determine how influential one drug is.
* Geography Location
	The specific county name in OH, KY, WV, VA, and PA are provided in detail. Thanks to [Simple Maps Corp.][1] for their generous contribution, we could get accurate longitude and latitude to locate a single county. That would be a great help in visualizing our analysis.
## Indirect Factors
There are several important factors that affects the modeling procedure but not provided directly. 
* Case History
	There are accurate data recording how many cases involving with drugs occurred in each county since 2010 until 2017. Putting individual case counts altogether would allow them make more sense.
* Neighbor Counties
	Besides grabbing the location of each county, their 3 nearest neighbor counties and their case history is also recorded to build a drug crisis spreading model.
* Population Density
	The annual population of each county is also provided. Combining them with the area information of each county, we can diverse each county into  several approximate density levels. That would be helpful in solving Problem 2.
## Resulting Dataset
* 451 Unique Counties
* 69 Kinds of Substances
* 24062 Case Recordings
## Error Handling
Thanks to the high quality database, there is no much difficulty finding out informations above. But it should be noticed that some names of counties are shared by two different states (for example, Adams County in Ohio and Adams County in Pennsylvania). To avoid conflicting analyzing result, both state name and county name should be used to identify a county. Hence the county data can be ensured unique.

[1]:	https://simplemaps.com "Simple Maps Corp."