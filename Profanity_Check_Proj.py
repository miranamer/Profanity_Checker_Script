from youtube_transcript_api import YouTubeTranscriptApi

def isProfane(video_id): # Returns num of swears and timestamps
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    profane_count = 0
    profane_timestamps = []

    for i in transcript:
        if '[\xa0__\xa0]' in i['text']: # '[\xa0__\xa0]' => refers to a swear
            profane_count += 1
            profane_timestamps.append([i['start'], '=>', (i['start']+i['duration'])])

    return (f"Swears: {profane_count} Timestamps: {profane_timestamps}") if profane_count > 0 else "No Swears"
