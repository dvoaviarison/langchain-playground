import json

from langchain_community.document_transformers import DoctranPropertyExtractor
from langchain_community.document_transformers import DoctranQATransformer
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documentContent="""
"Bohemian Rhapsody" - Queen [Bb Major]
"Perfect" - Ed Sheeran [A Major]
"Africa" - Toto [F# Minor]
"Fly Me to the Moon" - Frank Sinatra [C Major]
"Gravity" - John Mayer [E Minor]
"Sweet Child o' Mine" - Guns N' Roses [D Minor]
"November Rain" - Guns N' Roses [Bb Major]
"While My Guitar Gently Weeps" - The Beatles [G Major]
"Under the Bridge" - Red Hot Chili Peppers [Bb Major]
"Purple Rain" - Prince [Bb Major]
"Creep" - Radiohead [A Minor]
"Can't Help Falling in Love" - Elvis Presley [C Major]
"All of Me" - John Legend [A Major]
"September" - Earth, Wind & Fire [F Major]
"All Along the Watchtower" - Jimi Hendrix [E Minor]
"Wish You Were Here" - Pink Floyd [C Major]
"Stairway to Heaven" - Led Zeppelin [A Minor]
"Viva la Vida" - Coldplay [Bb Major]
"My Heart Will Go On" - Céline Dion [E Major]
"Blinding Lights" - The Weeknd [F# Minor]
"""

documents = [Document(page_content=documentContent)]
properties = [
    {
        "name": "song_list",
        "description": "Give me 3 songs. The first should talk about missing someone, the second should talk about love, and the third should talk about heartbreak.",
        "type": "array",
        "items": {
            "name": "title",
            "description": "The title of the song with link",
            "type": "string",
        },
        "required": True,
    },
]
property_extractor = DoctranPropertyExtractor(properties=properties)
extracted_document = property_extractor.transform_documents(
    documents, properties=properties
)
print(json.dumps(extracted_document[0].metadata, indent=2))