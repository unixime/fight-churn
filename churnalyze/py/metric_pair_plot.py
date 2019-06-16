import sys
import matplotlib.pyplot as plt
import matplotlib
import argparse

from churn_calc import ChurnCalculator

parser = argparse.ArgumentParser()
# Main run control arguments
parser.add_argument("--schema", type=str, help="The name of the schema", default='churnsim2')
parser.add_argument("--metrics", type=str,nargs=2, help="Two metrics to plot (if not plotting all pairs)")
# Additional options
parser.add_argument("--hide_ax", action="store_true", default=False,help="Hide axis labeling for publication of case studies")
parser.add_argument("--score", action="store_true", default=False,help="Plot Scores vs Scores")

parser.add_argument("--fontfamily", type=str, help="The font to use for plots", default='Brandon Grotesque')
parser.add_argument("--fontsize", type=int, help="The font to use for plots", default=14)



def plot_pair(cc,args,metric1,metric2):

    if not args.score:
        met1_data = cc.churn_data[metric1]
        met2_data = cc.churn_data[metric2]
        met1_label=metric1
        met2_label=metric2
        save_name = metric1 + '_vs_' + metric2
    else:
        scores,_ = cc.normalize_skewscale()
        met1_data = scores[metric1]
        met2_data = scores[metric2]
        met1_label='score('+metric1+')'
        met2_label='score('+metric2+')'
        save_name = metric1 + 'S_vs_' + metric2 + 'S'

    corr = met1_data.corr(met2_data)

    plt.figure(figsize=(6, 4))
    plt.scatter(met1_data,met2_data, marker='.')
    plt.xlabel(met1_label)
    plt.ylabel(met2_label)
    plt.tight_layout()
    plt.title('Correlation = %.2f' % corr)

    if args.hide_ax and not args.score:
        plt.gca().get_yaxis().set_ticklabels([])  # Hiding y axis labels on the count
        plt.gca().get_xaxis().set_ticklabels([])  # Hiding y axis labels on the count
        save_name += '_noax'

    plt.grid()
    plt.savefig(cc.save_path(save_name, ext='png'))
    plt.close()

if __name__ == "__main__":

    args, _ = parser.parse_known_args()

    font = {'family': args.fontfamily, 'size': args.fontsize}
    matplotlib.rc('font', **font)

    churn_calc = ChurnCalculator(args.schema)

    if args.metrics is not None:
        plot_pair(churn_calc, args, args.metrics[0],args.metrics[1])