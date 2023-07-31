function oneReward(address reward) returns bool {
    address[] rewardsList = getRewardsList();

    return  rewardsList.length == 1
        && rewardsList[0] == reward;
}

function oneAssetOneReward(address asset, address reward) returns bool {
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return oneAsset(asset)
        && oneReward(reward)
        && rewardsByAsset.length == 1
        && rewardsByAsset[0] == reward
        && getAvailableRewardsCount(asset) == 1;
}
