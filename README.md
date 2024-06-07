# Agriculture Chatbot

This project is an Agriculture Chatbot designed to answer questions related to organic farming. It leverages AWS Bedrock for natural language processing and vector embeddings, and Streamlit for the web interface.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [IAM and AWS Bedrock Access](#iam-and-aws-bedrock-access)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The Agriculture Chatbot is a question-answering system built to provide information about organic farming. The system uses Langchain for natural language processing and AWS Bedrock for embedding and inference. The chatbot is deployed using Streamlit for an interactive user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Version 3.8 or higher.
- **AWS Account**: With necessary permissions for Bedrock and S3.
- **Streamlit**: Installation (`pip install streamlit`).
- **Boto3**: Installation (`pip install boto3`).
- **Langchain**: Installation (`pip install langchain`).

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/agriculture-chatbot.git
    cd agriculture-chatbot
    ```

2. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure AWS Credentials**

    Set up your AWS IAM access and secret keys using the AWS CLI:

    ```bash
    aws configure
    ```

    Follow the prompts to enter your AWS Access Key ID, Secret Access Key, region, and output format.


## Usage

1. **Create Embeddings**

    Run the `create_embeddings.py` script to ingest data from the `Data` directory, create vector embeddings, and save the FAISS index locally.

    ```bash
    python src/create_embeddings.py
    ```

2. **Start the Streamlit Application**

    Run the `main.py` script to start the Streamlit web application.

    ```bash
    streamlit run src/main.py
    ```

3. **Interact with the Chatbot**

    Open your web browser and go to the local Streamlit URL (usually `http://localhost:8501`). Ask questions about organic farming, and the bot will provide answers based on the ingested data.

## IAM and AWS Bedrock Access

### Create an IAM User

    1. Go to the AWS Management Console.
    2. Navigate to IAM (Identity and Access Management).
    3. Create a new user with programmatic access.
    4. Attach necessary policies for Bedrock and S3 access.
    5. Save the access key ID and secret access key.

### AWS Bedrock Access

Ensure your IAM user has the following permissions for Bedrock:

- `bedrock:InvokeModel`
- `bedrock:ListModels`

Additionally, configure the AWS CLI with the credentials of this IAM user as shown in the setup instructions.

## License

Distributed under the MIT License. See `LICENSE` for more information.
