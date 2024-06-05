from pyrogram import filters
import os

class Config:
    API_ID = "20165423"
    API_HASH = "1371ff44f8818128c9b821b28d8e8d9c"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://yash:shivanshudeo@yk.6bvcjqp.mongodb.net/?retryWrites=true&w=majority&appName=yk"
    START_PIC = "https://graph.org/file/efb4c74b3eeee31be7bdc.jpg"
    SUDOERS = filters.user(["6399386263"])
