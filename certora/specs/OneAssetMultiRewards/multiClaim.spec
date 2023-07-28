rule multiClaimAllRewardsAsExpected(env e, address user, address to) {
    require oneAssetMultiRewards(AToken, Reward, RewardB);
    require e.msg.sender == user;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _amountB = getUserRewards(e, getAssetsList(), user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, getAssetsList(), to);

    assert rewards_[0] == Reward;
    assert rewards_[1] == RewardB;
    assert amounts_[0] == _amount;
    assert amounts_[1] == _amountB;
}

// rule oneClaimAllRewardsToSelfAsExpected(env e, address user) {
//     require oneAssetOneReward(AToken, Reward);
//     require e.msg.sender == user;

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);

//     address[] rewards_; uint256[] amounts_;
//     rewards_, amounts_ = claimAllRewardsToSelf(e, getAssetsList());

//     assert rewards_[0] == Reward;
//     assert amounts_[0] == _amount;
// }

// rule oneClaimAllRewardsOnBehalfAsExpected(env e, address user, address to) {
//     require oneAssetOneReward(AToken, Reward);
//     require e.msg.sender == getClaimer(user);

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);

//     address[] rewards_; uint256[] amounts_;
//     rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);

//     assert rewards_[0] == Reward;
//     assert amounts_[0] == _amount;
// }

// rule oneClaimRewardsAsExpected(env e, address user, address to) {
//     require oneAssetOneReward(AToken, Reward);
//     require e.msg.sender == user;

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
//     uint256 amount;
//     uint256 amount_ = claimRewards(e, getAssetsList(), amount, to, Reward);

//     assert amount_ == min( _amount, amount );
// }

// rule oneClaimRewardsOnBehalfAsExpected(env e, address user, address to) {
//     require oneAssetOneReward(AToken, Reward);
//     require e.msg.sender == getClaimer(user);

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
//     uint256 amount;
//     uint256 amount_ = claimRewardsOnBehalf(e, getAssetsList(), amount, user, to, Reward);

//     assert amount_ == min( _amount, amount );
// }

// rule oneClaimRewardsToSelfAsExpected(env e, address user) {
//     require oneAssetOneReward(AToken, Reward);
//     require e.msg.sender == user;

//     uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
//     uint256 amount;
//     uint256 amount_ = claimRewardsToSelf(e, getAssetsList(), amount, Reward);

//     assert amount_ == min( _amount, amount );
// }

// rule oneClaimUserRewards(env e, address user){
//     require oneAssetOneReward(AToken, Reward);

//     uint256 _claimable = getUserRewards(e, getAssetsList(), user, Reward);

//     address[] rewards; uint256[] amounts;
//     rewards, amounts = getAllUserRewards(e, getAssetsList(), user);
//     uint256 claimable_ = amounts[0];

//     assert claimable_ == _claimable;
// }
