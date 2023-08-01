invariant rewardsZero (address asset)
    getAvailableRewardsCount(asset) == 0 => rewardsCount(asset) == 0;

// invariant rewardByAssetIsInList(uint256 index)
//   index < rewardsAssetLength() => inArray(rewardsAsset(index), getRewardsList());
