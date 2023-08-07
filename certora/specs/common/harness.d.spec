definition harnessFunction(method f) returns bool =
        f.selector == sig:configureAsset(address,address,address).selector;

definition harnessReadFunction(method f) returns bool =
        f.selector == sig:getAssetsList().selector
    ||  f.selector == sig:getAssetRewardIndex(address,address).selector
    ||  f.selector == sig:getAvailableRewardsCount(address).selector
    ||  f.selector == sig:isContract(address).selector
    ||  f.selector == sig:inArray(address[],address).selector;

