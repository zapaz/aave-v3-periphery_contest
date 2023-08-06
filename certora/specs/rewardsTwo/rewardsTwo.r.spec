rule rewardsTwoByAssetAreInList(method f, env e, calldataarg args) filtered {
    f -> !f.isView && !harnessFunction(f)
} {
  require rewardsTwoAssetOne(AToken, Reward, RewardB);

  f@withrevert(e,args);

  address[] rewardsByAsset_ = getRewardsByAsset(AToken);
  address[] rewardsList_ = getRewardsList();

  assert rewardsByAsset_[0] == rewardsList_[0];
  assert rewardsByAsset_[1] == rewardsList_[1];
}

rule rewardTwoUserRewards(env e, address[] assets, address user) {
    require rewardsTwoAssetOne(AToken, Reward, RewardB);
    require assets[0] == AToken;
    require assets.length == 1;
    require getAssetDecimals(AToken) == 6;

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, assets, user);

    uint256 _claimable  = amounts[0];
    uint256 _claimableB = amounts[1];

    // uint256 claimable_  = userRewardsCalculate(e, user, Reward);
    uint256 claimableB_ = userRewardsCalculate(e, user, RewardB);

    // assert  claimable_ == _claimable;
    assert  claimableB_ == _claimableB;

    // assert  rewards[0] == Reward;
    assert  rewards[1] == RewardB;
}
