# Python stable diffusion GPU

Generate text to image using a stable diffusion model on your <b>local machine</b>.

## Quickstart
* go to api folder `cd api`
* install api dependencies `pip install -r requirements.txt`
* you can check if you have cuda gpu using `python cuda-check.py`
* start api server `uvicorn diffusion-api:app --reload`
* go to frontend folder `cd ../frontend`
* install frontend dependencies `npm install`
* start frontend `npx vite`
* navigate to url vite gives you and start generating images