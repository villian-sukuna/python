from gtts import gTTS

text = "surprice mother fucker"
#text = "fuck you"
tt = gTTS(text=text,lang="en")

tt.save("gh.mp3")