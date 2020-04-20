import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

from stable_baselines import results_plotter
from stable_baselines.results_plotter import load_results, ts2xy



def moving_average(values, window):
    """
    Smooth values by doing a moving average
    :param values: (numpy array)
    :param window: (int)
    :return: (numpy array)
    """
    weights = np.repeat(1.0, window) / window
    return np.convolve(values, weights, 'valid')


def plot_results(log_folder, type_str):
    """
    plot the results

    :param log_folder: (str) the save location of the results to plot
    :param type: (str) either 'timesteps', 'episodes' or 'walltime_hrs'
    """

    x, y = ts2xy(load_results(log_folder), type_str)
    # x, y = ts2xy(load_results(log_folder), 'episodes')
    # x, y = ts2xy(load_results(log_folder), 'walltime_hrs')

    y = moving_average(y, window=1)
    # Truncate x
    x = x[len(x) - len(y):]

    plt.figure()
    plt.plot(x, y)
    plt.xlabel(type_str)
    plt.ylabel('Rewards')



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', help='Log folder', type=str, default='trained_agents')
    args = parser.parse_args()

    log_dir = args.folder


    timesteps = 1e10
    # log_dir = "logs/sac/ReacherBulletEnv-v0_1/"
    # log_dir = "logs/ppo2/ReacherBulletEnv-v0_5/"

    # log_dir = "logs/a2c/ReacherBulletEnv-v0_1/"
    # log_dir = "logs/acktr/ReacherBulletEnv-v0_1/"
    # log_dir = "logs/a2c/Pendulum-v0_18/"

    W = load_results(log_dir)

    print("results: ", W)

    # # save walltime to stats.csv
    # df = pd.read_csv(log_dir+'stats.csv')  
    # df["Train walltime (s)"] = W["t"].max()
    # df.to_csv(log_dir+"stats.csv", index=False)
    # print(df)

    # ## plot evaluations

    # X = np.load(log_dir+'evaluations.npz')
    # print(X.files)

    # print(X['timesteps'].shape)
    # print(X['results'].shape)
    # print(X['ep_lengths'].shape)

    # T = X['timesteps']
    # R = X['results']
    # E = X['ep_lengths']

    # av_reward = []
    # for i in range(len(R)):
    #     av_reward.append(np.mean(R[i, :]))

    # plt.plot(T, av_reward)
    # plt.xlabel('Number of Timesteps')
    # plt.ylabel('Rewards')
    # plt.savefig(log_dir+"evaluations.png")
    # # plt.show()


    # plot all training rewards

    results_plotter.plot_results([log_dir], timesteps, results_plotter.X_TIMESTEPS, "")
    plt.savefig(log_dir+"reward_vs_timesteps.png")
    # plt.show()

    results_plotter.plot_results([log_dir], timesteps, results_plotter.X_EPISODES, "")
    plt.savefig(log_dir+"reward_vs_episodes.png")
    # plt.show()

    results_plotter.plot_results([log_dir], timesteps, results_plotter.X_WALLTIME, "")
    plt.savefig(log_dir+"reward_vs_walltime.png")
    # plt.show()




    #### smoothed training rewards
        
    plot_results(log_dir, 'timesteps')
    plt.savefig(log_dir+"reward_vs_timesteps_smoothed.png")
    # plt.show()

    plot_results(log_dir, 'episodes')
    plt.savefig(log_dir+"reward_vs_episodes_smoothed.png")
    # plt.show()

    plot_results(log_dir, 'walltime_hrs')
    plt.savefig(log_dir+"reward_vs_walltime_smoothed.png")
    # plt.show()

    print(log_dir+"reward_vs_walltime_smoothed.png")
