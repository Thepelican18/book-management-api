Book-Management-API
Design Decisions
I decided to structure the project into 4 main folders, reflecting the 4 layers of the DDD design:

Domain
This layer contains all the domain logic and should be isolated from any external changes. 
    It is divided into three subfolders:

        models: Contains the entities, with the only domain entity being book.py. Many developers use Pydantic here, which I believe is a mistake because if the framework ever changes, it could affect the domain.

        Repositories: Contains the contracts that the infrastructure layer follows to work with the domain.

        value_objects: A folder to store value objects. I decided that the ISBN should be a value object and that its format should be validated according to the domain’s expectations. With this, the domain layer is complete. 

    It could have included a services folder for domain-specific services, but it wasn’t necessary in this case.

Application
This folder represents the application layer, which is responsible for orchestrating operations between the Domain and Infrastructure layers. 
    It contains one subfolder:

        services: Contains the application services, in this case, a BookService that implements the CRUD logic and the search function. Initially, I had added two more folders, commands and queries, to separate the write and read logic. However, I decided to remove them because I considered them over-engineering for this use case.

        Infrastructure
        This layer handles persistence and external services. It contains one subfolder:

        repositories: This subfolder contains the implementation of different assets following the domain contract. In other words, by following the domain contract, we can use any database without affecting the domain. 
    
    I decided to use Python objects stored in pickle files for persistence because it was quick and allowed me to avoid losing data when the server is shut down. It would be easy to adapt this to a database like PostgreSQL using SQLAlchemy.

Interface
Finally, this folder corresponds to the presentation layer (API), which exposes functionality through HTTP endpoints. It also handles authentication and validates input and output data. 
    It contains three subfolders:

        dependencies: Contains the dependencies, in this case, the security dependency.

        routes: The endpoints that access the functionality.

        schemas: The Pydantic models to control data input and output in the routes. The routing for books is protected by the api_key dependency.

Now, let’s take a look at the configuration file and main:
    
    config.py: I opted for a basic configuration because nothing more is needed. I also considered that the API key and other configurations should come from environment variables, not be hard-coded. Since this is a simple API, I left it as is.

    main.py: I decided to handle domain exceptions here, registering them globally. Although I don’t love the idea of importing from the domain layer into the presentation layer, I think it is acceptable in this case.

Steps to run server:
    1.python -m venv book_api_venv 
    2.book_api_venv\Scripts\activate(windows users) or source book_api_venv/bin/activate (linux users).
    3."pip install -r requirements.txt" on root folder
    4."python main.py" on app folder

You can access the documentation by starting the server and going to http://127.0.0.1:5080/docs.

You can use integration test using "pytest .\tests\" command on root project path