# Data Analysis
## Data Origin
The major data source mentioned in Problem One is the `MCM_NFLIS_Data.xlsx` file. It contains all incidents involved with narcotic analgesics and heroin occurring since 2010 to 2017. Hopefully it can figure out the drug crisis spreading amount the northeast U.S.
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
	Besides grabbing the location of each county, their several nearest neighbor counties and their case history is also recorded to build a drug crisis spreading model.
* Population Density
	The annual population of each county is also provided. Combining them with the area information of each county, we can diverse each county into  several approximate density levels. That would be helpful in solving Problem 2.
## Resulting Dataset
* 451 Unique Counties
* 69 Kinds of Substances
* 24062 Case Recordings
## Error Handling
Thanks to the high quality database, there is no much difficulty finding out informations above. But it should be noticed that some names of counties are shared by two different states (for example, Adams County in Ohio and Adams County in Pennsylvania). To avoid conflicting analyzing result, both state name and county name should be used to identify a county. Hence the county data can be ensured unique.
## Spreading Index
To describe the spreading process quantitatively, opioid and heroin case report data during these years and the location data of all counties are introduced to fit the equation mentioned above.
According to general intuition, two counties at long distance might not lead to major spreadings. So for one specific county, only those data from the nearest `k` counties can be used in model fitting. Considering the fitting efficiency, `k` should be no more than 10.
The fitting result should go beyond a threshold value to make sense. Any lower spreading index should be treated as disturbance and ignored. By judging the value of spreading index, a weighted directed graph can be constructed to analyze the origin of any single kind of drugs.
## Considering Eco-Social Factors
In Problem 1 solving phase, only opioid and heroin related case data are applied in model building, but the total amount of drug abusing cases are provided separately. Hence those spreading factor above can’t be directly used here, and another spreading index fitting for general drug abusing cases is necessary.
Performing AHP needs data series of various factors. Eco-Social Factor Data in 2017 were not provided, so the fitting would be limited between 2010 and 2016 under this phase.
In the modeling part of Problem 1 solution, we have determined a best `k` value that optimizes the fitting procedure. It is assumed that the same `k` should also provide the optimized result, so as to reduce excessive fitting calculations.

[1]:	https://simplemaps.com "Simple Maps Corp."