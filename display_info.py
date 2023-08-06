from flask import Flask, request, jsonify


def display_info(product_info):

    beautified = "<h2> Title: " + product_info["title"] + "</h2> <br> <h2> Brand: " + product_info["brand"] + "</h2> <br> <h2> Review Score: " + product_info["review_score"] 

    return beautified
 