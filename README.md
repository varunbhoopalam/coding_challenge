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
       "found": true
     },
     "bitbucket_profile": {
       "name": "mailchip",
       "found": false
     }
   },
   "message": "At least one profile was not found" /* This field is nullable */
 }
```

This is an example of a successful request where both profiles were successfully found in github and bitbucket respectively.

**Request**

```
curl -i "http://127.0.0.1:5000/github-profile/mailchimp/bitbucket-profile/mailchimp/statistics"
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
     "languages": [
       { "name": "python"
       , "count": 3
       },
       { "name": "ruby"
       , "count": 4
       }
     ],
     "topics": [
       { "name": "flask"
       , "count: 3
       }
     ]
   },
   "message": null /* This field is nullable */
 }
```

## External Dependencies

* Github API v3 - https://api.github.com
  * Specific route - https://api.github.com/orgs/{org}/repos  
  * Learn more [here](https://docs.github.com/en/developers/overview/about-githubs-apis)
* Bitbucket API 2.0 - https://api.bitbucket.org
  * Specific route - https://api.bitbucket.org/2.0/repositories/{org}
  * Learn more [here](https://developer.atlassian.com/bitbucket/api/2/reference/meta/pagination)

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

### Run Tests

```
python app/{test_file.py}
```

## What'd I'd like to improve on...
* Add openAPI spec or swagger page
* Finish tests to document behavior
* Gather more information as to how this api would be used. With more information, we'd potentially know things like expected load, how often request parameters come up, etc and make better decisions as a result. Could accomplish this by
  * Talking to key stakeholders
  * Implementing persisted logging with analytics, something like prometheus+grafana
* Improve Speed, 
  * Potentially a lot of waiting around on external apis, introduce async to work on tasks concurrently
  * Caching, especially if the same requests are made over and over
* Authentication to not be rate limited
