def early_stopping(val_losses: list[float], patience: int = 5, min_delta: float = 0.0) -> list[bool]:
    counter = 0
    best_loss = val_losses[0]
    ans = []

    for i in range(len(val_losses)):
        if i == 0:
            ans.append(False)
        elif val_losses[i] < best_loss - min_delta:
            best_loss = val_losses[i]
            counter = 0
            ans.append(False)
        else:
            counter += 1
            if counter >= patience:
                ans.append(True)
                counter = 0
            else:
                ans.append(False)

    return ans