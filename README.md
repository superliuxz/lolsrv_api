# lolsrv_api

API specifications: https://github.com/lolcommits/lolcommits-lolsrv

Tested under Python 3.6.6 and Postgres 10.

---
First, set up the database. The default backend is Postgres:
```
createdb -U postgres lolsrv_api
createuser -U postgres lolsrv_api
psql -c "GRANT CONNECT ON DATABASE lolsrv_api TO lolsrv_api;" -U postgres
psql -c "ALTER USER lolsrv_api PASSWORD '<YOUR PASSWORD>'" -U postgres

```

Then, create `settings_<YOUR NAME>.py` file under `settings` directory.

Use the template:
```python
from .settings import *

DATABASES['default']['NAME'] = 'lolsrv_api'
DATABASES['default']['USER'] = 'lolsrv_api'
DATABASES['default']['PASSWORD'] = <YOUR PASSWORD>
DATABASES['default']['HOST'] = 'localhost'

IMG_FILE_PATH = "/tmp"

IMG_SINK_PATH = "lolsrv_api.image_sink.DatabaseSink"
``` 

---
For `autoenv`, the `.env` file:
```
export DJANGO_SETTINGS_MODULE=lolsrv_api.settings.settings_<YOUR NAME>
workon lolsrv_api
```

---
**TODOs**

- [ ] deployable to Google Cloud
- [ ] save images to persistent file system instead of database
