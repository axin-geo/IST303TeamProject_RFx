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
  b) (TE: one week) As a user, I want to have a Tool owner page that allows me to assign a raster function to a function owner (developer)  
  c) (TE: one week) As a user, n the rfx owner page, I want to be able to search and fileter based on rfx name, owner name. I want to be able to update/create owner, email and team info for raster functions.
  d) (TE: two week) As a user, I want to be able to compare 2 releases ans see if there are functions, parameters added or removed from one version of the software.

   
# Notes

All features

 a) (TE: 1 week) As a user, I want to have a database of all raster functions and their parameters in all the previous ArcGIS Pro releases
  1. create the index page
  2. Retrieve rfx information (stored in xml) from installed ArcGIS Pro in a particular software version.
  3. Convert the rfx info stored in xml to a json format
  4. Create RFX info page via flask. User needs to input the rfx name and Pro version, and server can returns the rfx info based on the input criterion back to the client browser.
  (- I want my dataset to have 3 tiers. 
        First tier, at the top is the database. 
        At the second tier is ArcGIS version (this could be 2.1, 2.2, 2.4, or the latest 3.1). 
        At the 3rd tier are the raster functions.
    - can use sql tables or json.
    - the concept of nested table does not exist in SQL. But could use foreign key.
    - json might be the best way to store our data)


  b) (TE: one week) As a user, I want to have a Tool owner page that allows me to assign a raster function to a function owner (developer)  
    1. create a SQL database with a table of columns rfx_id, owner, email, team
    2. create the RFX owner page
    3. The table uses the latest version of software to include all the rfxs up to date

  c) (TE: one week) As a user, n the tool owner page, I want to be able to search and fileter based on rfx name, owner name. I want to be able to update/create owner, email and team info for raster functions.
    1. Allow users to edit/update owner name, email and team
    2. a filter box on top of table to filter rows based on keyboards

  d) (TE: two  week) (TE: two week) As a user, I want to be able to compare 2 releases ans see if there are functions, parameters added or removed from one version of the software.
    1. create a comparison route page
    2. User needs to input the base Pro version, comparing Pro version. Server retreives the rfx info from the json files for requested versions. And do a comparison / diff. return results.

   