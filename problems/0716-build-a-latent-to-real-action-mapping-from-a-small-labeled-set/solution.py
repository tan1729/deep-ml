# 1. Pehle problem samjho
# Maan lo ek AI policy abstract actions generate karti hai, but robot ko actual control commands chahiye.
# - Latent action: AI ka abstract representation.
# - Real action: Actual control command jo robot ko execute karna hai.
# Humein kuch examples diye hain jahan latent action aur uska corresponding real action already known hai. In examples se humein ek mapping learn karni hai.
# 2. Given input ko samjho
# Example mein:
# - latents_labeled = [[1,0],[0,1]]
# - reals_labeled = [[2,0],[0,3]]
# - latents_query = [[1,1]]
# Pehli do arrays training data hain.
# Training examples
# Latent input
# [1, 0]

# Real output
# [2, 0]


# Latent input
# [0, 1]

# Real output
# [0, 3]


# Humein in known input-output pairs se mapping learn karni hai.

# 3. Linear map kya hota hai?
# Hum assume karte hain ki latent vector ko ek matrix \(W\) se multiply karke real action mil sakta hai:
# \[
# \text{Real action}=\text{Latent action}\times W
# \]

# Yahan:
# - Latent dimension \(d_l=2\)
# - Real action dimension \(d_r=2\)
# - Isliye mapping matrix \(W\) ka shape \(2\times2\) hoga.
# Given examples se humein pata chalta hai ki mapping hai:
# \[
# W=
# \begin{bmatrix}
# 2 & 0\\
# 0 & 3
# \end{bmatrix}
# \]

# Matlab first latent component ka effect first real component par 2 times hai, aur second latent component ka effect second real component par 3 times hai.
# 4. Ab query par prediction karo
# Query input hai:
# \[
# [1,1]
# \]

# Isko learned mapping se multiply karenge:
# \[
# [1,1]
# \begin{bmatrix}
# 2&0\\
# 0&3
# \end{bmatrix}
# =[2,3]
# \]

# Isliye output hoga [[2.0, 3.0]].
# 5. Least squares kyun use hota hai?
# Real problems mein labeled examples hamesha perfectly match nahi karte. Ho sakta hai data noisy ho ya examples zyada hon.

# Least squares aisi matrix \(W\) find karta hai jisse predicted real actions aur actual real actions ke beech squared errors ka sum minimum ho.

# Is question mein tumhe teen kaam karne hain:
# 1. Labeled latent-real pairs se best linear mapping learn karna.
# 2. Us mapping ko latents_query par apply karna.
# 3. Predictions ko nested Python list mein return karna.
# Crux: Training data se mapping learn karo, phir unseen latent inputs ko real actions mein convert karo.


import numpy as np

def map_latent_to_real(latents_labeled: np.ndarray, reals_labeled: np.ndarray, latents_query: np.ndarray) -> list:
    W = np.linalg.lstsq(latents_labeled, reals_labeled, rcond=None)[0]
    predictions = latents_query.dot(W)
    return predictions.tolist()
