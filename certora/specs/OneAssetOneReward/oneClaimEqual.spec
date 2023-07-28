rule oneClaimEqual(env e, address user, address to) {
    require oneAssetOneReward(AToken, Reward);

    uint256 totalSupply = AToken.totalSupply(e);
    uint256 balance = AToken.balanceOf(e, user);
    require balance > 0;
    require totalSupply >= balance;

    handleAction(e, user, totalSupply, balance);

    uint256 index;
    uint256 emissionPerSecond;
    uint256 lastUpdateTimestamp;
    uint256 distributionEnd;
    index, emissionPerSecond, lastUpdateTimestamp, distributionEnd =  getRewardsData(e, AToken, Reward);

    uint256 _userAccrued = getUserAccruedRewards(user, Reward);
    uint256 _userIndex = getUserAssetIndex(user, AToken, Reward);

    require index >= _userIndex;
    require e.block.timestamp < distributionEnd;
    require e.block.timestamp > lastUpdateTimestamp;

    mathint deltaTime = e.block.timestamp - lastUpdateTimestamp;
    mathint deltaIndex = ( emissionPerSecond * deltaTime ) / totalSupply;
    mathint _claimable = _userAccrued + balance * deltaIndex;

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);
    mathint claimable_ = amounts_[0];

    uint256 userAccrued_ = getUserAccruedRewards(user, Reward);
    uint256 userIndex_ = getUserAssetIndex(user, AToken, Reward);

    assert _claimable == claimable_;
}

rule oneClaimEqualUserRewards(env e, address user){
    require oneAssetOneReward(AToken, Reward);

    uint256 _claimable = getUserRewards(e, getAssetsList(), user, Reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, getAssetsList(), user);
    uint256 claimable_ = amounts[0];

    assert claimable_ == _claimable;
}
