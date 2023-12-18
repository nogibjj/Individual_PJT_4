[![Continuous Integration Quality Check](https://github.com/nogibjj/Individual_PJT_4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Individual_PJT_4/actions/workflows/cicd.yml)

# Individual Project 4: Deploying a Food Recommendation Service on Azure
## Overview
This repository demonstrates the deployment process of a web-based food recommendation service using Azure App Service. The user interface allows users to input preferences, moods, or occasions to receive personalized food recommendations, along with a link for food delivery via DoorDash.

## Executive Summary for Strategic Action
This proof-of-concept introduces a new customer-engaging feature where users express their feelings, thoughts, or recent events to receive food recommendations and a link for ordering food through DoorDash. Key action items include:

1. User Interface Design: Collaborate with the design team to create an interface suitable for incorporating this feature.
2. Feature Deployment: Integrate this feature into the food company's website.
3. Data Analysis for Future Enhancements: Utilize conversion rates to assess the feature's effectiveness and analyze user behavior for future sales campaign audience targeting.

## Feature Walkthrough 
1. Users can input thoughts or feelings into a small box, and if left blank, pressing the submit button will reload the page.
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/41ff9002-b567-4982-9993-c2a1329a27c1)

2. An input expressing a feeling serves as a prompt for the Chat GPT API to generate food recommendations.
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/14745091-b722-489d-ac27-a13ac4a177a4)

3. Upon submission, users are directed to a page displaying the top three food recommendations along with a DoorDash link for convenient ordering.
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/26c93eed-6278-4413-bd8e-641bc0ace0ac)
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/ee436922-b496-4298-b39d-84b42ad4ef1c)


## Upload the Docker image for other to run

After creating the Docker image for the app, share it on Docker Hub. Users can download the image file and run the app locally using the provided Docker run command.

```
Docker run [image_name]
docker build -t myappfoodrecommendation/myapp .
```
Result of Building a Docker Image
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/8db5f8cd-f743-4cfb-8117-30fdefae6a6b)
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/29cd1f4a-5a84-423a-a0b0-ae94e396e4fb)


## Deploy service on Azure

Once the app is built, use the Docker file to create an image. To deploy the app on Azure, follow these steps:

1. Create an Azure Container Registry.
2. Create a container repository and push the Docker image onto the repository.
3. Use the Azure App Service to deploy the app on Azure.

![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/35d0f122-d607-463f-aea2-f169e125b959)
![image](https://github.com/nogibjj/Individual_PJT_4/assets/141780408/17803cc2-4dea-4ac8-9fa1-4f56de655f16)


Use the provided codes during a similar process to configure Azure cloud services, Docker images, and deploy the web app.

```
# Build Docker image and tag it for the Azure Container Registry
docker build -t [RegistryName.azurecr.io]/myapp .

# Install Homebrew for Azure CLI installation (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update && brew install azure-cli

# Log in to Azure
az login --tenant 9665bee9-59c7-43dd-b86b-1b15d598b932
az acr login --name [RegistryName]

# Push Docker image to Azure Container Registry
docker push [RegistryName.azurecr.io]/myapp

```
