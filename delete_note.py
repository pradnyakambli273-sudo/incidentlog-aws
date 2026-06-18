import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def handler(event, context):
    note_id = event['pathParameters']['noteId']
    table.delete_item(Key={'noteId': note_id})
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'deleted': note_id})
    }