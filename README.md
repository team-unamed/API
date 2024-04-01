# Unamed Blockchain AI API

This API provides a simple interface to interact with AI models focused on blockchain technology. It has two endpoints: `/` and `/ask`.

## Endpoints

### `/` (GET)

This endpoint is used to check the status of the API. It returns a simple string `"Welcome to the Unamed Blockchain AI"`.

### `/ask` (POST)

This endpoint is used to ask a question to the AI model. It accepts the following query parameters:

- `question` (required): The question you want to ask the AI model.
- `model` (required): The name of the AI model you want to use. Supported models are `solidity`, `ethereum`, and `bitcoin`.
- `api_key` (optional): Your API key to authenticate with the service.

#### Request Example

```
POST /ask?question=What%20is%20the%20difference%20between%20a%20smart%20contract%20and%20a%20regular%20contract&model=solidity&api_key=your_api_key
```

#### Responses

- **200 OK**: The AI model's response to the question.
- **404 Not Found**: If the specified `model` does not exist (i.e., not one of `solidity`, `ethereum`, or `bitcoin`), the API will return `"This model does not exist"` with a 404 status code.

