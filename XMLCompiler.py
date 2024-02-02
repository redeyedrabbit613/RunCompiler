# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:43:19 2023

@author: John Wang
"""
import glob as gl
import xml.etree.ElementTree as ET

#define the pattern to search for .txt files
pattern = '\\OMNIOME.LOCAL\Shares\Shared\systems integration\__SystemsIntegration_Team_Members\_JW\Onso\OCG\Flow Cell Cluster Density Investigation\OCGs\OCG1\10-1.24 run folder\20??????_FC???????-BCC_OCG01_???\Logs\FC???????-BCC_metadata.xml'

#use glob to find the files matching the pattern
xml_files = gl.glob(pattern)

# Function to read attribute for a specific value
def read_attribute_for_value(xml_file, element_tag, attribute_name, target_value):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Iterate over elements with the specified tag
    for elem in root.iter(element_tag):
        # Check if the element has the target value for the specified attribute
        if elem.get(attribute_name) == target_value:
            return elem.get(attribute_name)
    
    return None  # If target value not found

# Specify the element tag, attribute name, and target value
element_tag = 'ClusterRunMetadata'
attribute_name = 'Fragment_FilePath'
target_value = 'STANDARD'

# Iterate over XML files and read attribute for the specific value
for xml_file in xml_files:
    attribute_value = read_attribute_for_value(xml_file, element_tag, attribute_name, target_value)
    if attribute_value:
        print(f"In {xml_file}, attribute '{attribute_name}' for '{element_tag}' with value '{target_value}' is '{attribute_value}'")
    else:
        print(f"In {xml_file}, attribute '{attribute_name}' for '{element_tag}' with value '{target_value}' not found")

        
"""
Spyder Editor

This is a temporary script file.
"""

