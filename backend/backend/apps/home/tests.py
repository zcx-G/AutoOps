from django.test import TestCase

# Create your tests here.
import base64,json
data = {
  'typ': 'JWT',
  'alg': 'HS256',
  'kid': '018c0ae2-87d3-491a-97a0-c9e868c6f13e'
}




header = base64.b64encode(json.dumps(data).encode()).decode()
print(header)