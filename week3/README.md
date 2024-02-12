## 📝 Module 3 Data Warehouse Homework

* **Question 1:**

```
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-400420.ny_green_taxi.external_green_2022_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage_green_taxi_dezoomcamp/green_taxi_2022_parquet/green_tripdata_2022-*.parquet']
);
```

```
SELECT COUNT(*) 
FROM ny_green_taxi.external_green_2022_tripdata;
```

> Answer: 840402

* **Question 2**:

```
-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE ny_green_taxi.green_2022_tripdata_nonpartitioned AS
SELECT * FROM ny_green_taxi.external_green_2022_tripdata;
```

```
-- This query will process 0 B when run.
SELECT COUNT(DISTINCT(PULocationID)) 
FROM ny_green_taxi.external_green_2022_tripdata;

-- This query will process 6.41 MB when run.
SELECT COUNT(DISTINCT(PULocationID)) 
FROM ny_green_taxi.green_2022_tripdata_nonpartitioned;
```

> Answer: 0 MB for the External Table and 6.41MB for the Materialized Table

* **Question 3**:

```
SELECT COUNT(*) 
FROM ny_green_taxi.external_green_2022_tripdata
WHERE fare_amount = 0;
```

> Answer: 1622

* **Question 4**:

```
-- Creating a partition and cluster table
CREATE OR REPLACE TABLE ny_green_taxi.green_2022_tripdata_partitoned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
SELECT * FROM ny_green_taxi.external_green_2022_tripdata;
```

> Answer: Partition by lpep_pickup_datetime Cluster on PUlocationID

* **Question 5**:

```
-- This query will process 12.82 MB when run.
SELECT DISTINCT(PULocationID) 
FROM ny_green_taxi.green_2022_tripdata_nonpartitioned
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- This query will process 1.12 MB when run.
SELECT DISTINCT(PULocationID) 
FROM ny_green_taxi.green_2022_tripdata_partitoned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';
```

> Answer: 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table

* **Question 6**:

> Answer: GCP Bucket

* **Question 7**:

> Answer: False

* **Question 8**:

```
-- This query will process 0 B when run.
SELECT COUNT(*)
FROM ny_green_taxi.green_2022_tripdata_nonpartitioned;
```

> Answer: This query will process 0B, because the COUNT(*) returns the number of rows of the table, which is already known and stored in the Storage Info of the table (metadata) after its creation.