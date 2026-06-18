import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')

def handler(event, context):
    note_id = event['pathParameters']['noteId']
    body = json.loads(event['body'])

    update_expr = "SET #s = :s"
    expr_names = {"#s": "status"}
    expr_values = {":s": body.get('status', 'Open')}

    if 'content' in body:
        update_expr += ", content = :c"
        expr_values[":c"] = body['content']

    if 'severity' in body:
        update_expr += ", severity = :sev"
        expr_values[":sev"] = body['severity']

    table.update_item(
        Key={'noteId': note_id},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_names,
        ExpressionAttributeValues=expr_values
    )
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'updated': note_id})
    }