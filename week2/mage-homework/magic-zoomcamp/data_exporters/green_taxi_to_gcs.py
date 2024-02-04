import os
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/dtc-de-course-400420-dc35f3372a39.json"

bucket_name = "mage_green_taxi_dezoomcamp"
projec_id = "dtc-de-course-400420"

table_name = "nyc_green_taxi"

root_path = f'gs://{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=["lpep_pickup_date"],
        filesystem=gcs
    )