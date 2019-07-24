#### 1. First-Visit

    ![first-visit](./image/mc-first-visit.png)

    ```python
    # first-visit
    pi = init_pi()
    returns = defaultdict(list)
    while step < 1e6:
        episode = generate_epsiode(pi)
        G = np.zeros(|S|)  # 每个 state 只保留一个 G
        for (s, r) in reversed(epsiode):
            G[s] = gamma * G[s] + r
        for s in STATES:
            returns[s].append(G[s])
    V = {s: np.mean(r) for s, r in returns.items()}

    # every-visit
    G = 0
    for (s, r) in reversed(epsiode):
        G = gamma * G + r
        returns[s].append(G)
    ```



#### 2. Exploring Starts

    ![es](./image/mc-es.png)

    ```python
    # exploring starts，即每次从固定的 (s, a) 开始采样，从之前的计算 V 变成计算 Q
    pi = init_pi()
    Q = np.zeros([ns, na])
    returns = defaultdict(list)
    while step < 1e6:
        episode = generate_epsiode(pi, s0, a0)
        G = np.zeros([S, A])  # 每个 state 只保留一个 G
        for (s, a, r) in reversed(epsiode):
            G[s, a] = gamma * G[s, a] + r
        for s in STATES:
            for a in ACTIONS:
            	returns[s, a].append(G[s, a])
    Q = {[s,a]: np.mean(r) for (s, a, r) in returns.items()}
    pi = argmax_a(Q)
    ```

