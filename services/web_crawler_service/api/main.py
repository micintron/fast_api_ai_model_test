""" API to grab content targets from a website.

    Endpoints
    ---------

    * GET /: health check. If API is running, will successfully return a message
    * GET /scrape_site: expects a "url" parameter with a website to scrape. Returns text of website.
    * GET /docs: Swagger docs for this API


    USAGE
    -----

    Run local: 
    > uvicorn main:app --reload

    Docker build:
    > docker build -t fastapi-demo .

    Docker run: 
    > docker run -p 8000:80 fastapi-demo

    You should then be able to navigate to localhost:8000/docs to see auto-generated Swagger
"""
import logging
import time
from typing import List, Dict
from datetime import datetime, timedelta, date
from fastapi import FastAPI, APIRouter, Request, Depends, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ai_test.ai_model_example import ai_test

#cache imports
from aiocache import Cache
from aiocache.serializers import PickleSerializer
cache = Cache(Cache.MEMORY, serializer=PickleSerializer())


logging.basicConfig(level=logging.INFO)
logging.info(" Application Web Crawler (AWC) -Started-  :"+ str(datetime.now()))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Welcome to the FastAPI ML API Production Demo"


@app.post("/ai-text")
def ai_text(request: Request, data_points:list):
    """Get score from model with data sent out
    
    Example----
    [-0.89483109,-1.0670149,-0.25448694]
    """
    logging.info("(AWC) endpoint AI test_text -Hit-  :"+ str(datetime.now()))

    try:
        start_time = time.time()
        results = ai_test(data_points)

        # write to cache and return
        logging.info('(AWC) endpoint AI test -END-  : run time = '+str(time.time() - start_time))
        return results

    except Exception as e:
        logging.error("(AWC) endpoint AI test -Error-  :"+ str(e))
        return None






if __name__ == "__main__":
    import json
    import os
    import subprocess

    target_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "sphinxdocs", "source", "_static", "webcrawler.json")
    with open(target_path, 'w') as f:
        json.dump(app.openapi(), f)

    subprocess.run("npx redoc-cli bundle webcrawler.json -o webcrawler.html", cwd=os.path.join(os.path.dirname(target_path)), shell=True, check=True)
    print(scrape_site.__doc__)
