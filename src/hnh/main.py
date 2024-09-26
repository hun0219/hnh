from fastapi import FastAPI
import os
import random

app = FastAPI()


def predict():
    dog_list = ["hotdog","not hotdog"]

    return dog_list[random.randint(0,1)]


@app.get("/")
def read_root():
    dog = predict()
    return dog
