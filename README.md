# Gadget Sales Real-Time Data Projection and CDC Pipeline on AWS

Real-time AWS CDC pipeline that captures INSERT, MODIFY, and REMOVE operations from DynamoDB, streams events through EventBridge Pipes and Kinesis, transforms and projects required attributes using AWS Lambda, and delivers JSON data to Amazon S3 for SQL-based analytics using AWS Glue and Amazon Athena.

## Architecture


```text
DynamoDB
    |
    v
DynamoDB Streams
    |
    v
Amazon EventBridge Pipes
    |
    v
Amazon Kinesis Data Streams
    |
    v
Amazon Data Firehose
    |
    v
AWS Lambda Transformation
    |
    v
Amazon S3
    |
    v
AWS Glue Data Catalog
    |
    v
Amazon Athena
```
## Key Features

- Real-time CDC event processing
- Supports INSERT, MODIFY, and REMOVE operations
- Lambda-based data projection and transformation
- Streaming data ingestion using Amazon Kinesis
- Automated delivery of transformed events to Amazon S3
- Data cataloging with AWS Glue
- SQL-based analytics using Amazon Athena


## AWS Services

| Service | Purpose |
|---|---|
| Amazon DynamoDB | Source database |
| DynamoDB Streams | Captures record changes |
| Amazon EventBridge Pipes | Routes CDC events |
| Amazon Kinesis Data Streams | Streams event data |
| Amazon Data Firehose | Buffers and delivers events |
| AWS Lambda | Transforms and projects fields |
| Amazon S3 | Stores projected CDC events |
| AWS Glue | Catalogs the data |
| Amazon Athena | Queries the data |

## Repository Structure


```text
gadget-sales-cdc-pipeline/
├── lambda/
│   └── producer.py
│   └── transform-for-firehose.py
├── Architecture.jpg
└── README.md
```
## Data Flow

1. Gadget sales records are inserted, modified, or deleted in DynamoDB.
2. DynamoDB Streams captures the changes.
3. EventBridge Pipes forwards events to Kinesis Data Streams.
4. Amazon Data Firehose consumes the streaming events.
5. Lambda transforms the records and extracts the required attributes.
6. Firehose delivers the projected CDC events to Amazon S3.
7. AWS Glue catalogs the data for querying through Athena.

## Lambda Transformation

The Lambda function processes Firehose transformation requests and:

- Extracts the required fields from incoming CDC events.
- Preserves the CDC operation type.
- Formats projected records as JSON.
- Returns records using the Firehose transformation response format.
- Handles malformed records according to the configured error-handling logic.

## Demo Video

Watch the project demonstration:

[https://youtu.be/G5nb7lvztOw?si=4432QFUKKQ7HHFgV]

## Data Storage Design

Amazon S3 stores projected CDC change events, including their operation types. It is not automatically a materialized current-state table.

A separate downstream processing step is required to apply inserts, updates, and deletes to construct the latest state of the dataset.


## Author

Varinder Kumar

Data Engineering | Python | SQL
