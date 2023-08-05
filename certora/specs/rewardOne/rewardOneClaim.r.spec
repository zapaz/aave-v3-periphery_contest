rule rewardOneClaimRewardsToSelfAsExpected(env e, address[] assets, address user, uint256 amount) {
    require rewardsOneAssetOne(AToken, Reward);
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

rule rewardOneClaimRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsOneAssetOne(assets[0], Reward);
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

rule rewardOneClaimRewardsAsExpected(env e, address[] assets, address user, address to, uint256 amount) {
    require rewardsOneAssetOne(assets[0], Reward);
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

rule rewardOneClaimAllRewardsOnBehalfAsExpected(env e, address[] assets, address user, address to) {
    require rewardsOneAssetOne(assets[0], Reward);
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

rule rewardOneClaimAllRewardsAsExpected(env e, address[] assets, address user, address to) {
    require rewardsOneAssetOne(assets[0], Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    mathint _amount = getUserRewards(e, assets, user, Reward);
    mathint _balance = Reward.balanceOf(e, to);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, assets, to);

    mathint amount_ = amounts_[0];
    // mathint accrued = getUserAccruedRewards(user, Reward);
    // mathint balance_ = Reward.balanceOf(e, to);
    // assert accrued == 0;
    // assert balance_ == _balance + _amount;

    assert amount_ == _amount;
    assert rewards_[0] == Reward;
}

rule rewardOneClaimAllRewardsToSelfAsExpected(env e, address[] assets, address user) {
    require rewardsOneAssetOne(assets[0], Reward);
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

rule rewardOneClaimUserRewards(env e, address[] assets, address user, address reward){
    require rewardsOneAssetOne(assets[0], reward);

    mathint _claimable = getUserRewards(e, assets, user, reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, assets, user);
    mathint claimable_ = amounts[0];

    assert claimable_ == _claimable;
}

rule rewardOneClaimTwice(env e, address[] assets, address user, address to, address reward, uint256 amount1, uint256 amount2) {
    require rewardsOneAssetOne(assets[0], reward);

    mathint amount = amount1;
    mathint claimable = getUserRewards(e, assets, user, reward);
    mathint claimedFirst = claimRewardsOnBehalf(e, assets, amount1, user, to, reward);
    mathint claimedSecond = claimRewardsOnBehalf(e, assets, amount2, user, to, reward);

    assert ( claimedFirst + claimedSecond ) <= claimable;
    assert ( amount >= claimable ) => ( claimedFirst == claimable ) && ( claimedSecond == 0 );
    assert ( amount <  claimable ) => ( claimedFirst == amount );
}






