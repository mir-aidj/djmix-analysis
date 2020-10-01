> WARNING: Work In Progress!

# Summary
* We want to understand how DJs create [DJ Mixes](https://en.wikipedia.org/wiki/DJ_mix).
* We collected and analyze 1,557 real-world DJ mixes including 13,728 tracks
  from [*1001Tracklists*](https://www.1001tracklists.com/).
* First, to understand how DJs use audio effects,
  we perform mix-to-track subsequence alignment using dynamic time warping (DTW).
* Then, using the alignment results, we also extract cue points,
  which indicate when tracks start/end in mixes.
* Finally, we perform analyses with three hypotheses below and show that statistical evidence supports the hypotheses.
  1) DJs tend not to change tempo and/or key of tracks much to avoid distorting the original essence of the tracks.
  2) DJs make seamless transitions from one track to another considering the musical structures of tracks.
  3) DJs tend to select cue points at similar positions in a single track.


# 1. The [*1001Tracklists*](https://www.1001tracklists.com/) Dataset

## Statistics
|Summary statistic                            | All    | Matched |
| ------------------------------------------- | ------:| -------:|
|The number of mixes                          | 1,564  | 1,557   |
|The number of unique tracks                  | 15,068 | 13,728  |
|The number of played tracks                  | 26,776 | 24,202  |
|The number of transitions                    | 24,344 | 20,765  |
|Total length of mixes (in hours)             | 1,577  | 1,570   |
|Total length of unique tracks (in hours)     | 1,038  | 913     |
|Average length of mixes (in minutes)         | 60.5   | 60.5    |
|Average length of unique tracks (in minutes) | 4.1    | 4.0     |
|Average number of played tracks in a mix     | 17.1   | 15.5    |
|Average number of transitions in a mix       | 14.5   | 12.9    |

## Mix Genre Distribution
![mix genre counts](img/genre_mix.svg?raw=true)

## Track Genre Distribution
![track genre counts](img/genre_track.svg?raw=true)


# 2. Mix-To-Track Subsequence Alignment

![Mix-to-track subsequence alignment](img/fig_align.svg?raw=true)

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/645555018&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/popovmusic" title="Alexander Popov" target="_blank" style="color: #cccccc; text-decoration: none;">Alexander Popov</a> · <a href="https://soundcloud.com/popovmusic/interplay-radioshow-250-01-07-19" title="Interplay Radioshow 250 (01-07-19)" target="_blank" style="color: #cccccc; text-decoration: none;">Interplay Radioshow 250 (01-07-19)</a></div>

# 3. Cue Point Extraction

![Cue point extraction](img/fig_cue.svg?raw=true)

# 4. Musicological Analysis of DJ Mixes

