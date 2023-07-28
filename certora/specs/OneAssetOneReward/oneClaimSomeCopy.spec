// Conditions to get rewards :
// AToken user balance > 0
// AToken totalSupply >= user balance
// AToken index >= user index
// timestamp < distributionEnd
// emissionPerSecond * (timestamp - lastUpdateTimestamp) > totalSupply
rule oneClaimSome(env e, address user) {
    require oneAssetOneReward(AToken, Reward);
    requireInvariant user_index_LEQ_index(AToken, Reward, user);

    uint256 totalSupply = AToken.totalSupply(e);
    uint256 balance = AToken.balanceOf(e, user);
    require balance > 0;
    require totalSupply >= balance;

    uint256 index;
    uint256 emissionPerSecond;
    uint256 lastUpdateTimestamp;
    uint256 distributionEnd;
    index, emissionPerSecond, lastUpdateTimestamp, distributionEnd =  getRewardsData(e, AToken, Reward);

    require e.block.timestamp < distributionEnd;
    require emissionPerSecond * e.block.timestamp > emissionPerSecond * lastUpdateTimestamp + totalSupply;

    assert getUserRewards(e, getAssetsList(), user, Reward) > 0;
}
