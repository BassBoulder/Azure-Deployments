To use the "Deploy to Azure" button, the link needs to be constructed in a way that points to the Azure portal deployment UI: https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-azure-button

EXAMPLE:

https://portal.azure.com/#create/Microsoft.Template/uri/{encoded-template-url}
Where {encoded-template-url} is the encoded URL of the ARM template stored in the Azure Storage account. Use URL encoding for special characters (including SAS Key):

** ` ` ! " # $ % & ' ( ) * + , / : ; < = > ? @ [ \ ] ^ _ ` { | } ~**

You can use online encoders or python script:
import urllib.parse
encoded_string = urllib.parse.quote('Special & Char=Value')

Storage URL: 
https://stuksazd.blob.core.windows.net/prodarm/test_storage.json?sp=r&st=2024-09-11T17:03:34Z&se=2024-09-12T01:03:34Z&sv=2022-11-02&sr=b&sig={SAS token}%3D

Encoded Storage URL:
https%3A%2F%2Fstuksazd.blob.core.windows.net%2Fprodarm%2Ftest_storage.json%3Fsp%3Dr%26st%3D2024-09-11T17%3A03%3A34Z%26se%3D2024-09-12T01%3A03%3A34Z%26sv%3D2022-11-02%26sr%3Db%26sig%3D{SAS token}%253D

The "Deploy to Azure" button url would for example be:
(https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fstuksazd.blob.core.windows.net%2Fprodarm%2Ftest_storage.json%3Fsp%3Dr%26st%3D2024-09-11T17%3A03%3A34Z%26se%3D2024-09-12T01%3A03%3A34Z%26sv%3D2022-11-02%26sr%3Db%26sig%3D{SAS token}%253D). |
