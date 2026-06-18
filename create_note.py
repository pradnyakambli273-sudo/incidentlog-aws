import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def handler(event, context):
    body = json.loads(event['body'])
    
    if 'content' not in body or 'severity' not in body:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'content and severity are required'})
        }
    
    if body['severity'] not in ['Critical', 'Warning', 'Info']:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'severity must be Critical, Warning or Info'})
        }

    incident = {
        'noteId': str(uuid.uuid4()),
        'content': body['content'],
        'severity': body['severity'],
        'status': 'Open',
        'createdAt': datetime.utcnow().isoformat()
    }
    table.put_item(Item=incident)
    return {
        'statusCode': 201,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(incident)
    }