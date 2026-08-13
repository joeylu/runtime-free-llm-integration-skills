# MiniMax Music Transport

```json
{
  "model": "music-3.0",
  "prompt": "...",
  "lyrics": "...",
  "lyrics_optimizer": false,
  "is_instrumental": false,
  "stream": false,
  "output_format": "url",
  "audio_setting": {"sample_rate":44100,"bitrate":256000,"format":"mp3"}
}
```

For instrumental output, `prompt` is required and lyrics are not. For ordinary vocal generation, lyrics are required unless `lyrics_optimizer=true`. Streaming requires `output_format=hex`; URL output is non-stream only and expires after 24 hours. Do not invent a duration field.
