from os import replace
import urllib.parse

Prefix = 'https://portal.azure.com/#create/Microsoft.Template/uri/'

##ADD IN CONTAINER
ContainerRoot = 'https://stuksazd.blob.core.windows.net/testarm/'

##ADD IN FILE
ContainerFile = 'mg.json'

##ADD IN SAS
SAS = 'sp=rl&st=2024-10-04T12:16:25Z&se=2024-11-08T21:16:25Z&spr=https&sv=2022-11-02&sr=c&sig=Oa732GZ9b8uuNBKN0pH3sjiJIPUvSvDEKacjWz%2F3Gto%3D'

FileAndSAS = (f'{ContainerFile}?{SAS}')

EncodedRoot = urllib.parse.quote(ContainerRoot)
EncodedFileAndSAS = urllib.parse.quote(FileAndSAS)

ReplacedEncodedRoot = EncodedRoot.replace("/", "%2F")


EncodedURL = (f'{Prefix}{ReplacedEncodedRoot}{EncodedFileAndSAS}')


print(EncodedURL)