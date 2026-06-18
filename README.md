# IncidentLog 🔴
> A serverless cloud incident tracking system built on AWS

Log, classify, and resolve infrastructure incidents by severity in real time — built entirely with AWS serverless services and deployed via AWS CLI.

🌐 **Live Demo:** http://notes-app-pradnya-2026.s3-website.ap-south-1.amazonaws.com

---

## Screenshots
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
| Access Control | IAM Roles & Policies |

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

---

## Setup & Deployment

### Prerequisites
- AWS CLI v2 configured
- Python 3.12
- GitHub account

### Deploy Lambda Functions
```bash
Compress-Archive -Path create_note.py -DestinationPath create_note.zip
aws lambda create-function --function-name create-note \
  --runtime python3.12 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/lambda-notes-role \
  --handler create_note.handler \
  --zip-file fileb://create_note.zip
```

### Deploy Frontend
```bash
aws s3 cp index.html s3://YOUR_BUCKET_NAME/ --acl public-read
```

---

## Roadmap
- [ ] User authentication via AWS Cognito
- [ ] Assign incidents to team members
- [ ] Comment threads per incident
- [ ] Email/SMS alerts via AWS SNS for Critical incidents
- [ ] Analytics dashboard — MTTR, incident frequency by service

---

## Tech Stack
![AWS](https://img.shields.io/badge/AWS-Lambda-orange)
![AWS](https://img.shields.io/badge/AWS-DynamoDB-blue)
![AWS](https://img.shields.io/badge/AWS-APIGateway-yellow)
![AWS](https://img.shields.io/badge/AWS-S3-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)

---

## Author
Pradnya — Third Year B.Tech, Electronics & Telecommunication  
Vidyalankar Institute of Technology, Mumbai