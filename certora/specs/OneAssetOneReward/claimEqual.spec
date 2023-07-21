rule claimSome(address user, address reward, address to) {
    requireInvariant user_index_LEQ_index(AToken, reward, user);

    uint256 deltaTime = 1200;

    address[] assetsList = getAssetsList();
    require assetsList.length == 1;
    require assetsList[0] == AToken;

    uint256 decimals = getAssetDecimals(AToken);
    require decimals <= 18;
    require decimals >= 6;
    require getAvailableRewardsCount(AToken) == 1;

    address[] rewardsList = getRewardsList();
    require rewardsList.length == 1;
    require rewardsList[0] == reward;

    address[] rewardsByAsset = getRewardsByAsset(AToken);
    require rewardsByAsset.length == 1;
    require rewardsByAsset[0] == reward;

    env e;
    require e.msg.sender == user;

    uint256 index;
    uint256 emissionPerSecond;
    uint256 lastUpdateTimestamp;
    uint256 distributionEnd;
    index, emissionPerSecond, lastUpdateTimestamp, distributionEnd =  getRewardsData(e, AToken, reward);

    require e.block.timestamp == require_uint256(lastUpdateTimestamp + deltaTime);
    require index < max_uint96;
    require emissionPerSecond > 0;
    require emissionPerSecond < max_uint96;
    require distributionEnd > e.block.timestamp;
    require AToken.totalSupply(e) > 0;

    uint256 userBalance = AToken.balanceOf(e, user);
    uint256 userIndex = getUserAssetIndex(user, AToken, reward);
    uint256 assetUnit = require_uint256(10^decimals);
    uint256 reserveIndex =  require_uint256((emissionPerSecond * deltaTime * assetUnit) / AToken.totalSupply(e));
    uint256 claimable = require_uint256(( userBalance * (reserveIndex - userIndex) ) /  assetUnit);

    address[] rewards;
    uint256[] claimedAmounts;
    uint256 _oldAssetIndex;
    uint256 _newAssetIndex;
    _oldAssetIndex, _newAssetIndex = getAssetIndex(e, AToken, reward);
    uint256 _userIndex = getUserAssetIndex(user, AToken, reward);
    uint256 _userAccrued = getUserAccruedRewards(user, reward);

    rewards, claimedAmounts = claimAllRewards(e, assetsList, to);

    uint256 oldAssetIndex_;
    uint256 newAssetIndex_;
    oldAssetIndex_, newAssetIndex_ = getAssetIndex(e, AToken, reward);
    uint256 userIndex_ = getUserAssetIndex(user, AToken, reward);
    uint256 userAccrued_ = getUserAccruedRewards(user, reward);

    assert index == _newAssetIndex;
    assert rewards[0] == reward;
    assert claimable == claimedAmounts[0];
}



