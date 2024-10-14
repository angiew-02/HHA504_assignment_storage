{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOn2JHehzz3jHMDPgEV1LAL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/angiew-02/HHA504_assignment_storage/blob/main/azure-storage-blob.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "20VvZ0jXX11t",
        "outputId": "206e6ab9-0b33-44c0-f61d-d6f550328773"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting azure-storage-blob\n",
            "  Downloading azure_storage_blob-12.23.1-py3-none-any.whl.metadata (26 kB)\n",
            "Collecting azure-identity\n",
            "  Downloading azure_identity-1.19.0-py3-none-any.whl.metadata (80 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m80.6/80.6 kB\u001b[0m \u001b[31m1.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting python-dotenv\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Collecting azure-core>=1.30.0 (from azure-storage-blob)\n",
            "  Downloading azure_core-1.31.0-py3-none-any.whl.metadata (39 kB)\n",
            "Requirement already satisfied: cryptography>=2.1.4 in /usr/local/lib/python3.10/dist-packages (from azure-storage-blob) (43.0.1)\n",
            "Requirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from azure-storage-blob) (4.12.2)\n",
            "Collecting isodate>=0.6.1 (from azure-storage-blob)\n",
            "  Downloading isodate-0.7.2-py3-none-any.whl.metadata (11 kB)\n",
            "Collecting msal>=1.30.0 (from azure-identity)\n",
            "  Downloading msal-1.31.0-py3-none-any.whl.metadata (11 kB)\n",
            "Collecting msal-extensions>=1.2.0 (from azure-identity)\n",
            "  Downloading msal_extensions-1.2.0-py3-none-any.whl.metadata (7.6 kB)\n",
            "Requirement already satisfied: requests>=2.21.0 in /usr/local/lib/python3.10/dist-packages (from azure-core>=1.30.0->azure-storage-blob) (2.32.3)\n",
            "Requirement already satisfied: six>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from azure-core>=1.30.0->azure-storage-blob) (1.16.0)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/dist-packages (from cryptography>=2.1.4->azure-storage-blob) (1.17.1)\n",
            "Requirement already satisfied: PyJWT<3,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from PyJWT[crypto]<3,>=1.0.0->msal>=1.30.0->azure-identity) (2.9.0)\n",
            "Collecting portalocker<3,>=1.4 (from msal-extensions>=1.2.0->azure-identity)\n",
            "  Downloading portalocker-2.10.1-py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12->cryptography>=2.1.4->azure-storage-blob) (2.22)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.21.0->azure-core>=1.30.0->azure-storage-blob) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.21.0->azure-core>=1.30.0->azure-storage-blob) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.21.0->azure-core>=1.30.0->azure-storage-blob) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.21.0->azure-core>=1.30.0->azure-storage-blob) (2024.8.30)\n",
            "Downloading azure_storage_blob-12.23.1-py3-none-any.whl (405 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m405.6/405.6 kB\u001b[0m \u001b[31m8.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading azure_identity-1.19.0-py3-none-any.whl (187 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m187.6/187.6 kB\u001b[0m \u001b[31m11.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading azure_core-1.31.0-py3-none-any.whl (197 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m197.4/197.4 kB\u001b[0m \u001b[31m11.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading isodate-0.7.2-py3-none-any.whl (22 kB)\n",
            "Downloading msal-1.31.0-py3-none-any.whl (113 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m113.1/113.1 kB\u001b[0m \u001b[31m7.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading msal_extensions-1.2.0-py3-none-any.whl (19 kB)\n",
            "Downloading portalocker-2.10.1-py3-none-any.whl (18 kB)\n",
            "Installing collected packages: python-dotenv, portalocker, isodate, azure-core, azure-storage-blob, msal, msal-extensions, azure-identity\n",
            "Successfully installed azure-core-1.31.0 azure-identity-1.19.0 azure-storage-blob-12.23.1 isodate-0.7.2 msal-1.31.0 msal-extensions-1.2.0 portalocker-2.10.1 python-dotenv-1.0.1\n"
          ]
        }
      ],
      "source": [
        "!pip install azure-storage-blob azure-identity python-dotenv"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## link for azure connection/security: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-python-get-started?tabs=account-key\n",
        "from azure.identity import DefaultAzureCredential\n",
        "from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient\n",
        "import os\n",
        "from dotenv import load_dotenv\n",
        "\n",
        "load_dotenv()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yAOXEdEJX3zR",
        "outputId": "fed6a94b-65ef-45a2-e954-7b5a887348ee"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "account_url_link = \"https://mystoragepractice123.blob.core.windows.net\"\n",
        "os.getenv(\"AZURE_STORAGE_ACCESS_KEY\")"
      ],
      "metadata": {
        "id": "RTcPKit-X66x"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "## function to list containers https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-containers-list-python\n",
        "def get_blob_service_client_account_key():\n",
        "    # TODO: Replace <storage-account-name> with your actual storage account name\n",
        "    account_url = account_url_link\n",
        "    shared_access_key = os.getenv(\"AZURE_STORAGE_ACCESS_KEY\")\n",
        "    credential = shared_access_key\n",
        "\n",
        "    # Create the BlobServiceClient object\n",
        "    blob_service_client = BlobServiceClient(account_url, credential=credential)\n",
        "\n",
        "    return blob_service_client"
      ],
      "metadata": {
        "id": "dn82aPnHYBfh"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "blob_service_client = get_blob_service_client_account_key()"
      ],
      "metadata": {
        "id": "yr8O0aXzYD1B"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def list_containers(blob_service_client):\n",
        "    containers = blob_service_client.list_containers(include_metadata=True)\n",
        "    for container in containers:\n",
        "        print(container['name'], container['metadata'])"
      ],
      "metadata": {
        "id": "KWPhn5IGYLr0"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "list_containers(blob_service_client)"
      ],
      "metadata": {
        "id": "zEARGE-PbV6B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def upload_blob_file(blob_service_client, container_name, filepathstring, filenamestring):\n",
        "    container_client = blob_service_client.get_container_client(container=container_name)\n",
        "    with open(file=os.path.join(filepathstring, filenamestring), mode=\"rb\") as data:\n",
        "        blob_client = container_client.upload_blob(name=filenamestring, data=data, overwrite=True)"
      ],
      "metadata": {
        "id": "vsq2Uz4BYPxB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "upload_blob_file(blob_service_client, 'storagepractice', './', 'pexels-jonaskakaroto-736230.jpg')"
      ],
      "metadata": {
        "id": "mo1zXJE5aIc-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def list_blobs_flat(blob_service_client, container_name):\n",
        "    container_client = blob_service_client.get_container_client(container=container_name)\n",
        "\n",
        "    blob_list = container_client.list_blobs()\n",
        "\n",
        "    for blob in blob_list:\n",
        "        print(f\"Name: {blob.name}\")"
      ],
      "metadata": {
        "id": "c2qdBOGRYmK6"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "list_blobs_flat(blob_service_client, 'storagepractice')"
      ],
      "metadata": {
        "id": "E2ddabCuaLBB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}