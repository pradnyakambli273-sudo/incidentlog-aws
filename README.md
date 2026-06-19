# IncidentLog 🔴
> A serverless cloud incident tracking system built on AWS

Log, classify, and resolve infrastructure incidents by severity in real time — built entirely with AWS serverless services and deployed via AWS CLI.

🌐 **Live Demo:** http://notes-app-pradnya-2026.s3-website.ap-south-1.amazonaws.com

---

## Screenshot
![IncidentLog Dashboard](screenshot.png)

---

## Features
- 🔴 **Severity Classification** — Critical, Warning, Info
- ✅ **Incident Lifecycle** — Open → Resolved status tracking
- ✏️ **Full CRUD** — Create, edit, and delete incidents
- 🔍 **Filter** by severity or status
- 📊 **Live stats** — real-time incident counts by severity
- ☁️ **100% Serverless** — zero servers, zero maintenance cost

---

## Architecture

| Component | AWS Service |
|---|---|
| Frontend Hosting | S3 Static Website |
| REST API | API Gateway (HTTP API) |
| Business Logic | Lambda (Python 3.12) |
| Database | DynamoDB |
| Access Control | IAM Roles and Policies |

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/notes` | Fetch all incidents |
| POST | `/notes` | Log a new incident |
| PUT | `/notes/{noteId}` | Update incident content or status |
| DELETE | `/notes/{noteId}` | Delete an incident |

---

## Project Structure

    incidentlog-aws/
    ├── create_note.py       # POST - log new incident
    ├── get_notes.py         # GET - fetch all incidents
    ├── update_note.py       # PUT - edit or resolve incident
    ├── delete_note.py       # DELETE - remove incident
    ├── index.html           # Frontend hosted on S3
    └── README.md

---

## Setup and Deployment

### Prerequisites
- AWS account with free tier
- AWS CLI v2 configured
- Python 3.12

### 1. Create DynamoDB table
```bash
aws dynamodb create-table \
  --table-name Notes \
  --attribute-definitions AttributeName=noteId,AttributeType=S \
  --key-schema AttributeName=noteId,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

### 2. Create IAM role for Lambda
```bash
aws iam create-role \
  --role-name lambda-notes-role \
  --assume-role-policy-document file://trust-policy.json

aws iam attach-role-policy \
  --role-name lambda-notes-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
```

### 3. Deploy Lambda functions
```bash
Compress-Archive -Path create_note.py -DestinationPath create_note.zip
aws lambda create-function \
  --function-name create-note \
  --runtime python3.12 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/lambda-notes-role \
  --handler create_note.handler \
  --zip-file fileb://create_note.zip
```

### 4. Deploy frontend to S3
```bash
aws s3 cp index.html s3://YOUR_BUCKET_NAME/ --acl public-read
```

---

## Roadmap
- [ ] User authentication via AWS Cognito
- [ ] Assign incidents to team members
- [ ] Comment threads per incident
- [ ] Email and SMS alerts via AWS SNS for Critical incidents
- [ ] Analytics dashboard — MTTR and incident frequency by service

---

## Tech Stack
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-blue)
![API Gateway](https://img.shields.io/badge/AWS-APIGateway-yellow)
![S3](https://img.shields.io/badge/AWS-S3-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)

---
