## Activo
[![Maintainability](https://api.codeclimate.com/v1/badges/6594af3ff034d4737892/maintainability)](https://codeclimate.com/repos/5b16a8d8e4ba1a02d5001488/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/6594af3ff034d4737892/test_coverage)](https://codeclimate.com/repos/5b16a8d8e4ba1a02d5001488/test_coverage)

An asset-management tool for Andela

# Description 
 The **activo-api** is the backbone of an application for managing physical assets of the organisation. The project enables  centralised management of assets of the organisation. The the api provides features for registering the allocation and usage of assets, repairs and conditions of devices, allocation of computer devices and seat allocations.

 ## Key Application features  
1.	Inventory Management
2.	Asset Allocations
3.	Asset Maintenance & Repair logs

## Development set up
- Check that python 3 is installed.
    ```
    python --v
    >> Python 3.6.5
    ``` 
- Check that virtualenv is installed.
    ```
    virtualenv --version
    >> Python 15.2.0
    ```
   
- Check that pip is installed.
    ```
    pip --version
    >> Python 10.0.1
    ``` 
    
- Check that postgres is installed.
    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1

    ```

- Clone the activo-api repo and cd into it
    ```
    git clone https://github.com/andela/activo-api.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in .env file
    ```
    FLASK_ENV = "development" # Takes either development, production, testing
    DATABASE_URI = "" # Development and production db uri
    TEST_DATABASE_URI = "" # Testing db uri
    ```
- Running migrations
    - initialize the database:
        ```
        flask init db
        ```    
    - Migrate database:
        ```
        flask db migrate
        ```
    - Upgrade to new structure:
        ```
        flask db upgrade
        ```
- Run application.
    ```
    python manage.py runserver
    ```



## Contribution guide
##### Contributing
All proposals for contribution must satisfy the guidelines in the product wiki.
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.This Project shall be utilising a [Pivotal Tracker board](https://www.pivotaltracker.com/n/projects/2170023) to track  the work done.

 ##### Pull Request Process
- A contributor shall identify a task to be done from the [pivotal tracker](https://www.pivotaltracker.com/n/projects/2170023).If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
- The Contributor shall then create a branch off  the ` develop` branch where they are expected to undertake the task they have chosen.
- After  undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review. 
- If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `develop` by the owners of this repository.
