# poc-revoke

### Dependency: 

`pip install request`

### Config: 

Edit config.ini file

### Start:

`python3 ./main.py`

### Sample response: 

```json
Token: eyJraWQiOiJkZWZhdWx0IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJiYWNrIiwiYXVkIjoiYmFjayIsImRvbWFpbiI6IjIxZDlmY2FiLWQ4Y2ItNDU0My05OWZjLWFiZDhjYjk1NDMxNiIsImlzcyI6Imh0dHA6XC9cL2xvY2FsaG9zdFwvYW1cL2FwaW1cL29pZGMiLCJleHAiOjE2MzMzNDkwNDcsImlhdCI6MTYzMzM0MTg0NywianRpIjoiSUhQRUI0UVBUQkR2MkdqVkdac1ZNQXI5ZF9CU1hCX0EzQ3o3eHBPTHFlTSJ9.pHMmFS4V9xOgoUu_ti_Mx4cCg4RDHWRPrjeO7ZV9jIAeGPeYuf2Qymru696AlVVAM7nc4z3nfRGtIuYBkBMnWbkV0WHf9Z8u-vsc24AYhOsaITucHukTCtA1yhHfJrE8tN8ALGZnyMLlqUES_NeyNTBupZxARhX4goUhFlj184zSYWSs-_A-wP_WKHeV5znIE0_yNzUDBkWZmK2DxDmu5FBRPFfbmLzsZjiL8GtNbmyj2Wgu4SQ0vpr1bdg66TGjIXnVVLjMGip0KPcyNLZ0Rlm-Imj90qfvtM7fMiZCYrpfvg4u3Vw7EfQzJxbqnv2oAqVdPA3YziYwh3C_oJ2WKA
Introspection is active token: True
{
  "sub" : "back",
  "domain" : "21d9fcab-d8cb-4543-99fc-abd8cb954316",
  "iss" : "http://localhost/am/apim/oidc",
  "active" : true,
  "exp" : 1633349047,
  "token_type" : "bearer",
  "iat" : 1633341847,
  "client_id" : "back",
  "jti" : "IHPEB4QPTBDv2GjVGZsVMAr9d_BSXB_A3Cz7xpOLqeM"
}
Revoke : 
HTTTP 200

Introspection is active token: True
{
  "sub" : "back",
  "domain" : "21d9fcab-d8cb-4543-99fc-abd8cb954316",
  "iss" : "http://localhost/am/apim/oidc",
  "active" : true,
  "exp" : 1633349047,
  "token_type" : "bearer",
  "iat" : 1633341847,
  "client_id" : "back",
  "jti" : "IHPEB4QPTBDv2GjVGZsVMAr9d_BSXB_A3Cz7xpOLqeM"
}
```
