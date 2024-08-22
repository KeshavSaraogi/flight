# Databricks notebook source
dbutils.widgets.text("Layer_Name","")
Layer_Name=dbutils.widgets.getArgument("Layer_Name")

# COMMAND ----------

Notebook_Path_Json = {
    "Raw": ["/GeekCoders/Raw_Sourcing/Raw_Plane"],
    "Cleansed": [
        
            "/GeekCoders/Cleansing/Airlines",
            "/GeekCoders/Cleansing/Airport",
            "/GeekCoders/Cleansing/Cancellation",
            "/GeekCoders/Cleansing/Flight",
            "/GeekCoders/Cleansing/Plane",
            "/GeekCoders/Cleansing/Unique_Carrier",
        
    ],
    "Data_Quality_Cleansed": 
        ["/GeekCoders/Data_Quality_Notebook/Cleansing_Data_Quality"]
    ,
    "Mart": 
        [
            "/GeekCoders/Mart/Dim_Airlines",
            "/GeekCoders/Mart/Dim_Airport",
            "/GeekCoders/Mart/Dim_Plane",
            "/GeekCoders/Cleansing/Dim_UniqueCarrier",
            "/GeekCoders/Mart/Dim_Cancellation",
            "/GeekCoders/Mart/Reporting_Flight",
            
        
    ],
    "Data_Quality_Mart":["/GeekCoders/Data_Quality_Notebook/Excecute_Mart_Data_Quality"]
}

# COMMAND ----------

for notebook_paths in Notebook_Path_Json[Layer_Name]:
    dbutils.notebook.run(notebook_paths,0)
