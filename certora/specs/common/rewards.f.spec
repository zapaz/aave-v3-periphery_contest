/////////////////////////////////////////////////////////////////////////////////
// Requirements for ONE reward
/////////////////////////////////////////////////////////////////////////////////
function rewardsOne(address reward) returns bool {
    address[] rewardsList = getRewardsList();

    return  rewardsList.length == 1
        && rewardsList[0] == reward;
}

/////////////////////////////////////////////////////////////////////////////////
// Requirements for ONE reward ONE asset
/////////////////////////////////////////////////////////////////////////////////
function rewardsOneAssetsOne(address asset, address reward) returns bool {
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return assetsOne(asset)
        && rewardsOne(reward)
        && rewardsByAsset.length == 1
        && rewardsByAsset[0] == reward
        && getAvailableRewardsCount(asset) == 1;
}

/////////////////////////////////////////////////////////////////////////////////
// Requirements for TWO rewards
/////////////////////////////////////////////////////////////////////////////////
function rewardsTwo(address reward1, address reward2) returns bool {
    address[] rewardsList = getRewardsList();

    return rewardsList.length == 2
        && rewardsList[0] == reward1
        && rewardsList[1] == reward2;
}

/////////////////////////////////////////////////////////////////////////////////
// Requirements for TWO rewards ONE asset
/////////////////////////////////////////////////////////////////////////////////
function rewardsTwoAssetOne(address asset, address reward1, address reward2) returns bool {
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return assetsOne(asset)
        && rewardsTwo(reward1, reward2)
        && rewardsByAsset.length == 2
        && rewardsByAsset[0] == reward1
        && rewardsByAsset[1] == reward2
        && getAvailableRewardsCount(asset) == 2;
}

