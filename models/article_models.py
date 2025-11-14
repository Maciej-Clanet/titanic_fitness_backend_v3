from pydantic import BaseModel

class ArticleThumbnail(BaseModel): 
   title: str 
   description: str 
   slug: str       #url friendly version of title ex: "sleep" 
   link: str       #full link ex: article/sleep 


class ArticleDetail(BaseModel): 
   title: str 
   content_html: str   #HTML stored as a string 