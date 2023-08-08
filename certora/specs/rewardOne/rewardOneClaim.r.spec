/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimRewardsToSelf equals getUserRewards
// - balance of reward increased by min of expected rewards and amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimRewardsToSelfAsExpected(env e, address[] assets, address user, uint256 amount) {
    require rewardsOneAssetsOne(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    mathint _amount_ = amount;
    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, user);

    mathint amount_ = claimRewardsToSelf(e, assets, amount, Reward);

    mathint balance_ = Reward.balanceOf(e, user);

    assert amount_ == min( _amount, _amount_ );
    assert balance_ == _balance + amount_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimRewardsOnBehalf equals getUserRewards
// - balance of reward increased by min of expected rewards and amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    mathint _amount_ = amount;
    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    mathint amount_ = claimRewardsOnBehalf(e, assets, amount, user, to, Reward);

    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == min( _amount, _amount_ );
    assert balance_ == _balance + amount_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimRewards equals getUserRewards
// - balance of reward increased by min of expected rewards and amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimRewardsAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    mathint _amount_ = amount;
    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    mathint amount_ = claimRewards(e, assets, amount, to, Reward);

    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == min( _amount, _amount_ );
    assert balance_ == _balance + amount_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimAllRewardsOnBehalf equals getUserRewards
// - balance of reward increased by expected rewards
// - accrued is set to zero after claiming
// - reward is Reward as expected
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimAllRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, assets, user, to);

    mathint amount_ = amounts_[0];
    mathint accrued = getUserAccruedRewards(user, Reward);
    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == _amount;
    assert accrued == 0;
    assert balance_ == _balance + _amount;
    assert rewards_[0] == Reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimAllRewards equals getUserRewards
// - balance of reward increased by expected rewards
// - accrued is set to zero after claiming
// - reward is Reward as expected
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimAllRewardsAsExpected(env e, address[] assets, address user, address to) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, assets, to);

    mathint amount_ = amounts_[0];
    mathint accrued = getUserAccruedRewards(user, Reward);
    mathint balance_ = Reward.balanceOf(e, to);

    assert amount_ == _amount;
    assert accrued == 0;
    assert balance_ == _balance + _amount;
    assert rewards_[0] == Reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimed rewards are equal to expected rewards
// - claimAllRewardsToSelf equals getUserRewards
// - balance of reward increased by expected rewards
// - accrued is set to zero after claiming
// - reward is Reward as expected
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimAllRewardsToSelfAsExpected(env e, address[] assets, address user) {
    require rewardsOneAssetsOne(assets[0], Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, user);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf(e, assets);

    mathint amount_ = amounts_[0];
    mathint accrued = getUserAccruedRewards(user, Reward);
    mathint balance_ = Reward.balanceOf(e, user);

    assert amount_ == _amount;
    assert accrued == 0;
    assert balance_ == _balance + _amount;
    assert rewards_[0] == Reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure getAllUserRewards is equal to getUserRewards for ONE asset ONE reward
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimUserRewards(env e, address[] assets, address user, address reward){
    require rewardsOneAssetsOne(assets[0], reward);

    mathint _claimable = getUserRewards(e, assets, user, reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, assets, user);
    mathint claimable_ = amounts[0];

    assert claimable_ == _claimable;
}


/////////////////////////////////////////////////////////////////////////////////
// Ensure claiming twice (in same block) cannot increase amount claimed
// - sum of two claims is less than expected claim
// - if first amount more than claimable, first claim gets all rewards, second claim zero
// - if first amount less than claimable, first claim gets exactly amount requested
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimTwice(env e, address[] assets, address user, address to, address reward, uint256 amount1, uint256 amount2) {
    require rewardsOneAssetsOne(assets[0], reward);

    mathint amount = amount1;
    mathint claimable = getUserRewards(e, assets, user, reward);
    mathint claimedFirst = claimRewardsOnBehalf(e, assets, amount1, user, to, reward);
    mathint claimedSecond = claimRewardsOnBehalf(e, assets, amount2, user, to, reward);

    assert ( claimedFirst + claimedSecond ) <= claimable;
    assert ( amount >= claimable ) => ( claimedFirst == claimable ) && ( claimedSecond == 0 );
    assert ( amount <= claimable ) => ( claimedFirst == amount );
}






