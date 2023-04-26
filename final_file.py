import pandas as pd
from io import BytesIO

from google.cloud import storage
from google.cloud import bigquery



# This is the trigger function and netry point for our project pipeline, It triggers/occurs when the object is created, or an existing object is overwritten in our bucket.

def hello_gcs(event, context):
    
    lst=[]
    file_name = event['name']
    bucket = event['bucket']
    
    # Creating a client object
    client = bigquery.Client()
    storage_client = storage.Client()
    
    # Set the ID of the new dataset you want to create
    file1= str(file_name).split(".")
    dataset_id =file1[0]
    # Check if the dataset exists
    dsexists = False
    for dataset in client.list_datasets():
        if dataset.dataset_id == dataset_id:
            dsexists = True
            break

    # If the dataset does not exist, create a new dataset
    if not dsexists:
        dataset = bigquery.Dataset(client.dataset(dataset_id))
        dataset.location = 'US'
        dataset = client.create_dataset(dataset)
        print('Created dataset {}.'.format(dataset.dataset_id))
    else:
        print('Dataset {} already exists.'.format(dataset_id))
    
    #bucket = storage_client.get_bucket('finaldatabucket')
    #obtaining the path of the file
    path = 'gs://'+str(bucket)+'/'+str(file_name)
    #reading csv file as dataframe
    df = pd.read_csv(path)
    #Dropping the unwanted columns
    df = df.drop(df.columns[0], axis=1)
    df=df.dropna()
    #filling the null fields with 0. 
    df=df.fillna(0)
    #checking for unique industries in the dataframe
    unique_industries= df.industry.unique()
    unique_length=len(unique_industries)
    #print(unique_industries[0])
    table_schema = []
    #retrieving the schema of the table to create a table
    for column in df.columns:
        if df[column].dtype == "object":
            column_type = "STRING"
        elif df[column].dtype == "int64":
            column_type = "INTEGER"
        elif df[column].dtype == "float64":
            column_type = "FLOAT"
        elif df[column].dtype == "bool":
            column_type = "BOOLEAN"
        else:
            column_type = "STRING"  # Default to string type
        table_schema.append(bigquery.SchemaField(column, column_type, mode="NULLABLE"))
    #print(df)

    for x in range(unique_length):
        #new_df=pd.DataFrame()
        new_df = df[df['industry'] == unique_industries[x]]
        # Create the BigQuery table
        table_name=unique_industries[x].split("/")[0]
        table_name=table_name.split(" ")[0]
        table_id = str(dataset_id)+"."+str(table_name)
        #creating Bigquery table using the schema.
        job_config = bigquery.LoadJobConfig(schema=table_schema)
        #dumping the filtered data into the big query table
        job = client.load_table_from_dataframe(new_df, table_id, job_config=job_config)
        job.result()

        # Check if the table was created successfully
        table = client.get_table(table_id)
        print(f"Table {table.table_id} was created with {len(table.schema)} columns.")
        
