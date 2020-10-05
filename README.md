# A Computational Analysis of Real-World DJ Mixes using Mix-To-Track Subsequence Alignment
> This repository contains the code for "A Computational Analysis of Real-World DJ Mixes using Mix-To-Track Subsequence Alignment"
> *Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR), 2020.*
> Taejun Kim, Minsuk Choi, Evan Sacks, Yi-Hsuan Yang, and Juhan Nam

This repository contains the code for:
1) mix-to-track subsequence alignment
2) mix segmentation
3) subsequence DTW visualization
4) BPM change analysis

We are going to use the awesome mix below by Palms Trax since it is the author's recent favorite mix.
`data/meta/tracklist.csv` contains the tracklist of the mix which is manually collected by the author from YouTube comments.

[![Palms Trax | Boiler Room: Streaming From Isolation | #11](https://img.youtube.com/vi/cPo-qzbGLqE/0.jpg)](https://www.youtube.com/watch?v=cPo-qzbGLqE)

The figure below is the visualization of the subsequence mix-to-track alignment for Palms Trax's mix.

![Subsequence DTW Visualization](img/dtwviz.png?raw=true "Subsequence DTW Visualization")

## Installing python packages
> NOTE: This repo is written and tested on Python `3.8.5`.

You can install required Python packages using the code below: 
```sh
pip install -r requirements.txt
pip install madmom==0.16.1  # madmom should be installed after installing cython
```


## Downloading audio files from YouTube
```sh
python script/download.py
```

## Running scripts
The scripts should be run in order below:
1. `python script/feature_extraction.py` extracts features and saves them under `cache/` using disk-caching of [joblib](https://joblib.readthedocs.io/).
2. `python script/alignment.py` performs mix-to-track subsequence DTW and saves the alignment results.
3. `python script/segmentation.py` evaluates mix segmentation performances and saves the segmentation results.
4. `python script/dtw_visualization.py` (optional) saves DTW visualizations for all mixes under `data/dtwviz/`, but the repo already contains the visualizations.



## Analysis notes
> NOTE: The scripts above should be run before since the analysis notes require the results of the scripts.
1. `note/mix_segmentation.ipynb` analyzes the segmentation results.
2. `note/bpm_change.ipynb` analyzes the tempo adjustment.
