import json

from langchain_community.document_transformers import DoctranPropertyExtractor
from langchain_community.document_transformers import DoctranQATransformer
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

urls = ["https://genius.com/Imagine-dragons-demons-lyrics"]
loader = AsyncHtmlLoader(urls)
docs = loader.load()
html2text = Html2TextTransformer()
docs_transformed = html2text.transform_documents(docs)
documentContent = docs_transformed[0].page_content[1000:2000]
print(documentContent)

documents = [Document(page_content=documentContent)]
properties = [
    {
        "name": "title",
        "description": "What title could you give to this song?",
        "type": "string",
        "required": True,
    },
    {
        "name": "summary",
        "description": "How would you summarize this song?",
        "type": "string",
        "required": True,
    },
    {
        "name": "mentions",
        "description": "A list of people mentioned in this song.",
        "type": "array",
        "items": {
            "name": "full_name",
            "description": "The full name of the person mentioned.",
            "type": "string",
        },
        "required": True,
    },
    {
        "name": "category",
        "description": "Explain what category of christian holiday is described in this song?",
        "type": "string",
        "required": True,
    },
]
property_extractor = DoctranPropertyExtractor(properties=properties)
extracted_document = property_extractor.transform_documents(
    documents, properties=properties
)
print(json.dumps(extracted_document[0].metadata, indent=2))