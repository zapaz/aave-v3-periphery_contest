invariant timestamp(env e, address asset, address reward)
    getLastUpdateTimestamp(asset, reward) <= e.block.timestamp
    { preserved with (env ep) { require  ep.block.timestamp == e.block.timestamp; } }

invariant rewardEnabled(address reward)
    isRewardEnabled(reward) <=> inArray(getRewardsList(), reward);

// invariant rewardsLength(address asset)
//     getRewardsByAssetLength(asset) <= getRewardsListLength()
//     filtered { f -> !f.isView && !harnessFunction(f) }
//     { preserved {
//         require (forall address reward . isRewardEnabled(reward) <=> inArray( getRewardsList(), reward) );
//     } }

// rule rewardsLengthRule(method f, env e, calldataarg args, address asset) filtered {
//     f -> !f.isView && !harnessFunction(f)
// } {
//   address[] rewards = getRewardsList();
//   require (forall address reward . isRewardEnabled(reward) <=> inArray(rewards, reward) );

//   require getRewardsByAssetLength(asset) <= getRewardsListLength();
//   f(e, args);
//   assert  getRewardsByAssetLength(asset) <= getRewardsListLength();
// }