# Hatchways test by Jordan ADOPO
Built api with Flask

## Table of Contents

- [Checklist](#about)
- [Test](#test)
- [Launch](#launch_api)

## Checklist <a name = "about"></a>

<br/>Before submitting your assessment, make sure you have:
<br/>&nbsp;&nbsp;    ❏ An /api/posts route that handles the following query parameters:
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ❏ tags (mandatory) : any number of comma-separated strings
<br/> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;      ❏ sortBy (optional) : one of “id”, “reads”, “likes”, “popularity”
<br/> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;      ❏ direction (optional) : one of “asc”, “desc”, defaults to “asc”
<br/>&nbsp; &nbsp;   ❏ Error handling: Return an error message if:
<br/> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;      ❏ tags parameter is missing
<br/> &nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;     ❏ sortBy or direction has an invalid value
<br/>&nbsp; &nbsp;   ❏ Testing without using our solution API route
<br/>&nbsp; &nbsp;   ❏ Caching (bonus)

## Running Test <a name = "test"></a>
```
./startup.sh test 
```
<b>or</b> 
```
bash startup.sh test
```



### Installing requiements

Just need one instruction

```
pip install -r requirements.txt
```
<b>or</b> if pip not added to path system
```
python -m pip install -r requirements.txt
```

## Start API <a name = "launch_api"></a>

```
flask run 
```
or
```
python -m flask run 
```
or
```
./startup.sh start 
```
<b>or</b> 
```
bash startup.sh test
```

### An example in browser with url:
http://127.0.0.1:5000/api/posts?tags=tech,history,startups&sortBy=reads
