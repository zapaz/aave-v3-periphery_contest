rule multiClaimAllRewardsAsExpected(env e, address user, address to) {
    require oneAssetMultiRewards(AToken, Reward, RewardB);
    require e.msg.sender == user;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _amountB = getUserRewards(e, getAssetsList(), user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards@withrevert(e, getAssetsList(), to);

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amounts_[0] == _amountB
        && amounts_[1] == _amountB;
}

rule multiClaimAllRewardsToSelfAsExpected(env e, address user) {
    require oneAssetMultiRewards(AToken, Reward, RewardB);
    require e.msg.sender == user;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _amountB = getUserRewards(e, getAssetsList(), user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf@withrevert(e, getAssetsList());

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amounts_[0] == _amountB
        && amounts_[1] == _amountB;
}

rule multiClaimAllRewardsOnBehalfAsExpected(env e, address user, address to) {
    require oneAssetMultiRewards(AToken, Reward, RewardB);
    require e.msg.sender == getClaimer(user);

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _amountB = getUserRewards(e, getAssetsList(), user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf@withrevert(e, getAssetsList(), user, to);

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amounts_[0] == _amountB
        && amounts_[1] == _amountB;
}

// rule multiClaimRewardsAsExpected(env e, address user, address to) {
//     require oneAssetMultiRewards(AToken, Reward, RewardB);
//     require e.msg.sender == user;

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
//     uint256 amount;
//     uint256 amount_ = claimRewards(e, getAssetsList(), amount, to, Reward);

//     assert amount_ == min( _amount, amount );
// }

// rule multiClaimRewardsOnBehalfAsExpected(env e, address user, address to) {
//     require oneAssetMultiRewards(AToken, Reward, RewardB);
//     require e.msg.sender == getClaimer(user);

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
//     uint256 amount;
//     uint256 amount_ = claimRewardsOnBehalf(e, getAssetsList(), amount, user, to, Reward);

//     assert amount_ == min( _amount, amount );
// }

// rule multiClaimRewardsToSelfAsExpected(env e, address user) {
//     require oneAssetMultiRewards(AToken, Reward, RewardB);
//     require e.msg.sender == user;

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
//     uint256 amount;
//     uint256 amount_ = claimRewardsToSelf(e, getAssetsList(), amount, Reward);

//     assert amount_ == min( _amount, amount );
// }

// rule multiClaimUserRewards(env e, address user){
//     require oneAssetMultiRewards(AToken, Reward, RewardB);

//     uint256 _claimable = getUserRewards(e, getAssetsList(), user, Reward);

//     address[] rewards; uint256[] amounts;
//     rewards, amounts = getAllUserRewards(e, getAssetsList(), user);
//     uint256 claimable_ = amounts[0];

//     assert claimable_ == _claimable;
// }
