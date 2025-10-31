To run the api tests:
Make sure you are inside the project folder:`cd pytest_demo`

`docker build -t pytest_demo:latest .`

`docker run -it pytest_demo:latest`

To run the playwright tests:
Make sure you are inside the project folder:`cd playwright_tests`

`docker build -t playwright_tests:latest .`

`docker run -it playwright_tests:latest`