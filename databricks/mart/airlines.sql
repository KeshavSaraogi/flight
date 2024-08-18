-- Databricks notebook source
-- MAGIC %sql
-- MAGIC use mart_dev;

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS airlines (
  iata_code STRING,
  icao_code STRING,
  name STRING
) USING DELTA LOCATION '/mnt/mart_datalake/airlines'

-- COMMAND ----------

INSERT OVERWRITE Dim_Airlines
SELECT 
iata_code 
,icao_code 
,name 
FROM  cleansed_dev.airline
