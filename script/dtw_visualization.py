import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from multiprocessing import Pool
from tqdm import tqdm

MATCH_RATE_THRES = 0.4
CASES = ['mfcc', 'chroma', 'chroma-keyinv', 'chroma+mfcc', 'chroma+mfcc-keyinv']
COLORS = ['C0', 'C1', 'C2', 'C3', 'C4']

df_trans = pd.read_pickle('data/mix_segmentation.pkl')


def main():
  os.makedirs('data/dtwviz', exist_ok=True)
  with Pool() as pool:
    mix_ids = df_trans.mix_id.unique()
    iterator = pool.imap(worker, mix_ids)
    for _ in tqdm(iterator, total=len(mix_ids)):
      pass


def worker(mix_id):
  df_mix = df_trans[df_trans.mix_id == mix_id].reset_index(drop=True)
  xmax = max(df_mix.wp_prev.apply(lambda wp: wp[:, 1].max()).max(),
             df_mix.wp_next.apply(lambda wp: wp[:, 1].max()).max())
  ymax = max(df_mix.wp_prev.apply(lambda wp: wp[:, 0].max()).max(),
             df_mix.wp_next.apply(lambda wp: wp[:, 0].max()).max())
  plt.figure(figsize=(12, 4))
  for i_case, case in enumerate(CASES):
    color = COLORS[i_case]
    df_case = df_mix[df_mix['case'] == case].reset_index(drop=True)
    for i_trans, trans in df_case.iterrows():
      wp_prev, wp_next = trans.wp_prev, trans.wp_next

      textoffset = 5
      # Plot the previous warping path in the transition.
      plt.plot(wp_prev[:, 1], wp_prev[:, 0], color=color)
      plt.text(wp_prev[0, 1] + textoffset, wp_prev[0, 0] + textoffset, str(i_trans), color='white',
               bbox={'facecolor': color, 'boxstyle': 'square, pad=0.1', 'linewidth': 0},
               verticalalignment='bottom', horizontalalignment='left')
      # Plot the next warping path in the transition if it is the last loop.
      if i_trans == len(df_case) - 1:
        plt.plot(wp_next[:, 1], wp_next[:, 0], color=color)
        plt.text(wp_next[0, 1] + textoffset, wp_next[0, 0] + textoffset, str(i_trans + 1), color='white',
                 bbox={'facecolor': color, 'boxstyle': 'square, pad=0.1', 'linewidth': 0},
                 verticalalignment='bottom', horizontalalignment='left')

      # Plot the boundary vertical lines.
      timestamp_beat_next = trans['timestamp_beat_next']
      plt.axvline(timestamp_beat_next, color='black', linestyle='--', linewidth=1)
      plt.text(timestamp_beat_next + textoffset, ymax * 1.10 + textoffset, str(i_trans), color='white',
               bbox={'facecolor': 'black', 'boxstyle': 'square, pad=0.1', 'linewidth': 0},
               verticalalignment='bottom', horizontalalignment='left')

      # Draw the bar at the bottom if the previous track is correctly matched.
      if trans.match_rate_prev > MATCH_RATE_THRES:
        box_height = 0.04 * ymax
        true_start_beat = trans.timestamp_beat_prev
        true_end_beat = trans.timestamp_beat_next
        plt.gca().add_patch(mpatches.Rectangle(xy=(true_start_beat, box_height * i_case),
                                               width=true_end_beat - true_start_beat, height=box_height,
                                               linewidth=0, facecolor=color, alpha=0.5))
      # Draw the bar at the bottom if the next track is correctly matched and if it is the last loop.
      if (i_trans == len(df_case) - 1) and (trans.match_rate_next > MATCH_RATE_THRES):
        box_height = 0.04 * ymax
        true_start_beat = df_case.iloc[i_trans]['timestamp_beat_next']
        true_end_beat = xmax + 1000  # just draw until the end of the figure
        plt.gca().add_patch(mpatches.Rectangle(xy=(true_start_beat, box_height * i_case),
                                               width=true_end_beat - true_start_beat, height=box_height,
                                               linewidth=0, facecolor=color, alpha=0.5))

  plt.xlim(0, xmax * 1.03)
  plt.ylim(0, ymax * 1.17)

  plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=3, mode='expand', borderaxespad=0.,
             handles=[mpatches.Patch(color='black', label='Ground Truth')] +
                     [mpatches.Patch(color=COLORS[i], label=case) for i, case in enumerate(CASES)])

  plt.ylabel('Track beat frame')
  plt.xlabel('Mix beat frame')
  plt.tight_layout()
  plt.savefig(f'data/dtwviz/{mix_id}.pdf')
  plt.close()


if __name__ == '__main__':
  main()
