import "./functions.spec";

rule claimAllAsExpected(address user, address reward, address to) {
    storage initial = lastStorage;

    env e;
    require e.msg.sender == user;
    require oneAssetOneReward(AToken, reward);

    address[] rewards;
    uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, getAssetsList(), user);
    assert rewards[0] == reward;

    address[] rewards1;
    uint256[] amounts1;
    rewards1, amounts1 = claimAllRewards(e, getAssetsList(), to)  at initial;
    assert rewards1[0] == reward;
    assert amounts1[0] == amounts[0];

    address[] rewards2;
    uint256[] amounts2;
    rewards2, amounts2 = claimAllRewardsToSelf(e, getAssetsList())  at initial;
    assert rewards2[0] == reward;
    assert amounts2[0] == amounts[0];

    address[] rewards3;
    uint256[] amounts3;
    require ( getClaimer(user) == e.msg.sender );
    rewards3, amounts3 = claimAllRewardsOnBehalf(e, getAssetsList(), user, to)  at initial;
    assert rewards3[0] == reward;
    assert amounts3[0] == amounts[0];
}

