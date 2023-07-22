import "./oneFunctions.spec";
import "./oneClaimFunctions.spec";

// invariant oneClaimRewardSameAsExpected(env e, address user, address reward, address to)
//     oneAssetOneReward(AToken, reward) =>
//       oneClaimFirstRewardExpectedAmount(e, user) ==
//       getUserRewards(e, getAssetsList(), user, reward);

function oneClaimRewardExpectedAmount(env e, address user, address asset, address reward) returns uint256 {
    require oneAssetOneReward(asset, reward);

    address[] rewards; uint256[] amounts;
    rewards, amounts = getAllUserRewards(e, getAssetsList(), user);

    assert rewards[0] == reward;

    return amounts[0];
}


rule oneClaimAllRewardsAsExpected(env e, address user, address reward, address to) {
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewards(e, getAssetsList(), to);

    assert rewards_[0] == reward;
    assert amounts_[0] == _amount;
}

rule oneClaimAllRewardsToSelfAsExpected(env e, address user, address reward, address to) {
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsToSelf(e, getAssetsList());

    assert rewards_[0] == reward;
    assert amounts_[0] == _amount;
}

rule oneClaimAllRewardsOnBehalfAsExpected(env e, address user, address reward, address to) {
    require e.msg.sender == getClaimer(user);

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    address[] rewards_; uint256[] amounts_;
    rewards_, amounts_ = claimAllRewardsOnBehalf(e, getAssetsList(), user, to);

    assert rewards_[0] == reward;
    assert amounts_[0] == _amount;
}

rule oneClaimRewardsAsExpected(env e, address user, address reward, address to) {
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    uint256 amount_ = claimRewards(e, getAssetsList(), _amount, to, reward);

    assert amount_ == _amount;
}

rule oneClaimRewardsOnBehalfAsExpected(env e, address user, address reward, address to) {
    require e.msg.sender == getClaimer(user);

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    uint256 amount_ = claimRewardsOnBehalf(e, getAssetsList(), _amount, user, to, reward);

    assert amount_ == _amount;
}

rule oneClaimRewardsToSelfAsExpected(env e, address user, address reward, address to) {
    require e.msg.sender == user;

    uint256 _amount = oneClaimRewardExpectedAmount(e, user, AToken, reward);

    uint256 amount_ = claimRewardsToSelf(e, getAssetsList(), _amount, reward);

    assert amount_ == _amount;
}

rule oneClaimRewardUnchanged(address user, method f, env e, calldataarg args) {
    uint256 _reward = oneClaimRewardExpectedAmount(e, user, AToken, Reward);

    f(e, args);

    uint256 reward_ = oneClaimRewardExpectedAmount(e, user, AToken, Reward);

    assert reward_ == _reward;
}


