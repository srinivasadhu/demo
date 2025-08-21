
---

### 8. `tests/test_basic.py` (optional but good for checkride)
```python
import lambda_handler

def test_lambda_handler():
    response = lambda_handler.lambda_handler({}, {})
    assert response['statusCode'] == 200
    assert "Hello from Lambda" in response['body']
