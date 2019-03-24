import wikipedia

import re
from sentence_splitter import  split_text_into_sentences

term = 'Steve Jobs'

summary = wikipedia.summary(term,sentences=7)


summary = re.sub(r"\([^)]*\)", "",summary)






result = split_text_into_sentences(
        text=summary,
        language="en",
    )


subtitles_template = """
1
00:00:00,000 --> 00:00:10,000
{0}

2
00:00:10,000 --> 00:00:20,000
{1}

3
00:00:20,000 --> 00:00:30,000
{2}

4
00:00:30,000 --> 00:00:40,000
{3}

5
00:00:40,000 --> 00:00:50,000
{4}

6
00:00:50,000 --> 00:01:00,000
{5}

7
00:01:00,000 --> 00:01:10,000
{6}"""

subtitles_template = subtitles_template.format(result[0],
            result[1], result[2], result[3],
            result[4], result[5], result[6])





print(result)
print('\n')
print(subtitles_template)
