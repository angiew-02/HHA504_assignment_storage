# HHA504_assignment_storage
The objective of this assignment is to familiarize you with cloud storage services in Azure and Google Cloud Platform (GCP). To learn how to upload files to Azure Blob Storage and GCP Cloud Storage using both Python and the platform's GUI.
# Upload Files Using the GUI
### *Azure Blob Storage*
![Azure Storage](https://github.com/user-attachments/assets/facaebd7-cfcf-407e-b578-a3e88ec965a8)
![Azure Blob](https://github.com/user-attachments/assets/98d1b7b1-afbc-42c2-af81-caaad9eb8808)
### *GCP Blob Storage*
![GCP Storage](https://github.com/user-attachments/assets/3ac8927e-7621-4efa-bda2-6c4f2bfe7049)
![GCP Blob](https://github.com/user-attachments/assets/d105e622-d6f0-4ac4-9748-a9d8c2647d6c)
# Explore Storage Features
### *Azure*
* Azure consist of access control such as shared access signature which allow for limited access to blob storage resources without showing the account key.
* The data security contains encryption where data stroed in blob stoage is automatically encrypted and you can manage your own encryption keys through Azure Key Vault. In addition the data is encrypted using HTTPS during transit
* For data management they have blob tiers which include hot which allow for frequently accessed data, cool which allow for infrequently accessed data with lower storage costs but higher access cost, and archive for rarely accessed data
### *GCP*
* GCP consist of access control such as identity and access management which uses IAM to control access to resources. In addition they have Access Control Lists which provide different levels of access control on buckets and objects and can generate signed URLs that provide temporary access to specific objects
* The data security contains encryption where data is stored in GCS is automatically encrypted using Google-managed keys and the bucket policies can be used to set conditions on access to storage resources
* For data management they have lifesystem management which allows for you to define lifecycle rules to manage data automatically such as deleting objects after a specified age or move objects to different storage classes. They offere different storage classes such as standard which is for frequently accessed data, nearline used for data that is accessed less than once a month, coldline for data that is accessed less than once a year, and achive which is for data that is rarely accessed and is meant for long-term storage. 
