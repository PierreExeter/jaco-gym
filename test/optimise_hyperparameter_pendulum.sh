#!/bin/bash

python train.py --algo a2c --env Pendulum-v0 -n 1000000 --log-folder logs/a2c/Pendulum-v0_1_opti_1M_100trials_noPruning/ -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner none  &> submission_log/log_a2c_opti_1M_100trials.run
# python train.py --algo a2c --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo acktr --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo ppo2 --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo ddpg --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo sac --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo td3 --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo ppo2 --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median
# python train.py --algo trpo --env Pendulum-v0 -n 100000 -optimize --n-trials 100 --n-jobs -1 --sampler tpe --pruner median

