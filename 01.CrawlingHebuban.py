import tweepy
import pandas as pd

def create_dictionary_user(includes_users):
    #Input = Includes dari Expansion dari User yang berisi ID, Name Profile, Username
    #Output = Dictionary dengan key = id_user dan values = username. Contoh "123456789" : "RickAstley"
    list_user_id = []
    list_username = []

    for i in range(len(includes_users)):
        list_user_id.append(str(includes_users[i].id))
        list_username.append(includes_users[i].username)

    return dict(zip(list_user_id, list_username))

def create_dictionary_referenced(includes_tweets):
    #Input = Includes dari Expansion dari Tweet referenced berisi ID Tweet dan ID Author
    #Output = Dictionary dengan key = tweet_id dan values = author_id. Contoh "987654321" : "123456789"
    list_ref_tweet_id = []
    list_auth_id = []

    for i in range(len(includes_tweets)):
        list_ref_tweet_id.append(str(includes_tweets[i].id))
        list_auth_id.append(str(includes_tweets[i].author_id))

    return dict(zip(list_ref_tweet_id, list_auth_id))

def get_data(data, dict_user, dict_referenced):
    #Input = Data dari Tweet Field, dan juga dictionary dari 2 function sebelumnya
    #Output = Mendapatkan data satu per satu dan ditampung ke variabel
    tweet_id = str(data.id)
    author_id = str(data.author_id)
    text = data.text
    created_at = str(data.created_at)
    #Validasi Referenced Tweets Jika Ada
    if (validation(data.referenced_tweets)):
        referenced_tweet_id = str(data.referenced_tweets[0].id)
        relation = data.referenced_tweets[0].type
        referenced_author_id = dict_referenced[referenced_tweet_id]
        referenced_author_username = dict_user[referenced_author_id]
    #Jika tidak ada Referenced Tweets
    else:
        referenced_tweet_id = "Tidak ada referenced tweet"
        relation = "Tidak ada relasi"
        referenced_author_id = "Tidak ada referenced tweet"
        referenced_author_username = "Tidak ada referenced tweet"
    lang = data.lang
    source = data.source
    author_username = dict_user[author_id]

    return tweet_id, author_id, text, created_at, referenced_tweet_id, relation, lang, source, referenced_author_id, referenced_author_username, author_username

def validation(isi):
    #Mengembalikan True jika isi tidak None (berisi)
    #Mengembalikan False jika isi kosong
    return (isi != None)

#================================================ MAIN FUNCTION ================================================

# Parameter/Variabel yang bisa di-custom / isi sendiri
# 1. Bearer Token API v2
bearer_token = "INSERT YOUR BEARER TOKEN"

# 2. Query
query = "#ヘブバン"

# 3. Max Results (per page) dengan rentang nilai min. 10 dan max. 100
max_results = 100

# 4. Banyaknya page. Jumlah tweet yang dicrawl adalah max_results x page
limit = 150

# Auth
client = tweepy.Client(bearer_token)

# Inisialisasi List agar dijadikan kolom Dataframe
list_tweet_id = []
list_author_id = []
list_text = []
list_created_at = []
list_referenced_tweet_id = []
list_relation = []
list_lang = []
list_source = []
list_referenced_author_id = []
list_referenced_author_username = [] 
list_author_username = []

# Proses Crawling
pages = tweepy.Paginator(client.search_recent_tweets, query,
                            max_results=max_results, tweet_fields=["id", "author_id", "text", "created_at", "referenced_tweets", "lang", "source"], 
                            expansions=["author_id", "referenced_tweets.id.author_id"], limit=limit)

# Dilakukan per pages
i = 0
for page in pages:
    # Melakukan output progress program ada pada page ke berapa
    i += 1
    print("Page ke-" + str(i))
    # Membuat Dictionary dengan 2 Function Teratas dari Expansions
    dict_user = create_dictionary_user(page.includes["users"])
    dict_referenced = create_dictionary_referenced(page.includes["tweets"])

    # Mendapatkan Data dari Tweet_Fields
    for j in range(len(page.data)):
        # Cek jika tidak ada error
        if (page.errors == []):
            # Function untuk mendapatkan data
            tweet_id, author_id, text, created_at, referenced_tweet_id, relation, lang, source, referenced_author_id, referenced_author_username, author_username = get_data(page.data[j], dict_user, dict_referenced)
            # Menampung hasil get ke list
            list_tweet_id.append(tweet_id)
            list_author_id.append(author_id)
            list_text.append(text)
            list_created_at.append(created_at)
            list_referenced_tweet_id.append(referenced_tweet_id)
            list_relation.append(relation)
            list_lang.append(lang)
            list_source.append(source)
            list_referenced_author_id.append(referenced_author_id)
            list_referenced_author_username.append(referenced_author_username)
            list_author_username.append(author_username)

# Mengubah menjadi Dictionary agar dapat diubah menjadi Dataframe
calon_dataframe = {
    'author_username' : list_author_username,
    'referenced_author_username' : list_referenced_author_username,
    'author_id' : list_author_id,
    'referenced_author_id' : list_referenced_author_id,
    'tweet_id' : list_tweet_id,
    'referenced_tweet_id' : list_referenced_tweet_id,
    'text' : list_text,
    'created_at' : list_created_at,
    'relation' : list_relation,
    'lang' : list_lang,
    'source' : list_source
}

# Mengubah ke Dataframe
hebuban_df = pd.DataFrame(calon_dataframe)

# Export ke Excel
hebuban_df.to_excel(r'hebuban_crawling.xlsx', index=False, header=True)

# Selesai
print("\nCOMPLETED!")