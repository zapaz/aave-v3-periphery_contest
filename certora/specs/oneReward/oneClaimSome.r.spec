function oneClaimable(env e, address user) returns uint256 {
    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, getAssetsList(), user);

    return amounts[0];
}
rule oneClaimSome(env e, address user) {
    require oneAssetOneReward(AToken, Reward);

    uint256 totalSupply = AToken.totalSupply(e);
    uint256 balance = AToken.balanceOf(e, user);
    require balance > 0;
    require totalSupply >= balance;

    uint256 index;
    uint256 emissionPerSecond;
    uint256 lastUpdateTimestamp;
    uint256 distributionEnd;
    index, emissionPerSecond, lastUpdateTimestamp, distributionEnd =  getRewardsData(e, AToken, Reward);

    require index >= getUserAssetIndex(user, AToken, Reward);
    require e.block.timestamp < distributionEnd;
    require emissionPerSecond * e.block.timestamp > emissionPerSecond * lastUpdateTimestamp + totalSupply;

    assert oneClaimable(e, user) > 0;
}