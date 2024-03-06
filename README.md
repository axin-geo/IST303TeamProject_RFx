# IST303TeamProject_RFx
1. Team Members
  My team members are Mohammed Alfawzan and Akhilesh Prakash Rajeswari.

2. Come up with a concept for your application.
  ArcGIS offers users to ability to leverage raster imagery data from data extraction, preparation, visualization to analysis. 
  On ArcGIS Pro, these imagery capabilities are inplemented as a group of raster functions, divided to various categories based on their application fields. 
  Each raster function has a set of parameters and its associated required data type.

  For an example of an raster function, check out documentation on clip raster function (https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/clip-function.htm). 

  **In each release of ArcGIS Pro, the raster functions (along with their parameters and its required data types) might go through some tweaks here and there. 
  We need something like a web database app that tracks the development of raster function changes across different releases of Pros. This web app also serves as a reference point for the development for function ownership and POC. **
   
3. Identify all the relevant project stakeholders.

  The key stakeholder in this project is Imagery/Raster team at Esri, and whoever that uses raster functions internally in Esri (could be other develpoment teams).

4. Create an initial set of project requirements expressed as user stories. User stories must have estimates of completion times.
   User Journeys: Shaping the Next Gen of Raster Functionality!
  a) (TE: one week) As a user, I want to have a database of all raster functions and their parameters in all the previous ArcGIS Pro releases
  b) (TE: one week) As a user, I want to have a Function property Lookup page that offers a filtering and search capability that finds the specific function I look for
  c) (TE: one week) As a user, I want to have a Tool owner page that allows me to assign a raster function to a function owner (developer)  
  d) (TE: one week) As a user, I want to have a comparison page that generates the changes in between releases

   
# Notes

All features
  0. Data preparation
    1. Create Bogus data for XML format file (ADRasterRegistry.xml) which contains the info about rfx.
    2. creae a table that hold rfx owners on the page

  1. a database which stores all raster functions and their parameters in all the current ArcGIS Pro release
    - I want my dataset to have 3 tiers. 
        First tier, at the top is the database. 
        At the second tier is ArcGIS version (this could be 2.1, 2.2, 2.4, or the latest 3.1). 
        At the 3rd tier are the raster functions.
    - can use sql tables or json.
    - the concept of nested table does not exist in SQL. But could use foreign key.
    - json might be the best way to store our data

    Task 1.1 get rfx and their properties from a xml format data source

    Task 1.2 write the rfx info to a json file. One json file corresponds to one version of ArcGIS software


  2. a Function property Lookup page that offers a filtering and search capability that finds the specific function I want to look for

  3. A csv table that stores information about rfx_id, owner, email, team
