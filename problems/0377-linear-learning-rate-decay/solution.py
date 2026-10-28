def linear_lr_decay(initial_lr: float, end_lr: float, num_steps: int) -> list:
    """
    Generate a linear learning rate decay schedule.
    
    Args:
        initial_lr: Starting learning rate
        end_lr: Final learning rate
        num_steps: Total number of training steps
    
    Returns:
        List of learning rates for each step
    """
    # Your code here
    if((num_steps-1)==0):
        return [initial_lr]
    p=(initial_lr-end_lr)/(num_steps-1)
    ans=[]
    for i in range(num_steps):
        ans.append(initial_lr)
        initial_lr-=p
    return ans