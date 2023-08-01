// more claimable with more time
rule rewardOneClaimMonotonicityTime() {
    require rewardsOneAssetOne(AToken, Reward);

    env _e; env e_; address user; address[] assets;

    uint256 _claimable = getUserRewards(_e, assets, user, Reward);
    uint256 claimable_ = getUserRewards(e_, assets, user, Reward);

     assert _e.block.timestamp <= e_.block.timestamp => _claimable <= claimable_;
}

// more claimable with more balance
rule rewardOneClaimMonotonicityAssets(env e, address user) {
    require rewardsOneAssetOne(AToken, Reward);

    uint256 amount;
    address[] assets;

    uint256 _claimable = getUserRewards(e, assets, user, Reward);
    AToken.transfer(e, user, amount);
    uint256 claimable_ = getUserRewards(e, assets, user, Reward);

    assert _claimable <= claimable_;
}

