// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.10;

import {RewardsController} from "../../contracts/rewards/RewardsController.sol";
import {RewardsDataTypes} from "../../contracts/rewards/libraries/RewardsDataTypes.sol";
import {ITransferStrategyBase} from "../../contracts/rewards/interfaces/ITransferStrategyBase.sol";
import {IEACAggregatorProxy} from "../../contracts/misc/interfaces/IEACAggregatorProxy.sol";

contract RewardOracleHarness {
    function latestAnswer() external returns (uint256) {
        return 42;
    }
}

contract RewardsControllerHarness is RewardsController {
    address public rewardOracle;

    constructor(address emissionManager) RewardsController(emissionManager) {
        rewardOracle = address(new RewardOracleHarness());
    }

    function isRewardEnabled(address reward) external view returns (bool) {
        return _isRewardEnabled[reward];
    }

    function getAssetsList() external view returns (address[] memory) {
        return _assetsList;
    }

    // returns an asset's reward index
    function getAssetRewardIndex(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].index;
    }

    function getlastUpdateTimestamp(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].lastUpdateTimestamp;
    }

    function getAvailableRewardsCount(address asset) external view returns (uint128) {
        return _assets[asset].availableRewardsCount;
    }

    function getEmissionPerSecond(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].emissionPerSecond;
    }

    function createConfigAsset(address asset, address reward, address transferStrategy)
        public
        returns (RewardsDataTypes.RewardsConfigInput memory config)
    {
        config.asset = asset;
        config.reward = reward;
        config.transferStrategy = ITransferStrategyBase(transferStrategy);
        config.rewardOracle = IEACAggregatorProxy(rewardOracle);
    }

    function configureAsset(address asset, address reward, address transferStrategy) external {
        RewardsDataTypes.RewardsConfigInput[] memory configs = new RewardsDataTypes.RewardsConfigInput[](1);
        configs[0] = createConfigAsset(asset, reward, transferStrategy);

        this.configureAssets(configs);
    }

    function isContract(address account) external view returns (bool) {
        return _isContract(account);
    }

    function inArray(address[] memory array, address addr) public pure returns (bool) {
        for (uint256 i = 0; i < array.length; i++) {
            if (array[i] == addr) {
                return true;
            }
        }
        return false;
    }
}
