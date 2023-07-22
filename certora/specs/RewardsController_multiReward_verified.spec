import "methods/Methods_base.spec";
import "methods/Methods_more.spec";
import "OneAssetMultiRewards/zero.spec";
import "OneAssetMultiRewards/invariant.spec";

using DummyERC20_rewardTokenB as RewardB;

///////////////// Properties ///////////////////////

use invariant rewardByAssetIsInList;

use rule zeroAddressAssetUnchanged;
use rule zeroAddressRewardUnchanged;
use rule cannotSetTransferStrategyToZero;

