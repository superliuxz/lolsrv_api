# lolsrv_api
[![CircleCI](https://circleci.com/gh/superliuxz/lolsrv_api/tree/master.svg?style=svg)](https://circleci.com/gh/superliuxz/lolsrv_api/tree/master)

---
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
Run with docker:
- Make sure the docker container has access to the database
- Make sure `DJANGO_SETTINGS_MODULE`, `DATABASE_NAME`, `DATABASE_USER`,
`DATABASE_PASSWORD` and `DATABASE_HOST` are set.

---
**TODOs**

- [x] dockerize the runtime
- [ ] deployable to Google Cloud
- [ ] save images to persistent file system instead of database
- [ ] better database credential management