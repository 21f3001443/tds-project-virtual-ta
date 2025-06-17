## CORS: Cross-Origin Resource Sharing

CORS (Cross-Origin Resource Sharing) is a security mechanism that controls how web browsers handle requests between different origins (domains, protocols, or ports). Data scientists need CORS for APIs serving data or analysis to a browser on a different domain.

Watch this practical explanation of CORS (3 min):

[![CORS in 100 Seconds](https://i.ytimg.com/vi_webp/4KHiSt0oLJ0/sddefault.webp)](https://youtu.be/4KHiSt0oLJ0
<youtube_summary>Cross-Origin Resource Sharing (CORS) is a mechanism that allows a website on one URL to request data from a different URL. It often frustrates developers because browsers enforce the same-origin policy, which permits requests only within the same origin for security reasons. When a browser makes a request, it includes an Origin header. If the request is to the same origin, it proceeds without issue. For cross-origin requests, the server must respond with an Access-Control-Allow-Origin header that matches the request's origin or use a wildcard (*) to allow any origin. If this header is missing or mismatched, the browser blocks the response, causing a CORS error with limited error details.

The solution to CORS issues lies on the server side. If you control the server, you can configure it to send the appropriate CORS headers. For example, in Express.js, this can be done with a simple middleware line that adds CORS headers to every response. Some HTTP requests, like PUT or those with non-standard headers, require a preflight OPTIONS request—a preliminary check by the browser to ensure the server allows the intended request methods and headers. The server replies with allowed origins, methods, and headers, and the browser can cache this approval using the max-age header to reduce repeated preflights.

To troubleshoot CORS errors, check the browser’s network tab for the Access-Control-Allow-Origin header in the response. If absent, enable CORS on the server. If present but mismatched, adjust the server configuration to allow the correct origin or methods. Proper server configuration ensures cross-origin requests succeed without security risks.</youtube_summary>
)

Key CORS concepts:

- **Same-Origin Policy**: Browsers block requests between different origins by default
- **CORS Headers**: Server responses must include specific headers to allow cross-origin requests
- **Preflight Requests**: Browsers send OPTIONS requests to check if the actual request is allowed
- **Credentials**: Special handling required for requests with cookies or authentication

If you're exposing your API with a GET request publicly, the only thing you need to do is set the HTTP header `Access-Control-Allow-Origin: *`.

Here are other common CORS headers:

```http
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
```

To implement CORS in FastAPI, use the [`CORSMiddleware` middleware](https://fastapi.tiangolo.com/tutorial/cors/):

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins
# Or, provide more granular control:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Allow a specific domain
    allow_credentials=True,  # Allow cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow specific methods
    allow_headers=["*"],  # Allow all headers
)
```

Testing CORS with JavaScript:

```javascript
// Simple request
const response = await fetch("https://api.example.com/data", {
  method: "GET",
  headers: { "Content-Type": "application/json" },
});

// Request with credentials
const response = await fetch("https://api.example.com/data", {
  credentials: "include",
  headers: { "Content-Type": "application/json" },
});
```

Useful CORS debugging tools:

- [CORS Checker](https://cors-test.codehappy.dev/): Test CORS configurations
- Browser DevTools Network tab: Inspect CORS headers and preflight requests
- [cors-anywhere](https://github.com/Rob--W/cors-anywhere): CORS proxy for development

Common CORS errors and solutions:

- `No 'Access-Control-Allow-Origin' header`: Configure server to send proper CORS headers
- `Request header field not allowed`: Add required headers to `Access-Control-Allow-Headers`
- `Credentials flag`: Set both `credentials: 'include'` and `Access-Control-Allow-Credentials: true`
- `Wild card error`: Cannot use `*` with credentials; specify exact origins
