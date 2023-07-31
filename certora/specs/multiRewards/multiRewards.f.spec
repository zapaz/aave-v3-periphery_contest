function multiRewards(address reward1, address reward2) returns bool {
    address[] rewardsList = getRewardsList();

    return rewardsList.length == 2
        && rewardsList[0] == reward1
        && rewardsList[1] == reward2;
}

function oneAssetMultiRewards(address asset, address reward1, address reward2) returns bool {
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return oneAsset(asset)
        && multiRewards(reward1, reward2)
        && rewardsByAsset.length == 2
        && rewardsByAsset[0] == reward1
        && rewardsByAsset[1] == reward2
        && getAvailableRewardsCount(asset) == 2;
}
