> WARNING: Work In Progress!

# Summary
* We want to understand how DJs create [DJ Mixes](https://en.wikipedia.org/wiki/DJ_mix).
* Therefore, we collected and analyze 1,557 real-world DJ mixes including 13,728 tracks
  from [*1001Tracklists*](https://www.1001tracklists.com/).
* To understand how DJs use audio effects,
  we perform mix-to-track subsequence alignment using
  [DTW](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_SubsequenceDTW.html).
* Then, using the alignment results, we also extract cue points,
  which indicate when individual tracks start/end in mixes.
* Finally, we perform analyses with three hypotheses below and show that statistical evidence supports the hypotheses:
    1. DJs tend not to change tempo and/or key of tracks much to avoid distorting the original essence of the tracks.
    2. DJs make seamless transitions from one track to another considering the musical structures of tracks.
    3. DJs tend to select cue points at similar positions in a single track.


# The [*1001Tracklists*](https://www.1001tracklists.com/) Dataset

We obtained a collection of DJ mix metadata via direct personal communication with 1001Tracklists.
Each entry of mixes contains a list of track, boundary timestamps and genre.
It also contains web links to the audio files of the mixes and tracks.
We downloaded the audio files separately from the linked media service websites on our own.

## Summary Statistics
The table below summarizes statistics of the dataset.
The original size of the dataset is denoted as ‘All’ and the size after
filtering as ‘Matched’.
Note that the number of played tracks is greater than the number of unique tracks
as a track can be played in multiple mixes.

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

## Genre Distribution
The dataset includes a variety of genres but mostly focuses on House and Trance music as shown below.

### Mix Genre Distribution
![mix genre counts](img/fig_genre_mix.svg?raw=true)

### Track Genre Distribution
![track genre counts](img/fig_genre_track.svg?raw=true)


# Mix-To-Track Subsequence Alignment
The objective of mix-to-track subsequence alignment is to
find an optimal alignment path between a subsequence of a
mix and a track used in the mix.
We compute the alignment by applying
[subsequence DTW](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C7/C7S2_SubsequenceDTW.html)
to beat synchronous features such as MFCC and chroma features.

Three examples below visualize the DTW-based mix-to-track subsequence alignment between a mix
and the original tracks played in that mix.
The colored solid lines show the warping paths of the alignment.
Since we use beat synchronous representations for them, the warping paths become diagonal
with a slope of one if a mix and a track are successfully aligned.

You can listen and see individual tracks used in the mixes if you go to the tracklist links.

## Well Aligned Example [[Tracklist Link]](https://1001.tl/14jltnct)
The example below shows an successfully aligned example for the most of tracks and
features where all warping paths have straight diagonal paths.
<iframe width="100%" height="140" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/645555018&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/popovmusic" title="Alexander Popov" target="_blank" style="color: #cccccc; text-decoration: none;">Alexander Popov</a> · <a href="https://soundcloud.com/popovmusic/interplay-radioshow-250-01-07-19" title="Interplay Radioshow 250 (01-07-19)" target="_blank" style="color: #cccccc; text-decoration: none;">Interplay Radioshow 250 (01-07-19)</a></div>
![Well aligned example](img/fig_align_good.svg?raw=true)


## Badly Aligned Example [[Tracklist Link]](https://1001.tl/15fulzc1)
This example is failing because sounds from crowds are also 
recorded in the mix. You can hear crowds sreaming if you listen to the mix below.
<iframe width="100%" height="120" src="https://www.mixcloud.com/widget/iframe/?hide_cover=1&feed=%2FAirFM%2Fjustice-live-glastonbury-festival-2017-25-june-2017%2F" frameborder="0" ></iframe>
![Badly aligned example](img/fig_align_bad.svg?raw=true)


## Key Changed Example [[Tracklist Link]](https://1001.tl/bcx2z0t)
Since the proposed alignment method is key transposition invariant,
the method works even though a DJ changes the key of tracks.
This is an example which the key-invariant method distinctively works better than 
others as the DJ frequently uses key transposition on the mix.
You can hear that some tracks are key changed
if you go to the tracklist link and listen to the mix and the individual tracks!
<iframe width="100%" height="140" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/325077089&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/maxvangeli" title="Max Vangeli" target="_blank" style="color: #cccccc; text-decoration: none;">Max Vangeli</a> · <a href="https://soundcloud.com/maxvangeli/max-vangeli-presents-noface-radio-episode-046" title="Max Vangeli Presents: NoFace Radio - Episode 046" target="_blank" style="color: #cccccc; text-decoration: none;">Max Vangeli Presents: NoFace Radio - Episode 046</a></div>
![Key changed example](img/fig_align_keychanged.svg?raw=true)



# Cue Point Extraction
If you look closer to the warping paths from the subsequence DTW,
you can also extract cue points which indicate where tracks start/end in mixes.
The figure below is a zoomed-in view of a visualization of mix-to-track subsequence alignment explaining the three types of
extracted cue points.
The two alignment paths drift from the diagonal lines in the transition region
(between 2310 and 2324 in mix beat) because the two tracks cross-fades.
<p align="center">
    <img src="img/fig_cue.svg?raw=true">
</p>

# Musicological Analysis of DJ Mixes
We hypothesize that DJs share common practices in the creative process.
Here, we validate the hypotheses mentioned in the summary above using the 
results from the mix-to-track subsequence alignment and the cue point extraction.

## Tempo Adjustment Analysis
The figure below shows a histogram of percentage differences of tempo 
between the original track and the audio segment in the mix.
86.1% of the tempo are adjusted less than 5%, 
94.5% are less than 10%, and 98.6% are less than 20%.
<p align="center">
    <img src="img/fig_diff_bpm.svg?raw=true">
</p>

## Key Change Analysis
The figure below shows a histogram of key change between the original track 
and the corresponding audio segment in the mix.
Only 2.5% among the total 24,202 tracks are transposed and, among those transposed tracks, 
94.3% of them are only one semitone transposed. 
This result indicates that DJs generally do not perform key transposition
much and leave the “master tempo” function on DJ systems turned on in
most cases.
<p align="center">
    <img src="img/fig_diff_key.svg?raw=true">
</p>

## Transition Length Analysis
The figure below shows a histogram of
transition lengths in the number of beats. We annotated
the dotted lines every 32 beat which is often considered as
a phrase in the context of dance music. The histogram has
peaks at every phrases. This indicates that DJs consider the
repetitive structures in the dominant genres of music when
they make transitions or set cue points.
<p align="center">
    <img src="img/fig_cue_translength.svg?raw=true">
</p>

## Cue Point Agreement Among DJs
We collected all extracted cue points for each track and computed the
statistics of deviations in cue-in points and cue-out points
among DJs. From the results, 23.6% of the total cue point pairs have zero deviation.
40.4% of them were within one measure (4 beats), 73.6% were within 8 measures and 
86.2% were within 16 measures. This indicates that there are some rules that DJs
share in deciding the cue points. 
<p align="center">
    <img src="img/fig_cue_diff.svg?raw=true">
</p>

# You can do it too! [[GitHub Repo Link]](https://github.com/mir-aidj/djmix-analysis)
We published the code for mix-to-track subsequence alignment, cue point extraction,
DTW visualization and the tempo analysis.
The code uses the cool mix below by Palms Trax as an input data.
 
<p align="center">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/cPo-qzbGLqE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

And you will get the visualization below after running the code!

![Palms Trax DTW Viz](img/palmstrax_dtwviz.svg?raw=true)


# Preview of our next move

