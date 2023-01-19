import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS=''

client= motor.motor_asyncio.AsuncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get("user_collection")
public_posts = database.get("public_posts")
private_collection = database.get("private_collection")

def user_helper (user) -> dict:
    return{
        "id": str(user["_id"]),
        "fullname":user["fullname"],
        "email": user["email"],
        "interests": user["interests"]        
    }
def post_helper (post) -> dict:
    return{
        "id": str(post["_id"]),
        "song_title":post["song_title"],
        "artist": post["artist"],
        "brand_record": post["brand_record"],
        "year": post["year"]          
    }

#Retrive public songs

async def retrieve_songs():
    songs = []
    async for song in  public_posts.find():
        songs.append(post_helper(song))
    return song

#add a new song
async def add_song(song_data:dict)-> dict:
    song= await public_posts.insert_one(song_data)
    new_song =  await public_posts.find_one({"id":song.inserted_id})
    return post_helper(new_song)



