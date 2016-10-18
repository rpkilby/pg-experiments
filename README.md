# pg-experiments

Quick(ish) & simple vagrant provisioning for testing out `django.contrib.postgres` features (jsonb, hstore).


## Instructions:

1. Install vagrant
2. Provision the vagrant vm:

  ```sh
  $ vagrant up
  $ virtualenv .env
  $ .env/bin/pip install -r deploy-requirements.txt
  $ .env/bin/fab vagrant provision
  ```

3. `vagrant ssh`
4. ...


## Usage:

A virtualenv has been setup as `/home/vagrant/venv`. The project code is synced and located under `/home/vagrant/pg-experiments`.
