from youtube_transcript_api import YouTubeTranscriptApi

counter = 0

def containsNum(word):
    for c in word:
        if c.isdigit(): return False
    return True

def getID(url):
    url = url.split("v=")
    url = ''.join(url[1][:11])
    print(url)

    return url


while True:
    word = input("Enter a word to search (only characters): ")
    if word.isalnum() is False or containsNum(word) is False:
        print("characters only, try again")
    else:
        break


while True:
    url = input("Copy and paste a youtube URL: ")
    try:
        url = getID(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(url)
        break
    except:
        print("Invalid URL, try again.")
        pass


while True:
    lang = input("Enter a language code (2 letter abbreviation, ie English = 'en'): ")
    try:
        transcript = transcript_list.find_transcript([lang])
        break
    except:
        print('Language is not found.')
        pass


while True:
    exclusive = input("Should the word be exclusive and not part of another word? Y/N: ")
    if exclusive.lower() == 'y':
        new = " " + word + " "
        break
    elif exclusive.lower() == 'n':
        new = word
        break
    else:
        print("Invalid")
        pass

try:
    for block in transcript.fetch():
        if new.lower() in block['text'].lower():
            counter += 1
    
    print(f"'{word}' is said {counter} times in this video in the {lang} translation of this video.")
except:
    print('ERROR')


