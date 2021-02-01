# **Project title:** Job Coverage In the Transition from Fossil Fuel to Clean Energy

## **Roles**
### Suzanne
#### Title: Data co-wrangler / writing muscle
#### Role: Renewable energy data
#### Contribution:
    * Will help write up assignments as needed
    * Work with and develop visualizations for all renewable energy related data sets
    * Will meet with TAs/Yoh as needed to resolve problems with Python coding
    * Project management / organizing meetings / ensuring team meets deadlines

### Matt
#### Title: Data finder / demographics mapper
#### Role: Demographic data
#### Contribution:
    * Find relevant datasets for our research questions
    * Map and visualize demographic data, including race/ethnicity, income, and wages
    * Help write up assignments
    * Manage group repo

### Rachel
#### Title: Data wrangler / project management support 
#### Role: Fossil fuel data set
#### Contribution: 
    * Work with and develop relevant visualizations for all fossil fuel related data sets
    * Support document development related to group assignments
    * Support project management for group assignments 
    * Co-create and collaborate on research questions 
    * Support python/dataset troubleshooting 
    
## **Status update**

We met this weekend to discuss the project, and compared notes after respective office hours with Yoh/Chris. In light of feedback we received, we are revising our project slightly to come up with a more provocative question. Initially, we planned to study the availability and quality of fossil fuel jobs and renewable energy jobs in California by county. However, the feedback we received made us question how much nuance we could bring to that question, given the data we have to work with--it might end up being more of a descriptive project than making a strong argument. 

After further discussion yesterday, we now plan to look at the ratio between the number of jobs and units of energy produced by a given fossil fuel power plant, in order to draw conclusions about the number of clean energy power plants that will need to replace them, and whether these clean energy power plants will provide the same level of employment. We will thus need to figure out how many units of energy are produced per county at fossil fuel plants, how many jobs that corresponds to, how much renewable energy will be needed to replace this energy, and how many jobs come along with those power plants. The mood still seems enthusiastic and excited to work on the project and produce a meaningful product.

## **Data update**

We’ve compiled almost all of the data we need. We have data on CA county demographics, fossil fuel and renewable energy jobs per county, the locations and output (size) of power plants across the state, and the anticipated retirement year of those plants. Ideally we’d find a source that identifies the number of jobs associated with clean energy development (for example, 10 jobs for every 1 MW of clean energy added), but if we can’t find that we can estimate it based on the clean energy jobs per energy output per county.

[CA Energy Commission Power Plants Data](https://cecgis-caenergy.opendata.arcgis.com/datasets/california-power-plants/data?geometry=-154.211%2C31.065%2C-75.461%2C43.271). This dataset provides the location of every power plant in California, both renewable and fossil fuel. It contains data on plant emissions and lifespan as well. This data will allow us to map power plants across the state by type.
[2018 County Business Patterns Data](https://data.census.gov/cedsci/table?g=0400000US06.050000&d=ANN%20Business%20Patterns%20County%20Business%20Patterns&n=2111%3A2211%3A2212%3A32411%3A486&tid=CBP2018.CB1800CBP&hidePreview=true). This County Business Patterns (CBP) data provides employment numbers among fossil fuel and renewable energy sectors across all counties in California. We narrowed the CBP data down to five relevant NAICS codes: 2111 (Oil and gas extraction), 2211 (Electric power generation), 2212 (Natural gas distribution), 32411 (Petroleum refineries), and 486 (Pipeline transportation). 
[CalEnviroScreen 3.0 Data](https://oehha.ca.gov/media/downloads/calenviroscreen/document/ces3results.xlsx). Using data from CalEnviroScreen will enable us to situate the fossil fuel and renewable energy sectors with larger social demographics. This dataset is especially useful for understanding the spatial distribution of energy resources in the state and provides an explicit focus on the environmental justice dimensions of energy production.
Data from [“The future of United States fossil fuel-fired electricity”](http://emilygrubert.org/wp-content/uploads/2020/12/fossil_transition-script.html). This dataset includes jobs and output data for power points across the US. We plan to narrow these data down to California and use them in our analysis of understanding how many fossil fuel jobs will be lost in a given county in the future, and how many will need to be replaced by renewable energy jobs to meet energy demands. This dataset overlaps with the CA Power Plants data, but is easier to use and already compiled across our areas of interest.

## **Concerns**

#### Major Concerns
    * Conducting deeper analysis beyond descriptive research: Our Week 3 Assignment focused on visualizing where clean energy and fossil fuel jobs are located in California. Our challenge moving forward will be to shift our research question to produce deeper insights.
    * Need for additional, relevant datasets: We have shifted our research question to investigate how many clean energy jobs will be needed to replace fossil fuel jobs. We’ll need additional information beyond the datasets we’ve already found to answer: 1) how many jobs per megawatt produced per county at fossil fuel plants, 2) how many renewable energy jobs will be needed to produce the same amount of energy. 
#### Minor Concerns:
    * Data cleaning: While we have found some datasets related to our research question, they require significant cleaning to make them usable for our purposes. Data cleaning has been challenging thus far and sometimes involves techniques we have yet to learn in class. 
