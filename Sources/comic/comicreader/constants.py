
#~~~~~~~~~~~~~~~~IMAGE CONSTANTS~~~~~~~~~~~~~~~#

IMAGE_STATUS_PENDING = 0
IMAGE_STATUS_DOWNLOAD_FAILED = 1
IMAGE_STATUS_DOWNLOAD_SUCCESS = 2

IMAGE_STATUS_CHOICES = (
    (IMAGE_STATUS_PENDING, "Pending"),
    (IMAGE_STATUS_DOWNLOAD_FAILED, "Download failed"),
    (IMAGE_STATUS_DOWNLOAD_SUCCESS, "Download success"),
)

API_KEYWORD_TYPE_CATEGORY = 'category'
API_KEYWORD_TYPE_FAVORITE = 'favorite'
API_KEYWORD_TYPE_READ_MOST = 'read-most'
API_KEYWORD_TYPE_NEW = 'new'
API_KEYWORD_TYPE_SEARCH = 'search'
API_KEYWORD_SEARCH_TYPE_AUTHOR = 'author'
API_KEYWORD_SEARCH_TYPE_EBOOK = 'ebook_name'
API_KEYWORD_TYPE_HOT = 'hot'


API_LIMIT_ELEMENT_SEARCH = 10
API_BLOCK_CATEGORY = ['18+','16+','Ecchi','Adult']
API_ID_EBOOK_HOT = [1,4,15,7,12,14,20,54,25,76,43,11]

API_PATH_ABS= '/home/ubuntu/Comicreader/'
# "/home/zero/PycharmProjects/ComicReader/Downloads"  #server:    /home/ubuntu/Comicreader/