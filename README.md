# AWS S3 cleanup routine

### This code can handle S3 objects, by events using a SQS or AWS API.
> the payload events must contains :

| key | description |
| --- | --- |
| bucket | the bucket name from S3 |
| path | the path to access the object |
| object | the object name |

### <i>Testing locally...</i>
> use the `python3` to create a virtual enviromnent:
```
python3 -m venv lambda_env
```

> access the virtual environment created:
```
. lambda_env/bin/activate
```

> into the `venv`, install the requeriments:
```
pip3 install -r requeriments.txt
```

> now you can call the `test.sh` bash to simulate the behavior of a python lambda:
```
./test.sh main lambda_function.py event.json
```

*or*
```
python-lambda-local -f main lambda_function.py event.json
```

### Note
> you can change the event values in the `event.json` file, then note that both scenarios are valid:
```Json
{
  "bucket":"datalake_raw",
  "path":"index00101/2020-02-08/",
  "object":"obj0001_test_file.csv"
}
```
*or*
```Json
[
  {
    "bucket":"datalake_raw",
    "path":"index00101/2020-02-08/",
    "object":"obj0001_test_file.csv"
  },
  {
    "bucket":"datalake_raw",
    "path":"index00110/2020-02-09/",
    "object":"obj0100_test_file.csv"
  }
]
```
