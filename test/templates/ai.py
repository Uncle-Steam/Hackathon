import boto3
import json

brt = boto3.client(service_name='bedrock-runtime')

def assistant(prompt):
  body = json.dumps({
      'prompt': '\n\nHuman:' + prompt + '\n\nAssistant:',
      'max_tokens_to_sample': 100
  })
                    
  response = brt.invoke_model_with_response_stream(
      modelId='anthropic.claude-v2', 
      body=body
  )

  completion_output = ""

  stream = response.get('body')
  if stream:
      for event in stream:
          chunk = event.get('chunk')
          if chunk:
              chunk = (json.loads(chunk.get('bytes').decode()))
              completion_output += chunk.get('completion', '')


  return completion_output
