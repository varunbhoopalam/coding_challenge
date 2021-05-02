# Git Profile API

This API serves organization profile metadata from aggregating information from both Github and Bitbucket. 

## Routes

One route will be exposed to serve metadata

GET - /github-profile/{githubProfile}/bitbucket-profile/{bitbucketProfile}/statistics

The githubProfile and bitbucketProfile are passed as path variables. If either profile cannot be found in github or bitbucket, we will return a Bad Request 404 resource not found and detail which resource(s) could not be found.

**Request**

```
curl -i "http://127.0.0.1:5000/github-profile/mailchimp/bitbucket-profile/mailchip/statistics"
```

**Response**

```
 { "status": "failure",
   "data": {
     "code": 404,
     "github_profile": {
       "name": "mailchimp",
       "found": false
     },
     "bitbucket_profile": {
       "name": "mailchimp",
       "found": false
     }
   },
   "message": "At least one profile was not found" /* This field is nullable */
 }
```

This is an example of a successful request where both profiles were successfully found in github and bitbucket respectively.

**Request**

```
curl -i "http://127.0.0.1:5000/github-profile/mailchimp/bitbucket-profile/mailchip/statistics"
```

**Response**

```
 { "status": "success",
   "data": {
     "public_repo_count": 20,
     "public_repo_breakdown": /* This field is nullable */
     { "original_repo_count": 10,
       "forked_repo_count": 10
     },
     "watcher_count": 15,
     "langauge_count": 8,
     "topics_count": 4
   },
   "message": null /* This field is nullable */
 }
```

## Install:

You can use a virtual environment (conda, venv, etc):
```
conda env create -f environment.yml
source activate user-profiles
```

Or just pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running the code

### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests

```
curl -i "http://127.0.0.1:5000/health-check"
```


## What'd I'd like to improve on...
* Add openAPI spec or swagger page
