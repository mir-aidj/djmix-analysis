> WARNING: Work In Progress!

# Summary
* We want to understand how DJs create [DJ Mixes](https://en.wikipedia.org/wiki/DJ_mix).
* We collected and analyze 1,557 real-world DJ mixes including 13,728 tracks
  from [*1001Tracklists*](https://www.1001tracklists.com/).
* First, to understand how DJs use audio effects,
  we perform mix-to-track subsequence alignment using
  [DTW](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_SubsequenceDTW.html).
* Then, using the alignment results, we also extract cue points,
  which indicate when tracks start/end in mixes.
* Finally, we perform analyses with three hypotheses below and show that statistical evidence supports the hypotheses.
    1. DJs tend not to change tempo and/or key of tracks much to avoid distorting the original essence of the tracks.
    2. DJs make seamless transitions from one track to another considering the musical structures of tracks.
    3. DJs tend to select cue points at similar positions in a single track.


# 1. The [*1001Tracklists*](https://www.1001tracklists.com/) Dataset

## Statistics

<p align="center">
    <table style="width:100%">
        <tr><th>Summary statistic                            </th><th>All    </th><th>Matched</th></tr>
        <tr><td>The number of mixes                          </td><td>1,564  </td><td>1,557  </td></tr>
        <tr><td>The number of unique tracks                  </td><td>15,068 </td><td>13,728 </td></tr>
        <tr><td>The number of played tracks                  </td><td>26,776 </td><td>24,202 </td></tr>
        <tr><td>The number of transitions                    </td><td>24,344 </td><td>20,765 </td></tr>
        <tr><td>Total length of mixes (in hours)             </td><td>1,577  </td><td>1,570  </td></tr>
        <tr><td>Total length of unique tracks (in hours)     </td><td>1,038  </td><td>913    </td></tr>
        <tr><td>Average length of mixes (in minutes)         </td><td>60.5   </td><td>60.5   </td></tr>
        <tr><td>Average length of unique tracks (in minutes) </td><td>4.1    </td><td>4.0    </td></tr>
        <tr><td>Average number of played tracks in a mix     </td><td>17.1   </td><td>15.5   </td></tr>
        <tr><td>Average number of transitions in a mix       </td><td>14.5   </td><td>12.9   </td></tr>
    </table>
</p>


## Mix Genre Distribution
![mix genre counts](img/genre_mix.svg?raw=true)

## Track Genre Distribution
![track genre counts](img/genre_track.svg?raw=true)


# 2. Mix-To-Track Subsequence Alignment

## [Well aligned example](https://1001.tl/14jltnct)
![Well aligned example](img/fig_align_good.svg?raw=true)
<iframe width="100%" height="140" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/645555018&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/popovmusic" title="Alexander Popov" target="_blank" style="color: #cccccc; text-decoration: none;">Alexander Popov</a> · <a href="https://soundcloud.com/popovmusic/interplay-radioshow-250-01-07-19" title="Interplay Radioshow 250 (01-07-19)" target="_blank" style="color: #cccccc; text-decoration: none;">Interplay Radioshow 250 (01-07-19)</a></div>

## [Badly aligned example](https://1001.tl/15fulzc1)
![Badly aligned example](img/fig_align_bad.svg?raw=true)
<iframe width="100%" height="140" src="https://www.mixcloud.com/widget/iframe/?hide_cover=1&feed=%2FAirFM%2Fjustice-live-glastonbury-festival-2017-25-june-2017%2F" frameborder="0" ></iframe>

## [Key changed example](https://1001.tl/bcx2z0t)
![Key changed example](img/fig_align_keychanged.svg?raw=true)
<iframe width="100%" height="140" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/325077089&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/maxvangeli" title="Max Vangeli" target="_blank" style="color: #cccccc; text-decoration: none;">Max Vangeli</a> · <a href="https://soundcloud.com/maxvangeli/max-vangeli-presents-noface-radio-episode-046" title="Max Vangeli Presents: NoFace Radio - Episode 046" target="_blank" style="color: #cccccc; text-decoration: none;">Max Vangeli Presents: NoFace Radio - Episode 046</a></div>


# 3. Cue Point Extraction

![Cue point extraction](img/fig_cue.svg?raw=true)

# 4. Musicological Analysis of DJ Mixes

# You can do it too!
You can do it too!

# Preview of our next move

