import numpy as np

def track_rl_experiment(episode_rewards: list, episode_lengths: list, window_size: int = 10) -> dict:
    """
    Summarize metrics from an RL training run.
    
    Args:
        episode_rewards: Total reward per episode
        episode_lengths: Number of timesteps per episode
        window_size: Window size for moving average and improvement calculation
    
    Returns:
        Dictionary with training summary statistics
    """
    te=len(episode_rewards)
    mr=np.mean(episode_rewards)
    sr=np.sqrt(np.mean((episode_rewards-mr)**2))
    mxr=np.max(episode_rewards)
    mnr=np.min(episode_rewards)
    be = 0
    for i in range(te):
        if episode_rewards[i] > episode_rewards[be]:
            be = i 
    ml=np.mean(episode_lengths)
    fma=np.mean(episode_rewards[-window_size:])
    ri=np.mean(episode_rewards[-window_size:])-np.mean(episode_rewards[0:window_size])

    return {
    'total_episodes': te,
    'mean_reward': round(float(mr), 4),
    'std_reward': round(float(sr), 4),
    'max_reward': round(float(mxr), 4),
    'min_reward': round(float(mnr), 4),
    'best_episode': be,
    'mean_length': round(float(ml), 4),
    'final_moving_avg': round(float(fma), 4),
    'reward_improvement': round(float(ri), 4)
}



