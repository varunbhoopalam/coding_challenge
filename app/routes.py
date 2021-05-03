import logging

import flask
from flask import Response, jsonify
from service import get_profile_statistics
from exceptions import ProfileNotFoundError

app = flask.Flask("user_profiles_api")
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)


@app.route("/github-profile/<githubProfile>/bitbucket-profile/<bitbucketProfile>/statistics", methods=["GET"])
def aggregate_profile_statistics(githubProfile, bitbucketProfile):
    """
    Endpoint to serve organization profile metadata from aggregating information from both Github and Bitbucket
    """
    try:
        return Response({
            "status": "success",
            "data": get_profile_statistics(githubProfile, bitbucketProfile),
            "message": "success"},
            status=200)
    except ProfileNotFoundError as e:
        return Response({
            "status": "failure",
            "data": e.data,
            "message": "At least one profile was not found"},
            status=404)
