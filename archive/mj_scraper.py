import lyricsgenius
import pandas as pd
import time

client_secret = "_6KsxWpifvCH5vzQSEvz3JK3ljkGf51nFjDn8T1daMzGbkXi-NEIyGPZpmq0mia2w1N-TFCDegeas5g8_PqNAQ"
client_id = "lAMPzZWTzfH1amlRYL2zeAvplSfRLpQ4yAMODOBMf8y_K6UUb556dLKWVNv--C4f"
token = "45fu0Tzz40ybauiM4C4zY48wS8QgsMg-wAZGjOWxTDFu_t2rlQEHpMOBlygwDuaZ"

# connect to genius
genius = lyricsgenius.Genius(
    token,
    timeout=15,
    retries=3,
    remove_section_headers=True,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)", "(Demo)", "(Instrumental)"]
)

# search michael jackson
artist = genius.search_artist(
    "Michael Jackson",
    max_songs=50,
    sort="popularity"
)

# build the DataFrame
titles = []
lyrics_list = []

for song in artist.songs:
    titles.append(song.title)
    lyrics_list.append(song.lyrics)

    print(song.title)

    time.sleep(0.5)

# create the DataFrame
songs_df = pd.DataFrame({
    "title": titles,
    "lyrics": lyrics_list
})

# save CSV
songs_df.to_csv("michael_jackson_lyrics.csv", index=False)

print(songs_df.head())