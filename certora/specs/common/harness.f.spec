function harnessFunction(method f) returns bool {
  return f.selector
      == sig:getAssetsList().selector
      || sig:getAssetRewardIndex(address,address).selector
      || sig:getAvailableRewardsCount(address).selector
      || sig:isContract(address).selector
      || sig:inArray(address,address[]).selector;
}
