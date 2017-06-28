# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Chapter2Model1.py
# Created on: 2017-01-26 04:26:31.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Bus_Stops = "C:\\Projects\\SanFrancisco.gdb\\SanFrancisco\\Bus_Stops"
CensusBlocks2010 = "C:\\Projects\\SanFrancisco.gdb\\SanFrancisco\\CensusBlocks2010"
Inbound71 = "C:\\Projects\\SanFrancisco.gdb\\Chapter2Results\\Inbound71"
Inbound71_400ft_buffer = "C:\\Projects\\SanFrancisco.gdb\\Chapter2Results\\Inbound71_400ft_buffer"
Intersect71Census = "C:\\Projects\\SanFrancisco.gdb\\Chapter2Results\\Intersect71Census"

# Process: Select
arcpy.Select_analysis(Bus_Stops, 
                      Inbound71, 
                      "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'")

# Process: Buffer
arcpy.Buffer_analysis(Inbound71, 
                      Inbound71_400ft_buffer, 
                      "400 Feet", "FULL", "ROUND", "NONE", "")

# Process: Intersect

arcpy.Intersect_analysis([Inbound71_400ft_buffer,CensusBlocks2010],
                         Intersect71Census, "ALL", "", "INPUT")
