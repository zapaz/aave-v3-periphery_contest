rule rewardOneClaim(env e, address user, address to) {
    require rewardsOneAssetOne(AToken, Reward);
    // requireInvariant userIndexIncreaseWithSomeAvailableReward(useAToken,Reward);
    address[] assets;

    uint256 amountOnce; uint256 amountTwice;

    uint256 claimable = getUserRewards(e, assets, user, Reward);

    uint256 claimedOnce = claimRewardsOnBehalf(e, assets, amountOnce, user, to, Reward);
    uint256 claimedTwice = claimRewardsOnBehalf(e, assets, amountTwice, user, to, Reward);

    assert assert_uint256(claimedOnce + claimedTwice) <= claimable;
    assert ( amountOnce >= claimable ) => ( claimedOnce == claimable ) && ( claimedTwice == 0 );
    assert ( amountOnce <  claimable ) => ( claimedOnce == amountOnce );

}

rule rewardOneClaimAllRewardsAsExpected(env e, address user, address to) {
    require rewardsOneAssetOne(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, getAssetsList(), to);

    uint256 accrued = getUserAccruedRewards(user, Reward);
    assert accrued == 0;

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert rewards_[0] == Reward;
    assert amounts_[0] == _amount;
}

rule rewardOneClaimAllRewardsToSelfAsExpected(env e, address user) {
    require rewardsOneAssetOne(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, user);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf(e, getAssetsList());

    uint256 accrued = getUserAccruedRewards(user, Reward);
    assert accrued == 0;

    uint256 balance_ = Reward.balanceOf(e, user);
    assert balance_ == _balancePlusAmount;

    assert rewards_[0] == Reward;
    assert amounts_[0] == _amount;
}

rule rewardOneClaimAllRewardsOnBehalfAsExpected(env e, address user, address to) {
    require rewardsOneAssetOne(AToken, Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + _amount);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);

    uint256 accrued = getUserAccruedRewards(user, Reward);
    assert accrued == 0;

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert rewards_[0] == Reward;
    assert amounts_[0] == _amount;
}

rule rewardOneClaimRewardsAsExpected(env e, address user, address to) {
    require rewardsOneAssetOne(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != to;

    uint256 amount;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + min( _amount, amount ));

    uint256 amount_ = claimRewards(e, getAssetsList(), amount, to, Reward);

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert amount_ == min( _amount, amount );
}

rule rewardOneClaimRewardsOnBehalfAsExpected(env e, address user, address to) {
    require rewardsOneAssetOne(AToken, Reward);
    require e.msg.sender == getClaimer(user);
    require getTransferStrategy(Reward) != to;

    uint256 amount;
    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, to);
    uint256 _balancePlusAmount = require_uint256(_balance + min( _amount, amount ));

    uint256 amount_ = claimRewardsOnBehalf(e, getAssetsList(), amount, user, to, Reward);

    uint256 balance_ = Reward.balanceOf(e, to);
    assert balance_ == _balancePlusAmount;

    assert amount_ == min( _amount, amount );
}

rule rewardOneClaimRewardsToSelfAsExpected(env e, address user) {
    require rewardsOneAssetOne(AToken, Reward);
    require e.msg.sender == user;
    require getTransferStrategy(Reward) != user;

    uint256 amount;

    uint256 _amount = getUserRewards(e, getAssetsList(), user, Reward);
    uint256 _balance = Reward.balanceOf(e, user);
    uint256 _balancePlusAmount = require_uint256(_balance + min( _amount, amount ));

    uint256 amount_ = claimRewardsToSelf(e, getAssetsList(), amount, Reward);

    uint256 balance_ = Reward.balanceOf(e, user);
    assert balance_ == _balancePlusAmount;

    assert amount_ == min( _amount, amount );
}

rule rewardOneClaimUserRewards(env e, address user){
    require rewardsOneAssetOne(AToken, Reward);

    address[] assets;

    uint256 _claimable = getUserRewards(e, assets, user, Reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, assets, user);
    uint256 claimable_ = amounts[0];

    assert claimable_ == _claimable;
}
