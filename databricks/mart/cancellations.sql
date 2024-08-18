-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_dev;

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS Dim_Cancellation (
  code STRING,
  description STRING
) USING DELTA LOCATION '/mnt/mart_datalake/Dim_dev'

-- COMMAND ----------

INSERT OVERWRITE Dim_Cancellation
SELECT 
code 
,description 
FROM  cleansed_dev.Cancellation
