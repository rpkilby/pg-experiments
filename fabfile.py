
from __future__ import absolute_import

from fabric.api import task, cd, sudo
from fabtools.require.postgres import LocalRule
from fabtools import require
from fabtools import postgres
from fabtools import python

from fabtools.vagrant import vagrant


DB_USER = 'vagrant'
DB_NAME = 'pg-experiments'
PROJECT_NAME = 'pg-experiments'


@task
def provision(name='default'):
    # initialize postgres
    require.postgres.server(9.5, postgis=True)

    pg_service = postgres.service_name(9.5)
    require.service.started(pg_service)
    require.service.enabled(pg_service)
    # require.postgres.listening_on('*')

    require.postgres.hba_conf([
        LocalRule('all', 'postgres', 'peer'),
        LocalRule('all', 'all', 'peer'),
    ], default=False)

    # setup db/user
    require.postgres.user(DB_USER)
    require.postgres.database(DB_NAME, DB_USER)
    require.package('postgresql95-contrib')
    sudo("psql -d %s -c 'CREATE EXTENSION IF NOT EXISTS CITEXT'" % DB_NAME, user='postgres')

    # setup virtual environment
    require.rpm.repository('epel')
    require.packages([
        'git',
        'gcc',
    ])

    require.python.pip()
    require.python.package('virtualenv', use_sudo=True)
    require.python.virtualenv('venv')

    with python.virtualenv('venv'), cd(PROJECT_NAME):
        require.python.requirements('requirements.txt', upgrade=True)
