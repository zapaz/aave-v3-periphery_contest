rule rewardsTwoClaimAllRewardsAsExpected(env e, address[] assets, address user, address to) {
    require rewardsTwoAssetOne(assets[0], Reward, RewardB);
    require e.msg.sender == user;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _amountB = getUserRewards(e, assets, user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards@withrevert(e, assets, to);
    mathint amount0_ = amounts_[0];
    mathint amount1_ = amounts_[1];

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amount0_    == _amount
        && amount1_    == _amountB;
}

rule rewardsTwoClaimAllRewardsToSelfAsExpected(env e, address[] assets, address user) {
    require rewardsTwoAssetOne(assets[0], Reward, RewardB);
    require e.msg.sender == user;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _amountB = getUserRewards(e, assets, user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf@withrevert(e, assets);
    mathint amount0_ = amounts_[0];
    mathint amount1_ = amounts_[1];

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amount0_    == _amount
        && amount1_    == _amountB;
}

rule rewardsTwoClaimAllRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to) {
    require rewardsTwoAssetOne(assets[0], Reward, RewardB);
    require e.msg.sender == getClaimer(user);

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _amountB = getUserRewards(e, assets, user, RewardB);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf@withrevert(e, assets, user, to);
    mathint amount0_ = amounts_[0];
    mathint amount1_ = amounts_[1];

    assert !lastReverted =>
           rewards_[0] == Reward
        && rewards_[1] == RewardB
        && amount0_    == _amount
        && amount1_    == _amountB;
}

rule rewardsTwoClaimRewardsAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsTwoAssetOne(assets[0], Reward, RewardB);
    require e.msg.sender == user;

    mathint _amount_ = amount;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint amount_ = claimRewards(e, assets, amount, to, Reward);

    assert amount_ == min( _amount, _amount_ );
}

rule rewardsTwoClaimRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsTwoAssetOne(assets[0], Reward, RewardB);
    require e.msg.sender == getClaimer(user);

    mathint _amount_ = amount;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint amount_ = claimRewardsOnBehalf(e, assets, amount, user, to, Reward);

    assert amount_ == min( _amount, _amount_ );
}

rule rewardsTwoClaimRewardsToSelfAsExpected(env e, address[] assets, address user, uint256 amount) {
    require rewardsTwoAssetOne(assets[0], Reward, RewardB);
    require e.msg.sender == user;

    mathint _amount_ = amount;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint amount_ = claimRewardsToSelf(e, assets, amount, Reward);

    assert amount_ == min( _amount, _amount_ );
}

rule rewardsTwoClaimUserRewards(env e, address[] assets, address user){
    require rewardsTwoAssetOne(AToken, Reward, RewardB);

    mathint _claimable = getUserRewards(e, assets, user, Reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, assets, user);
    mathint claimable_ = amounts[0];

    assert claimable_ == _claimable;
}
