## Smile Direct Club Challenge API

### How do I test it?
We use pytest as our testing framework... You can test the project by running:

`pytest`

### How do I run it?
Serverless can emulate an AWS lambda environment locally, you can run the project locally by running:

`sls wsgi serve`

### How do I deploy it
Serverless will take care of setting up our CloudFormation templates and deploying our project, If you have an AWS envionment set up, you can deploy it using:

`sls deploy`

### How do I tear it down?
Serverless will delete the Lambda and the CloudFormation template if you run:

`sls remove`