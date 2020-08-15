# miniservidor-aws
Attemplate for small python aws server

IT IS IMPORTANT  TO  KNOW THAT fastapi OR uvicorn DEPENDS ON python>=3.7

It is better to create the file .gitignore on this page gitignore.io

In the file requirements there are three important libraries:
- fastapi: for creating api end-points for receiving http request.
- uvicorn: to setup a running server.
- boto3: exclusive for aws.

For installing the libraries run the following command on the terminal 
```shell script
pip install -r requirements.txt
```

For initializing the fastapi's app run the following command on the terminal
```shell script
uvicorn main:app --host 0.0.0.0
```

To send parameters in get request, modify the url on the browser
```shell script
http://0.0.0.0:8000?a=2&b=3
``` 
