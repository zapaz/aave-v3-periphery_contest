rule shouldClaimAgainAfterBlocks(address user, address reward, address to) {
    uint256 decimals = getAssetDecimals(AToken);
    require decimals <= 18;
    require decimals >= 6;
    require getAvailableRewardsCount(AToken) == 1;

    address[] assetsList = getAssetsList();
    require assetsList.length == 1;
    require assetsList[0] == AToken;

    address[] rewardsList = getRewardsList();
    require rewardsList.length == 1;
    require rewardsList[0] == reward;

    address[] rewardsByAsset = getRewardsByAsset(AToken);
    require rewardsByAsset.length == 1;
    require rewardsByAsset[0] == reward;

    address[] rewards1;
    address[] rewards2;
    uint256[] claimedAmounts1;
    uint256[] claimedAmounts2;

    env e1;
    uint256 index1;
    uint256 emissionPerSecond1;
    uint256 lastUpdateTimestamp1;
    uint256 distributionEnd1;
    require e1.msg.sender == user;
    index1, emissionPerSecond1, lastUpdateTimestamp1, distributionEnd1 =  getRewardsData(e1, AToken, reward);
    require e1.block.timestamp == require_uint256(lastUpdateTimestamp1 + 12000);
    require index1 < max_uint96;
    require emissionPerSecond1 > 0;
    require emissionPerSecond1 < max_uint96;
    require distributionEnd1 > e1.block.timestamp;
    require AToken.totalSupply(e1) > 0;

    uint256 accrued1 = getUserAccruedRewards(user, reward);
    rewards1, claimedAmounts1 = claimAllRewards(e1, assetsList, to);

    env e2;
    uint256 index2;
    uint256 emissionPerSecond2;
    uint256 lastUpdateTimestamp2;
    uint256 distributionEnd2;
    require e2.msg.sender == user;
    require e2.block.timestamp == require_uint256(e1.block.timestamp + 12000);
    require e2.block.number == require_uint256(e1.block.number + 1000);
    index2, emissionPerSecond2, lastUpdateTimestamp2, distributionEnd2 =  getRewardsData(e2, AToken, reward);
    require e2.block.timestamp == require_uint256(lastUpdateTimestamp2 + 12000);
    require index2 < max_uint96;
    require emissionPerSecond2 > 0;
    require emissionPerSecond2 < max_uint96;
    require distributionEnd2 > e2.block.timestamp;

    // firstTerm = emissionPerSecond * timeDelta * assetUnit  > totalSupply
    require require_uint256( emissionPerSecond2 * 12000 * ( 10^decimals ) )  > AToken.totalSupply(e2);

    uint256 accrued2 = getUserAccruedRewards(user, reward);
    rewards2, claimedAmounts2 = claimAllRewards(e2, assetsList, to);

    uint256 accrued3 = getUserAccruedRewards(user, reward);

    address reward1 = rewards1[0];
    address reward2 = rewards2[0];
    uint256 claimedAmount1 = claimedAmounts1[0];
    uint256 claimedAmount2 = claimedAmounts2[0];

    assert reward1 == reward2;
    assert claimedAmount1 > 0 => claimedAmount2 > 0;
}


rule user_index_keeps_growing(address asset, address reward, address user, method f) filtered { f -> !f.isView } {
    uint256 _index = getUserAssetIndex(user, asset, reward);

    env e; calldataarg args;
    f(e, args);

    uint256 index_ = getUserAssetIndex(user, asset, reward);

    assert index_ >= _index;
}
