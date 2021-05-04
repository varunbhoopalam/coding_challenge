import logging

import flask
from flask import Response, jsonify
from app.service import get_profile_statistics
from app.exceptions import ProfileNotFoundError, ServiceNotAvailable

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
        return jsonify({
            "status": "success",
            "data": get_profile_statistics(githubProfile, bitbucketProfile),
            "message": "success"})
    except ProfileNotFoundError as e:
        return jsonify({
            "status": "failure",
            "data": e.data,
            "message": "At least one profile was not found"})
    except ServiceNotAvailable as e:
        return jsonify({
            "status": "failure",
            "data": e.data,
            "message": "At least one service unavailable"})