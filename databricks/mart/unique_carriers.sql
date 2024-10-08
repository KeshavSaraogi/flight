-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_devs;

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS Dim_UniqueCarrier (
  code STRING,
  description STRING
) USING DELTA LOCATION '/mnt/mart_datalake/Dim_UniqueCarrier'

-- COMMAND ----------

INSERT OVERWRITE Dim_UniqueCarrier
SELECT 
code 
,description 

FROM  cleansed_dev.Unique_Carriers
