// more claimable with more time
rule oneClaimMoreTime(address user) {
    require oneAssetOneReward(AToken, Reward);

    storage initial = lastStorage;

    env _e; env e_;
    require e_.block.timestamp >= _e.block.timestamp;

    address[] assets = getAssetsList();

    uint256 _claimable = getUserRewards(_e, assets, user, Reward) at initial;
    uint256 claimable_ = getUserRewards(e_, assets, user, Reward) at initial;

     assert claimable_ >= _claimable;
}

// more claimable with more balance
rule oneClaimMoreAssets(env e, address user) {
    require oneAssetOneReward(AToken, Reward);

    storage initial = lastStorage;

    uint256 amount;
    address[] assets = getAssetsList();

    uint256 _claimable = getUserRewards(e, assets, user, Reward) at initial;

    AToken.transfer(e, user, amount) at initial;
    uint256 claimable_ = getUserRewards(e, assets, user, Reward);

    assert claimable_ >= _claimable;
}

// less claimable with more totalSupply
rule oneClaimLessTotalSupply(env e, address user) {
    require oneAssetOneReward(AToken, Reward);

    storage initial = lastStorage;

    uint128 amount;
    address[] assets = getAssetsList();

    address other;
    require other != user;
    require other != 0;

    uint256 _claimable = getUserRewards(e, assets, user, Reward) at initial;

    AToken.mint(e, other, amount) at initial;
    uint256 claimable_ = getUserRewards(e, assets, user, Reward);

    assert claimable_ <= _claimable;
}


// rule claimable more if emission more

