## Kraepelin Test Page

### Simple kraepelin page

### requirements:
- python 3 & virtualenv `https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b`

### Progress
- [x] User interface
- [x] generate kraepelin test by visiting `host/test` by default will be `5x5` size, but can be modified by passing `?size=6x6`
- [ ] API to handle user answer
- [ ] database configurations
 
### Development
- Clone the repository
- create virtualenv `virtualenv -p python3 env`
- activate virtual environment `cd kraepelin` & `. env/bin/activate`
- install dependencies `pip install -r requirements.txt`
- run in dev mode `python wsgi.py`, it should be running on `localhost:5000`
