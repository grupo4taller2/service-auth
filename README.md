# service-tipitos

![Lint](https://github.com/grupo4taller2/service-tipitos/actions/workflows/lint.yml/badge.svg)

![Test](https://github.com/grupo4taller2/service-tipitos/actions/workflows/test.yml/badge.svg)

[![Heroku Deploy](https://github.com/grupo4taller2/service-tipitos/actions/workflows/deploy.yml/badge.svg)](https://g4-fiuber-service-tipitos.herokuapp.com/docs)

[![Codecov Test coverage](https://codecov.io/gh/grupo4taller2/service-tipitos/branch/main/graph/badge.svg?token=C3GAHNA3D0)](https://codecov.io/gh/grupo4taller2/service-tipitos)

---

> In order to trigger the alembic migrations, you run the `alembic upgrade head` command.
When you make any change to a database table, you capture that change by running `alembic
revision --autogenerate -m "Some description"` - this will generate a new file in the 
versions directory which you should always check.


> alembic -c ./alembic/alembic.ini revision --autogenerate -m "First table"