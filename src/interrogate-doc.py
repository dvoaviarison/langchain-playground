import json

from langchain_community.document_transformers import DoctranPropertyExtractor
from langchain_community.document_transformers import DoctranQATransformer
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documentContent="""
# Because (F - Ab)
[Watch the Lamb (C)](https://www.notion.so/Watch-the-Lamb-C-d79e95a6afbc4bbb8975b951e7ce34c7?pvs=21)
[Risen (Bb)](https://www.notion.so/Risen-Bb-9dbb31b6ced3451db8b5c2e371372f3f?pvs=21)
[We believe (E)](https://www.notion.so/We-believe-E-956b95aee7574b359af43c4f86581ef5?pvs=21)
[Draw me close to you (G)](https://www.notion.so/Draw-me-close-to-you-G-ba567af9fcc640829a0ab558020ba976?pvs=21)
[Shine Jesus Shine (G)](https://www.notion.so/Shine-Jesus-Shine-G-c7761319e0e7402e9a9bc289a7ccdc1d?pvs=21)
[You raise me up (Bb)](https://www.notion.so/You-raise-me-up-Bb-87b40243d9cd4197a8d8310846621004?pvs=21)
[The power of Your love (G) *](https://www.notion.so/The-power-of-Your-love-G-9d5232a855ce417faf8e40990249b0a2?pvs=21)
[Hymn of heaven (Bb)](https://www.notion.so/Hymn-of-heaven-Bb-e28a6d6ff9a94af592f2139f0cbfa4e9?pvs=21)
[How great is our God (F)](https://www.notion.so/How-great-is-our-God-F-4f735c0f219b4f7a95083512b294fd2c?pvs=21)
[He wants it all (Eb)](https://www.notion.so/He-wants-it-all-Eb-7ae748267a1a4db8b543a9a0dcd68874?pvs=21)
[Still (Bb) *](https://www.notion.so/Still-Bb-4c17bc0f80a44a92a448f374ca9f5169?pvs=21)
[Gratitude (F)](https://www.notion.so/Gratitude-F-be0e62a698d04d53902238394d3d77aa?pvs=21)
[The first Noel (C)](https://www.notion.so/The-first-Noel-C-9f48498e5c5a4289a5077ab8fd998d8a?pvs=21)
[Oh Holy night (G)](https://www.notion.so/Oh-Holy-night-G-9c6228f26c404d2a86d150675b6c1d5f?pvs=21)
[Mary did you know (C)](https://www.notion.so/Mary-did-you-know-C-787e012e53bb49de89d0cb66d428f359?pvs=21)
[Light of the world (D)](https://www.notion.so/Light-of-the-world-D-ac7922271a6d49c1be86fac9c90a540e?pvs=21)
[10,000 Reasons (C)](https://www.notion.so/10-000-Reasons-C-cef4f6c34a9a43bba26c824944e98f3e?pvs=21)
[This is the air I breathe (G)](https://www.notion.so/This-is-the-air-I-breathe-G-a7ee2a9c29dd43a9b050640777a01cb0?pvs=21)
[Joy in the morning (Bb)](https://www.notion.so/Joy-in-the-morning-Bb-3a63661c0b1c43d4a697deb46bbce3f5?pvs=21)
[Here I am to worship Kids (C)](https://www.notion.so/Here-I-am-to-worship-Kids-C-9aeb67f396a74456ab1ad2fa1109d294?pvs=21)
[Here I am to worship (C)](https://www.notion.so/Here-I-am-to-worship-C-66b415dc6ac345839241574061a51e6f?pvs=21)
[Hosanna (D)](https://www.notion.so/Hosanna-D-4d3b2d68cecb40b5a2fbaf56ca640c8c?pvs=21)
[Mighty to save (E)](https://www.notion.so/Mighty-to-save-E-283f8e9618ef41b695fd016386a4edcd?pvs=21)
[Worthy is the lamb (G)](https://www.notion.so/Worthy-is-the-lamb-G-943a1297e1cf4ce592891c5dadc71624?pvs=21)
[Peace Be Still (Ab)](https://www.notion.so/Peace-Be-Still-Ab-6e959d62b56d4621bcea2d61424ad469?pvs=21)
[Holy Spirit Rain Down (F)](https://www.notion.so/Holy-Spirit-Rain-Down-F-5c25ab238ba6456fa7f48479efee80fb?pvs=21)
[You are God alone (Db)](https://www.notion.so/You-are-God-alone-Db-52c149896dc348bc98131c51fc6e0817?pvs=21)
[God will make a way (C)](https://www.notion.so/God-will-make-a-way-C-c216a960792049d7afd182bab960b453?pvs=21)
[My God Is Still The Same](https://www.notion.so/My-God-Is-Still-The-Same-663e17fe203e4ee8bd0980b27d07b120?pvs=21)
[Who Am I](https://www.notion.so/Who-Am-I-63a02b25af6c4b259481f0c3031bf206?pvs=21)
[Undo](https://www.notion.so/Undo-2788acc8b46344f39cf205a2627a5467?pvs=21)
[Indescribable](https://www.notion.so/Indescribable-6447904782234ffbaa44b507841c8539?pvs=21)
[Cornerstone](https://www.notion.so/Cornerstone-ec1b5f997dbc40169b819cde96000665?pvs=21)
[You Are My King (Amazing Love)](https://www.notion.so/You-Are-My-King-Amazing-Love-0f48f3bd46d547adbd26ab2c4f78ec19?pvs=21)
[He is exalted (F)](https://www.notion.so/He-is-exalted-F-7e9448c724a3460c8e6a19f135016040?pvs=21)
[Beautiful One (Bb)](https://www.notion.so/Beautiful-One-Bb-7c66bb7d452a48e1b84b2a6b9e94dfd9?pvs=21)
[Every Praise](https://www.notion.so/Every-Praise-b5b5633676124e15ba9ad7dfeb6bce25?pvs=21)
[I give myself away](https://www.notion.so/I-give-myself-away-ac49b7036fff454aa32d1d9af5322706?pvs=21)
[**Testify To Love (C)**](https://www.notion.so/Testify-To-Love-C-4645942537d5402bacf9e3ea60293094?pvs=21)
[**Give thanks (D)**](https://www.notion.so/Give-thanks-D-4f5117dfddde4b7a8d3e038ea93bc8ad?pvs=21)
[Agnus Dei (G)](https://www.notion.so/Agnus-Dei-G-8440152f779d45cdbb9c13f39a7e46fc?pvs=21)
[The goodness of God (Ab) ](https://www.notion.so/The-goodness-of-God-Ab-06ec7cc1673f44fda852c3a23283e245?pvs=21)
[The power of the cross](https://www.notion.so/The-power-of-the-cross-ed5d3f5c886f4c2c887e1c27b5e0ee08?pvs=21)
[I'm So amazed](https://www.notion.so/I-m-So-amazed-85ae7ee7117344398f24f7bdbc3b0f80?pvs=21)
"""

documents = [Document(page_content=documentContent)]
properties = [
    {
        "name": "song_list",
        "description": "Give me 3 songs. the first on should be worship, the second praise and the thirs a good opening song",
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