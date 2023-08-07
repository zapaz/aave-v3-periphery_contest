// more claimable with more time
rule rewardOneClaimMonotonicityTime(address[] assets, address user, address reward) {
    require rewardsOneAssetsOne(assets[0], reward);

    // added requirement to reduce timeout
    require getAssetDecimals(assets[0]) == 6;

    env _e; env e_;
    mathint _claimable = getUserRewards(_e, assets, user, reward);
    mathint claimable_ = getUserRewards(e_, assets, user, reward);

    assert _e.block.timestamp <= e_.block.timestamp => _claimable <= claimable_;
}

// more claimable with more balance
rule rewardOneClaimMonotonicityAssets(env e, address user, uint256 amount) {
    require rewardsOneAssetsOne(AToken, Reward);
    address[] assets = getAssetsList();

    mathint _claimable = getUserRewards(e, assets, user, Reward);
    AToken.transfer(e, user, amount);
    mathint claimable_ = getUserRewards(e, assets, user, Reward);

    assert _claimable <= claimable_;
}

// more claimable with more emission
rule rewardOneClaimMonotonicityEmission(env e, address user, uint256 amount) {
    require rewardsOneAssetsOne(AToken, Reward);
    address[] assets = getAssetsList();
    address[] rewards = getRewardsByAsset(AToken);

    uint88[] _emissionsPerSeconds;
    uint88 _emissionsPerSecond = _emissionsPerSeconds[0];
    setEmissionPerSecond(e, AToken, rewards, _emissionsPerSeconds);

    mathint _claimable = getUserRewards(e, assets, user, Reward);

    uint88[] emissionsPerSeconds_;
    uint88 emissionsPerSecond_ = emissionsPerSeconds_[0];
    setEmissionPerSecond(e, AToken, rewards, emissionsPerSeconds_);

    mathint claimable_ = getUserRewards(e, assets, user, Reward);

    assert emissionsPerSecond_ >= _emissionsPerSecond => claimable_ >= _claimable;
}
