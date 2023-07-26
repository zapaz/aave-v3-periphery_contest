import "methods/Methods_base.spec";
import "methods/Methods_more.spec";
import "OneAsset/oneAsset.spec";
import "OneAssetMultiRewards/zero.spec";
import "OneAssetMultiRewards/multiRewards.spec";
import "OneAssetMultiRewards/oneAssetMultiRewards.spec";

using DummyERC20_rewardTokenB as RewardB;

///////////////// Properties ///////////////////////

use rule rewardsByAssetAreInList;

use rule zeroAddressAssetUnchanged;
use rule zeroAddressRewardUnchanged;
use rule cannotSetTransferStrategyToZero;

