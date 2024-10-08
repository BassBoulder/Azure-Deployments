#Import OS & Parse Functions
from os import replace
import urllib.parse

# Leave Unchanged - This is the URI to the Microsoft Portal
Prefix = 'https://portal.azure.com/#create/Microsoft.Template/uri/'

# Change - This is the URI to your Storage Container
ContainerRoot = '<Storage Container>'

# Change - This is the name of your File within the Storage Container
ContainerFile = '<fileanme.json>'

# Change - This is the SAS Key to your Storage Container (NO NOT LEAVE PUBLICLY AVAILABLE)
SAS = '<SAS KEY>'


# ENCODING PREPERATION
#################
FileAndSAS = (f'{ContainerFile}?{SAS}')

EncodedRoot = urllib.parse.quote(ContainerRoot)
EncodedFileAndSAS = urllib.parse.quote(FileAndSAS)
ReplacedEncodedRoot = EncodedRoot.replace("/", "%2F")
#################
# ENCODING OUTPUT
EncodedURL = (f'{Prefix}{ReplacedEncodedRoot}{EncodedFileAndSAS}')

# Copy - This is what you need to copy into your "Deploy to Azure" button wrapper code
print(EncodedURL)
