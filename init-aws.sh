#!/bin/bash
awslocal dynamodb create-table \
   --table-name products \
   --attribute-definitions \
      AttributeName=sku,AttributeType=S \
      AttributeName=brand,AttributeType=S \
   --key-schema \
      AttributeName=sku,KeyType=HASH \
      AttributeName=brand,KeyType=RANGE \
   --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
   --region us-east-1