invariant timestamp(env e, address asset, address reward)
    getLastUpdateTimestamp(asset, reward) <= e.block.timestamp
    { preserved with (env ep) { require  ep.block.timestamp == e.block.timestamp; } }

invariant rewardEnabled(address reward)
    isRewardEnabled(reward) <=> inArray(getRewardsList(), reward);

invariant rewardsLength(address asset)
    getRewardsByAssetLength(asset) <= getRewardsListLength()
    filtered { f -> !harnessFunction(f) }
    { preserved {
        require (forall address reward . isRewardEnabled(reward) <=> inArray( getRewardsList(), reward) );
    } }


