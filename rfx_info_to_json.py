import arcpy
# import arcpy ## installing Arcpy requires Pro to be installed 
# ArcGIS Pro installation info can be found at "\ArcGIS\Pro\binArcGIS.Installation.xml"

import os
import datetime
import xml.etree.ElementTree as ET
import json


# get version 
# https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/getinstallinfo.htm
verinfo = arcpy.GetInstallInfo()

PRO = True

# collect all arcgis version info
arcgis_version = {}
arcgis_version['version'] = verinfo["Version"]
arcgis_version['productName'] = verinfo["ProductName"]
if arcgis_version['productName'] == "Server":
    if PRO:
        arcgis_version['productName'] = "Server-AO11"

arcgis_version['buildNumber'] = verinfo["BuildNumber"]
arcgis_version['buildDate'] = datetime.datetime.fromtimestamp(
                                    os.path.getmtime(os.path.join(
                                    verinfo['InstallDir'], 'bin', 'GPCoreFunctions.dll'))).strftime("%Y-%m-%d")
arcgis_version['comment'] = ""

# create rfx_info directory to store json files for all ArcGIS versions
if not os.path.exists("rfx_info"):
    os.mkdir("rfx_info")

# initialize json file name
out_name = "rfx_info\\rfx_info{0}_{1}_{2}.json".format(
                    arcgis_version["productName"],
                    verinfo["Version"].replace(".", ""),
                    verinfo["BuildNumber"])


# Read XML file that contains rfx info at "\ArcGIS\Pro\bin\Extensions\DataSourcesRaster"

# XML elements become JSON objects.
# XML attributes become JSON properties.
# Nested XML elements become nested JSON objects or arrays.

# Define the path to your XML file
xml_file_path = r'C:\Program Files\ArcGIS\Pro\bin\Extensions\DataSourcesRaster\ADRasterRegistry.xml'

# Define the output JSON file name
json_file_path = out_name

# Namespace mapping as extracted from the user's XML structure
namespaces = {'ns': 'http://schemas.esri.com/Raster/Registry'}

def parse_rfxDefinition(element):
    """
    Recursively converts an XML element and its children into a dictionary,
    removing namespace URIs from the keys.
    """
    # Helper function to remove namespace from tag
    def strip_namespace(tag):
        return tag.split('}', 1)[-1] if '}' in tag else tag
    
    # Start with the element's attributes, stripping namespaces from keys
    rfx_def = {strip_namespace(k): v for k, v in element.attrib.items()}
    
    for child in element:
        key = strip_namespace(child.tag)
        if list(child):  # If the child has further nested elements
            value = parse_rfxDefinition(child)
        else:  # If the child has no nested elements
            value = child.text.strip() if child.text else None
        if key in rfx_def:  # If the key already exists, ensure it's a list
            if not isinstance(rfx_def[key], list):
                rfx_def[key] = [rfx_def[key]]
            rfx_def[key].append(value)
        else:
            rfx_def[key] = value
    
    return rfx_def

if os.path.exists(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Initialize an empty list to hold dictionaries for each rfxDefinition
    rfx_definitions = []

    # Loop through each rfxDefinition element, accounting for the namespace
    for rfxDefinition in root.findall('.//ns:rfxDefinition', namespaces=namespaces):
        rfx_definitions.append(parse_rfxDefinition(rfxDefinition))
    
    # Create a new dictionary that includes both arcgis_version and rfx_definitions
    output_data = {
        'arcgis_version': arcgis_version,
        'rfx_definitions': rfx_definitions
    }
    
    # Serialize the new dictionary to JSON
    with open(json_file_path, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)
        
    print(f"Converted XML to JSON and saved to {json_file_path}")
else:
    print(f"File not found: {xml_file_path}")

