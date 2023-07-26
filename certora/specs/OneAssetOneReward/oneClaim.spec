import "./oneClaimFunctions.spec";

// getUserAccruedRewards
// function getUserRewards(address[] calldata assets,address user,address reward) external view override returns (uint256) {

rule oneClaimAllRewardsAsExpected(env e, address user, address reward, address to) {
    require oneAssetOneReward(AToken, reward);
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, getAssetsList(), to);

    assert rewards_[0] == reward;
    assert amounts_[0] == _amount;
}

rule oneClaimAllRewardsToSelfAsExpected(env e, address user, address reward) {
    require oneAssetOneReward(AToken, reward);
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf(e, getAssetsList());

    assert rewards_[0] == reward;
    assert amounts_[0] == _amount;
}

rule oneClaimAllRewardsOnBehalfAsExpected(env e, address user, address reward, address to) {
    require oneAssetOneReward(AToken, reward);
    require e.msg.sender == getClaimer(user);

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);

    assert rewards_[0] == reward;
    assert amounts_[0] == _amount;
}

rule oneClaimRewardsAsExpected(env e, address user, address reward, address to) {
    require oneAssetOneReward(AToken, reward);
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    uint256 amount_ = claimRewards(e, getAssetsList(), _amount, to, reward);

    assert amount_ == _amount;
}

rule oneClaimRewardsOnBehalfAsExpected(env e, address user, address reward, address to) {
    require oneAssetOneReward(AToken, reward);
    require e.msg.sender == getClaimer(user);

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    uint256 amount_ = claimRewardsOnBehalf(e, getAssetsList(), _amount, user, to, reward);

    assert amount_ == _amount;
}

rule oneClaimRewardsToSelfAsExpected(env e, address user, address reward) {
    require oneAssetOneReward(AToken, reward);
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    uint256 amount_ = claimRewardsToSelf(e, getAssetsList(), _amount, reward);

    assert amount_ == _amount;
}


